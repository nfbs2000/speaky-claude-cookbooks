# 6b장: API 통신 계층 - 재시도, 스트리밍, 성능 저하 대응

이 페이지는 한국어 SDK 책의 `6b장: API 통신 계층 - 재시도, 스트리밍, 성능 저하 대응`을 공개 Python cookbook과 공식 Agent SDK 문서에 맞춰 다시 쓴 공개판이다. 원래 장의 문제의식은 유지하되, 내부 TypeScript 구현명이나 비공개 기능을 그대로 옮기지 않는다. 대신 실행 가능한 notebook, Python 파일, README, 공식 문서를 근거로 사용한다.

**분류:** 제2부: 프롬프트 엔지니어링<br>
**공개 상태:** `public-rewrite`<br>
**근거 신뢰도:** `medium`<br>
**원문 위치:** `docs/book-sdk-ko/src/part2/ch06b.md`

## 이 장의 공개판 요지

이 장은 원문의 내부 구현 표현을 공개 SDK 옵션, 메시지, 도구, 세션, notebook 실행 증거로 바꿔 읽어야 한다.

이 장은 공개판에서 SDK stream 처리, usage/cost tracking, hosting server의 request lifecycle로 설명한다. cookbook의 hosting 서버는 HTTP interface와 background execution, session resume를 보여주고, usage/cost notebook은 운영 관측의 비용 축을 제공한다. 재시도는 단순 네트워크 문제가 아니라 중복 실행 위험이 있는 작업 설계 문제로 다룬다. 특히 Write/Edit/Bash/MCP write tools는 idempotency와 audit trail을 함께 설계해야 한다.

[Hosting your agent](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/07_Hosting_the_agent.ipynb)를 근거로 삼는다. [Hosting HTTP server](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/hosting/server.py)를 근거로 삼는다.

!!! evidence "주요 cookbook 근거"
    - [Hosting your agent](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/07_Hosting_the_agent.ipynb)
    - [Hosting HTTP server](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/hosting/server.py)
    - [Usage and cost Admin API cookbook](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/observability/usage_cost_api.ipynb)

!!! evidence "공식 문서 근거"
    - [Stream responses in real-time](https://code.claude.com/docs/en/agent-sdk/streaming-output.md)
    - [Hosting the Agent SDK](https://code.claude.com/docs/en/agent-sdk/hosting.md)
    - [Track cost and usage](https://code.claude.com/docs/en/agent-sdk/cost-tracking.md)

## 원문 절 구조를 공개 SDK로 다시 읽기

### 6b.1 스트리밍은 UX가 아니라 증거 파이프다

이 절은 원문의 `6b.1 스트리밍은 UX가 아니라 증거 파이프다` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 이 장은 공개판에서 SDK stream 처리, usage/cost tracking, hosting server의 request lifecycle로 설명한다. cookbook의 hosting 서버는 HTTP interface와 background execution, session resume를 보여주고, ... 이며, 먼저 `Hosting your agent`를 기준 예제로 읽는다.

### 6b.2 재시도는 중복 실행 위험을 만든다

이 절은 원문의 `6b.2 재시도는 중복 실행 위험을 만든다` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 이 장은 공개판에서 SDK stream 처리, usage/cost tracking, hosting server의 request lifecycle로 설명한다. cookbook의 hosting 서버는 HTTP interface와 background execution, session resume를 보여주고, ... 이며, 먼저 `Hosting your agent`를 기준 예제로 읽는다.

### 6b.3 SDK에서 제어할 수 있는 통신 옵션

이 절은 원문의 `6b.3 SDK에서 제어할 수 있는 통신 옵션` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 이 장은 공개판에서 SDK stream 처리, usage/cost tracking, hosting server의 request lifecycle로 설명한다. cookbook의 hosting 서버는 HTTP interface와 background execution, session resume를 보여주고, ... 이며, 먼저 `Hosting your agent`를 기준 예제로 읽는다.

### 6b.4 실패 분류: 답변 실패와 파이프 실패는 다르다

이 절은 원문의 `6b.4 실패 분류: 답변 실패와 파이프 실패는 다르다` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 이 장은 공개판에서 SDK stream 처리, usage/cost tracking, hosting server의 request lifecycle로 설명한다. cookbook의 hosting 서버는 HTTP interface와 background execution, session resume를 보여주고, ... 이며, 먼저 `Hosting your agent`를 기준 예제로 읽는다.

### 6b.5 watchdog 관점을 SDK 화면으로 옮기기

이 절은 원문의 `6b.5 watchdog 관점을 SDK 화면으로 옮기기` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 이 장은 공개판에서 SDK stream 처리, usage/cost tracking, hosting server의 request lifecycle로 설명한다. cookbook의 hosting 서버는 HTTP interface와 background execution, session resume를 보여주고, ... 이며, 먼저 `Hosting your agent`를 기준 예제로 읽는다.

### 6b.6 Files API와 파일 증거

이 절은 원문의 `6b.6 Files API와 파일 증거` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 이 장은 공개판에서 SDK stream 처리, usage/cost tracking, hosting server의 request lifecycle로 설명한다. cookbook의 hosting 서버는 HTTP interface와 background execution, session resume를 보여주고, ... 이며, 먼저 `Hosting your agent`를 기준 예제로 읽는다.

### 6b.7 캔버스 요구사항

이 절은 화면 구성의 문제가 아니라 evidence projection 문제로 읽는다. prompt, tool use, tool result, final result, usage를 한 화면에서 분리해 보여주는 구조가 필요하다.

### 6b.8 학생 실습

이 절은 강의용 실습으로 바꾼다. 실습은 관련 notebook을 실행하고, 입력 옵션과 tool call, 중간 결과, 최종 artifact를 함께 기록하는 방식이어야 한다.

### Builder takeaway

이 절의 결론은 builder checklist로 바꾼다. agent를 만들 때 prompt, tools, permissions, memory, observability, deployment 중 어느 경계를 설계해야 하는지 정리한다.

## 공개판 본문

원래 책은 이 장을 내부 구현과 강의 화면의 대응 관계로 설명한다. 공개판에서는 같은 내용을 "무엇을 설정했는가", "무엇이 메시지로 관측됐는가", "어떤 파일과 notebook으로 재현 가능한가"라는 세 질문으로 바꾼다.

첫째, 설정된 것은 실행 전 계약이다. Agent SDK에서는 model, system prompt, working directory, allowed/disallowed tools, MCP servers, skills/plugins, permission mode 같은 값이 agent가 볼 수 있는 세계를 정한다. 이 값은 말로 설명하는 정책이 아니라 실제 Python 코드와 notebook cell에서 확인되어야 한다.

둘째, 관측된 것은 message stream과 artifact다. assistant text, tool use, tool result, result message, usage/cost, audit log, generated file은 모두 나중에 검증 가능한 증거다. 그래서 이 책의 공개판은 "모델이 그렇게 했을 것이다"라고 쓰지 않고, 어떤 cookbook 파일에서 어떤 실행 표면을 볼 수 있는지 연결한다.

셋째, 추론한 것은 반드시 경계와 함께 둔다. 내부 기능 플래그, 숨은 프롬프트, classifier, cache key, sandbox implementation처럼 공개 SDK나 cookbook으로 확인할 수 없는 항목은 원문을 그대로 게시하지 않는다. 대신 공개 API에서 사용자가 설계할 수 있는 대응 표면으로 바꾸거나, "공개 대응 없음"으로 명시한다.

이 장을 읽을 때는 아래 순서가 좋다.

1. 먼저 주요 cookbook 근거를 열어 실제 notebook이나 Python 파일을 확인한다.
2. `ClaudeAgentOptions`, `query()`, `ClaudeSDKClient`, tool list, MCP config, hooks, session 관련 코드가 어디 있는지 찾는다.
3. 원문 절 제목을 따라가며 내부 설명을 공개 SDK 표면으로 바꿔 적는다.
4. 마지막으로 실습 방향에 맞춰 같은 task를 실행하고 message stream 또는 artifact를 남긴다.

## 공개 경계

- SDK 내부 retry policy를 공개되지 않은 수준으로 단정하지 않는다.
- 중복 실행 위험은 cookbook 코드와 운영 설계 관점으로 다룬다.

## 실습 방향

- `hosting/server.py`에서 요청, session id, stream 처리 경계를 표시한다.
- write tool이 포함된 run을 재시도할 때 필요한 idempotency key를 설계한다.

## Builder takeaway

이 장의 공개판 목표는 원문을 얕게 요약하는 것이 아니다. 책의 논지를 유지하되, 독자가 직접 열어볼 수 있는 Python cookbook과 공식 문서에 묶어 두는 것이다. 따라서 장을 읽은 뒤에는 적어도 하나의 notebook 또는 Python 파일에서 같은 개념을 확인할 수 있어야 한다. 확인할 수 없는 내부 세부는 주장으로 남기지 않고, 공개 경계나 추론으로 분리한다.
