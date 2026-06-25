# 출처와 검증

이 사이트의 본문은 다음 출처만 근거로 삼습니다.

## 1차 출처

- [Claude Agent SDK 공식 문서](https://code.claude.com/docs/en/agent-sdk/overview.md)
- [Claude Agent SDK Python GitHub 저장소](https://github.com/anthropics/claude-agent-sdk-python)
- [Claude Cookbooks 공식 페이지](https://platform.claude.com/cookbooks)
- 이 포크의 `registry.yaml`, notebook, Python 파일, README

## 생성 방식

`scripts/build_pages_docs.py`가 `registry.yaml`과 `docs/data/book_projection.yml`을 읽어 다음 문서를 생성합니다.

- `docs/projection/chapter-map.md`
- `docs/projection/part*.md`
- `docs/projection/chapters/*.md`
- `docs/recipes/*.md`

챕터 매핑을 바꿀 때는 생성된 Markdown을 직접 고치지 말고 `docs/data/book_projection.yml`을 수정한 뒤 생성 스크립트를 다시 실행합니다.

```bash
python scripts/build_pages_docs.py
mkdocs build --strict
```
