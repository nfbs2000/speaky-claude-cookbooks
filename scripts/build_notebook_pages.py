"""Render every *_kr.ipynb into docs/notebooks/ as a standalone page.

The site is served by legacy GitHub Pages straight out of docs/, so anything
written here is live on the next push. Output mirrors the source tree, which
keeps the seven different guide_kr.ipynb files from colliding and gives each
notebook a category for free: its top-level directory.

Run from the repo root:

    uv run python scripts/build_notebook_pages.py

Caveat: mkdocs is not aware of these files. A `mkdocs build` aimed at docs/
would clean them out, since it removes what it did not generate.
"""

from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path

import nbformat
from nbconvert import HTMLExporter

WIDGET_MIME = "application/vnd.jupyter.widget-state+json"

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "notebooks"
REPO = "https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main"

# Directory name -> what to call it in the index. Anything not listed falls
# back to the bare directory name, so a new top-level folder still renders.
CATEGORY_LABELS = {
    "capabilities": "핵심 기능",
    "claude_agent_sdk": "Agent SDK",
    "coding": "코딩",
    "extended_thinking": "확장 사고",
    "fable_5_fallback_billing": "Fable 5 폴백·과금",
    "finetuning": "파인튜닝",
    "managed_agents": "Managed Agents",
    "misc": "기타",
    "multimodal": "멀티모달",
    "observability": "관측 가능성",
    "patterns": "에이전트 패턴",
    "skills": "스킬",
    "third_party": "서드파티 연동",
    "tool_evaluation": "도구 평가",
    "tool_use": "도구 사용",
}

# Roughly how useful each category is as a starting point, so the index does
# not open on "기타". Everything unlisted sorts after these, alphabetically.
CATEGORY_ORDER = [
    "misc",
    "tool_use",
    "capabilities",
    "multimodal",
    "patterns",
    "claude_agent_sdk",
    "managed_agents",
    "skills",
    "extended_thinking",
    "third_party",
    "coding",
    "observability",
    "finetuning",
    "tool_evaluation",
    "fable_5_fallback_billing",
]


def korean_title(nb_path: Path) -> str:
    """First H1 of the translated notebook, else a readable filename."""
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        for line in "".join(cell.get("source", [])).splitlines():
            if line.startswith("# "):
                # Strip trailing mkdocs anchors like {#setup}.
                return re.sub(r"\s*\{#[^}]*\}\s*$", "", line[2:]).strip()
    return nb_path.stem.replace("_kr", "").replace("_", " ")


def render(exporter: HTMLExporter, src: Path) -> tuple[Path, int]:
    rel = src.relative_to(ROOT).with_suffix(".html")
    dest = OUT / rel
    dest.parent.mkdir(parents=True, exist_ok=True)

    nb = nbformat.read(src, as_version=4)

    # Five of the third_party notebooks carry a widget-state block with no
    # "state" key, which makes nbconvert's widget filter raise KeyError. The
    # same block is in the upstream originals, so drop it here rather than
    # editing the notebooks: the translations must stay byte-identical to
    # their sources in everything but the markdown.
    widgets = nb.get("metadata", {}).get("widgets")
    if widgets and "state" not in widgets.get(WIDGET_MIME, {}):
        nb.metadata.pop("widgets", None)

    body, _ = exporter.from_notebook_node(nb)
    dest.write_text(body, encoding="utf-8")
    return rel, dest.stat().st_size


def build_index(entries: list[dict]) -> str:
    by_category: dict[str, list[dict]] = {}
    for e in entries:
        by_category.setdefault(e["category"], []).append(e)

    ordered = [c for c in CATEGORY_ORDER if c in by_category]
    ordered += sorted(c for c in by_category if c not in CATEGORY_ORDER)

    sections = []
    for cat in ordered:
        items = sorted(by_category[cat], key=lambda e: e["title"])
        rows = "\n".join(
            f'''      <li><a class="item" href="{html.escape(e["href"])}">
        <span class="title">{html.escape(e["title"])}</span>
        <span class="path">{html.escape(e["source"])}</span>
      </a></li>'''
            for e in items
        )
        label = CATEGORY_LABELS.get(cat, cat)
        sections.append(
            f'''  <section>
    <h2>{html.escape(label)} <span class="count">{len(items)}</span></h2>
    <div class="dir">{html.escape(cat)}/</div>
    <ul>
{rows}
    </ul>
  </section>'''
        )

    return TEMPLATE.format(total=len(entries), sections="\n\n".join(sections))


TEMPLATE = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>한국어 쿡북 노트북</title>
<style>
  :root {{
    --bg: #ffffff; --fg: #1a1a1a; --muted: #6b6b6b;
    --line: #e6e6e6; --accent: #c15f3c; --chip: #f4f0ed;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #191919; --fg: #ececec; --muted: #999999;
      --line: #303030; --accent: #e08d6d; --chip: #262220;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; padding: 3.5rem 1.5rem 5rem;
    background: var(--bg); color: var(--fg);
    font: 16px/1.65 -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo",
          Pretendard, "Noto Sans KR", sans-serif;
  }}
  main {{ max-width: 52rem; margin: 0 auto; }}
  h1 {{ font-size: 1.8rem; margin: 0 0 .4rem; letter-spacing: -.02em; }}
  .lede {{ color: var(--muted); margin: 0 0 .6rem; }}
  .total {{ color: var(--muted); font-size: .88rem; margin: 0 0 3rem; }}
  section {{ margin: 0 0 2.75rem; }}
  h2 {{
    font-size: 1.05rem; margin: 0 0 .1rem;
    display: flex; align-items: baseline; gap: .5rem;
  }}
  .count {{
    font-size: .75rem; font-weight: 500; color: var(--muted);
    background: var(--chip); padding: .1rem .45rem; border-radius: 999px;
  }}
  .dir {{
    color: var(--muted); font-size: .78rem; margin: 0 0 .7rem;
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  }}
  ul {{ list-style: none; padding: 0; margin: 0; }}
  li {{ border-top: 1px solid var(--line); }}
  li:last-child {{ border-bottom: 1px solid var(--line); }}
  a.item {{
    display: flex; flex-wrap: wrap; align-items: baseline; gap: .25rem 1rem;
    padding: .8rem .3rem; color: inherit; text-decoration: none;
  }}
  a.item:hover {{ background: color-mix(in srgb, var(--accent) 9%, transparent); }}
  .title {{ font-weight: 600; flex: 1 1 22rem; }}
  .path {{
    color: var(--muted); font-size: .78rem;
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  }}
  .note {{
    margin-top: 3rem; padding: 1rem 1.1rem;
    border-left: 3px solid var(--accent);
    background: color-mix(in srgb, var(--accent) 6%, transparent);
    color: var(--muted); font-size: .88rem;
  }}
  .note strong {{ color: var(--fg); }}
  a {{ color: var(--accent); }}
</style>
</head>
<body>
<main>
  <h1>한국어 쿡북 노트북</h1>
  <p class="lede">원본 노트북의 마크다운 셀만 한국어로 옮긴 판본입니다. 코드와 실행 결과는 원본 그대로입니다.</p>
  <p class="total">전체 {total}편 · 분류는 저장소의 디렉터리를 따릅니다</p>

{sections}

  <p class="note">
    <strong>번역 범위.</strong> 설명(마크다운)만 한국어이고 코드 셀은 원본과 바이트 단위로 같습니다.
    실행 결과와 코드 주석은 영어 그대로입니다.
    원본은 <a href="https://github.com/nfbs2000/speaky-claude-cookbooks">GitHub 저장소</a>에서 볼 수 있습니다.
  </p>
</main>
</body>
</html>
"""


def main() -> None:
    sources = sorted(ROOT.glob("**/*_kr.ipynb"))
    sources = [p for p in sources if ".git" not in p.parts and "docs" not in p.parts]
    if not sources:
        raise SystemExit("no *_kr.ipynb found")

    # Rebuild from scratch so a renamed or deleted notebook does not leave a
    # stale page behind.
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    exporter = HTMLExporter()
    exporter.exclude_input_prompt = True
    exporter.exclude_output_prompt = True

    entries, total_bytes = [], 0
    for src in sources:
        rel, size = render(exporter, src)
        total_bytes += size
        source_rel = str(src.relative_to(ROOT))
        entries.append(
            {
                "title": korean_title(src),
                "href": str(rel),
                "source": source_rel,
                "category": src.relative_to(ROOT).parts[0],
            }
        )
        print(f"  {size / 1024:>7.0f} KB  {rel}")

    (OUT / "index.html").write_text(build_index(entries), encoding="utf-8")

    print(f"\n{len(entries)} notebooks -> {OUT.relative_to(ROOT)}")
    print(f"{total_bytes / 1024 / 1024:.1f} MB of HTML")


if __name__ == "__main__":
    main()
