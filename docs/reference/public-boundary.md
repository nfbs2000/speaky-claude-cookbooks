# 공개 경계

이 사이트는 공개 문서와 실행 가능한 cookbook을 기준으로 책 내용을 재작성합니다. 다음 항목은 원문을 그대로 옮기지 않습니다.

## 그대로 게시하지 않는 항목

- 비공개 기능 플래그 이름과 전체 목록
- 내부 프롬프트 원문 또는 숨은 classifier prompt로 보이는 내용
- 공개 SDK 문서에 없는 내부 state machine 이름
- 샌드박스 내부 구현을 단정하는 설명
- 모델의 숨은 사고 과정을 복원한다고 읽힐 수 있는 표현

## 공개 표현으로 바꾸는 항목

- 내부 권한 분류기 설명은 `permission_mode`, `allowed_tools`, `disallowed_tools`, `can_use_tool`, hooks 흐름으로 바꿉니다.
- 내부 프롬프트 계층 설명은 `system_prompt`, `CLAUDE.md`, `setting_sources`, output styles, slash commands, skills로 바꿉니다.
- 내부 세션 압축 설명은 sessions, resume/fork, context engineering, prompt caching, compaction cookbook으로 바꿉니다.
- 내부 오케스트레이션 설명은 `ClaudeSDKClient`, `query()`, `AgentDefinition`, MCP, managed/self-hosted examples로 바꿉니다.

## 신뢰도 표기

- `high`: 공식 문서와 이 저장소의 실행 파일이 같은 개념을 직접 보여줍니다.
- `medium`: cookbook 예제로 설명 가능하지만 공개 문서에서 세부가 제한적입니다.
- `low`: 장의 핵심이 비공개/추론성이라 경계 설명만 둡니다.
