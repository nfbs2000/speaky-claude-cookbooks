# 공개 투영 개요

이 투영판은 오프라인 한국어 책의 장 구조를 유지하되, 각 장의 설명을 공개 Agent SDK와 cookbook 예제에 맞춰 다시 작성합니다.

## 왜 다시 매핑하는가

책은 TypeScript 기반 내부 구조와 공개 SDK에서 직접 보이지 않는 제어면을 교육용으로 다룹니다. 반면 이 포크는 대부분 Python 노트북과 실행 가능한 예제입니다. 그래서 장 제목을 그대로 복사하면 실제 공개 사용자가 확인할 수 없는 설명이 섞입니다.

이 사이트는 다음 질문에 답하도록 재구성합니다.

> 이 장의 아이디어는 공개 SDK에서 어떤 옵션, 메시지, 도구 호출, 세션 기록, cookbook 예제로 확인할 수 있는가?

## 상태 분류

- <span class="projection-status status-public">public</span> 공개 SDK와 cookbook 예제로 직접 설명할 수 있습니다.
- <span class="projection-status status-rewrite">public-rewrite</span> 원래 장의 내부 표현을 공개 API 용어로 바꿔야 합니다.
- <span class="projection-status status-partial">partial</span> 일부는 공개 예제로 설명되지만 내부 세부는 제외합니다.
- <span class="projection-status status-omit">omit</span> 공개 사이트에는 원문을 옮기지 않고 경계 설명만 둡니다.

## 기준 출처

공식 Agent SDK 문서는 agent loop, sessions, tools, hooks, permissions, MCP, subagents, skills, plugins, hosting, OpenTelemetry를 공개 문서로 제공합니다. 이 저장소는 그 표면을 Python 노트북과 실제 agent 파일로 보여줍니다.

따라서 장별 페이지는 매번 다음 네 가지를 함께 둡니다.

- 공개 SDK에서 보이는 개념
- 이 포크의 cookbook/README/Python 파일
- 공식 문서 링크
- 공개하지 않거나 재서술해야 하는 경계
