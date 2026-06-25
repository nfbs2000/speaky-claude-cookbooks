# Speaky Claude Cookbooks

이 사이트는 한국어 Claude Agent SDK 책의 내용을 공개된 Claude Agent SDK 문서와 이 포크의 실행 가능한 Python/Jupyter cookbook에 맞춰 다시 배치한 GitHub Pages 문서입니다.

책은 Claude Code/Agent SDK의 내부 구조를 교육용으로 깊게 설명하지만, 공개 사이트에서는 **공식 문서와 이 저장소에서 확인 가능한 예제**만 근거로 삼습니다. 내부 구현명, 비공개 기능 플래그, 숨은 프롬프트 원문처럼 공개 검증이 어려운 항목은 그대로 옮기지 않고 공개 API와 실행 예제로 재작성합니다.

## 읽는 순서

1. [공개 투영 개요](projection/index.md)에서 원칙을 확인합니다.
2. [전체 챕터 매핑](projection/chapter-map.md)에서 책의 각 장이 어떤 cookbook 자료로 재배치되는지 봅니다.
3. [Agent SDK 레시피](recipes/agent-sdk.md)부터 실행 가능한 노트북을 따라갑니다.
4. 공개/비공개 경계가 애매한 장은 [공개 경계](reference/public-boundary.md)를 먼저 읽습니다.

## 핵심 원칙

- 책 원문을 그대로 복제하지 않습니다.
- 공개 SDK 문서, 이 저장소의 노트북, Python 파일, README를 근거로 다시 씁니다.
- 각 장마다 관련 cookbook, 공식 문서, 공개 제한 사항, 신뢰도를 표시합니다.
- 실행 가능한 예제를 우선합니다. 개념 설명은 항상 실제 파일 링크와 함께 둡니다.

## 주요 출처

- [Claude Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview.md)
- [Claude Agent SDK Python reference](https://code.claude.com/docs/en/agent-sdk/python.md)
- [Claude Cookbooks](https://platform.claude.com/cookbooks)
- [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python)
- [anthropics/claude-agent-sdk-demos](https://github.com/anthropics/claude-agent-sdk-demos)
