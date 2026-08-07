---
name: sync-upstream
description: Merge anthropics/claude-cookbooks into this fork without pulling in CI workflows. Use whenever upstream needs to be synced, merged, or pulled.
---

# Sync Upstream

This fork tracks `anthropics/claude-cookbooks` but runs no CI. The only live
Actions workflow is `pages-build-deployment`, which GitHub generates for the
legacy Pages deploy and which has no file in `.github/workflows/`.

Upstream ships nine workflow files. If they land here they run against every
changed notebook — including the 87 `*_kr.ipynb` Korean translations — which
costs API budget and turns the Actions tab red for reasons unrelated to this
fork's work.

So the rule is: take everything upstream has **except** `.github/workflows/`.

## Workflow

1. Confirm the working tree is clean. The script refuses to run otherwise, and
   a conflicted merge is hard enough to read without unrelated edits in it.

2. Run the script:

   ```bash
   scripts/sync_upstream.sh              # defaults to upstream/main
   scripts/sync_upstream.sh upstream/v2  # or any ref
   ```

   It fetches, merges, deletes `.github/workflows/`, commits, and verifies the
   directory ended up empty.

3. If it stops with *conflicts outside .github/workflows*, resolve those by
   hand, then finish with:

   ```bash
   git rm -rf --ignore-unmatch .github/workflows && git commit
   ```

4. Ask GitHub whether it agrees. The file being gone is necessary but not
   sufficient — a workflow that ran before can linger in the Actions list:

   ```bash
   gh workflow list --all | grep -v pages-build-deployment
   ```

   Empty output means only the Pages deploy can run. Anything else is a
   workflow that can still fire; disable it:

   ```bash
   gh workflow disable "<name>"
   ```

5. Push, then confirm the Pages deploy succeeded:

   ```bash
   git push origin main
   gh run list --limit 3
   ```

## Checking the translations after a sync

Upstream edits notebooks that have `*_kr.ipynb` siblings. A sync can therefore
leave a translation describing code that has changed underneath it.

Each translation records the source commit it was made from, in notebook
metadata under `korean_translation.source_commit`. To find translations whose
source moved after that commit:

```bash
uv run python - <<'PY'
import glob, json, subprocess
for kr in sorted(glob.glob("**/*_kr.ipynb", recursive=True)):
    meta = json.load(open(kr, encoding="utf-8"))["metadata"].get("korean_translation")
    if not meta:
        continue
    src, since = meta["source_path"], meta["source_commit"]
    moved = subprocess.run(
        ["git", "log", "--oneline", f"{since}..HEAD", "--", src],
        capture_output=True, text=True,
    ).stdout.strip()
    if moved:
        print(f"{kr}\n  source changed since {since[:8]}:\n{moved}\n")
PY
```

Re-translate only the markdown cells of whatever that prints. Code cells stay
byte-identical to the source notebook — that invariant is what makes this check
work, so do not "fix" code in a translation.

## What not to do

- **Do not run a bare `git merge upstream/main`.** The `.gitattributes` entry
  only covers content merges. When upstream modifies a workflow file this fork
  deleted, git raises a modify/delete conflict that no merge driver resolves,
  and a careless resolution restores the file.
- **Do not re-add workflow files** to make a merge go quietly. Deleting them is
  the point.
- **Do not enable workflows** to "check if they pass". Notebook Tests executes
  notebooks against the live API.
