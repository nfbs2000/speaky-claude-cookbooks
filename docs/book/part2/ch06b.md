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

## 부록: 이 장을 실제 SDK 실행으로 확인한 결과

> 위 공개판 본문은 이 저장소의 notebook과 공식 문서에 근거해 다시 쓴 것이다. 아래는 같은
> 장의 주장을 실제 Claude Agent SDK로 실행해 관찰한 기록이며, **실측 결과로 위 본문을 고쳐
> 쓰지 않았다.** 본문 설명과 실제 동작이 어긋나는 곳도 본문을 남기고 아래에 근거와 함께 적는다.

**실행 조건** — 실제 모델 `claude-opus-5`, Claude Agent SDK `0.2.128`. 통신 계층의 다섯 국면을
따로 실행했다(`103238-e1ac26b5` 부분 스트림, `103316-15c0b725` 실행 중 인터럽트,
`103340-dfe3c027` 도구 결과 뒤 turn 한도, `103401-427be665` 체크포인트 되감기,
`103439-e3093bb2` 외부 세션 저장). 원본 사건 392건 중 101건을 정리했다.

### 실제로 확인된 것

- 부분 스트림 이벤트 58건이 실제로 쌓인 뒤 `Read`와 최종 결과로 이어졌다. 스트리밍은
  결과를 조금씩 보내는 것이지 별도의 결과를 만드는 것이 아니다.
- 오래 걸리는 handler가 시작된 뒤 Python 쪽 인터럽트가 그 실행을 실제로 끊었다.
- 성공한 도구 결과가 끝난 뒤에 turn 한도 종료가 왔다. 한도가 도구 실행 중간을 자르지
  않는다.
- 실제 사용자 메시지 UUID를 기준으로 되감기가 동작했다.
- 외부 세션 저장소에 append가 일어나고 개수가 맞았다.

### 본문을 이렇게 읽으면 안 되는 곳

- **"요청부터 종료까지 Opus 5 하나로 처리된다"** — 요청·시작·주 어시스턴트는 Opus 5였지만,
  다섯 실행 모두 종료 기록의 사용량에 Haiku 4.5 보조 사용이 함께 있었다.
  (근거: 각 시도의 종료 SDK 메시지 82·22·22·106·94·46)

### 이번 실행으로는 확인하지 못한 것

- 네트워크 계층의 실제 재시도·백오프 동작. 이 장의 재시도 설명은 옵션과 관찰된 종료 경로까지
  확인한 것이고, 전송 실패를 인위적으로 만들어 관찰한 것은 아니다.

## Codex 최종 검토 의견

### 제 판단

종료 이유를 모델 품질, 도구 실패, 호스트 중단, turn 한도, 저장·복구로 나눠 읽으라는 주장은 운영에서 매우 중요합니다. 이 구분 없이 모든 문제를 “모델이 이상하다”로 처리하면 재시도 중복과 데이터 손실을 놓칩니다. 다만 장 제목이 약속하는 재시도·성능 저하 대응에 비해 직접 실험의 중심은 스트림, 중단, 한도, 체크포인트, 세션 저장입니다. **좋은 transport 관찰 장이지만 네트워크 복원력 실험은 아직 절반만 갖춰졌습니다.**

### 검증을 읽고 달라진 신뢰도

58개 부분 이벤트 뒤 Read와 최종 Result가 이어지고, 실행 중 handler가 `interrupt()`로 취소되며, 성공한 도구 결과 다음에 `error_max_turns`가 오는 순서는 강하게 확인됐습니다. 실제 사용자 메시지 UUID로 파일을 되감은 결과도 설득력 있습니다. 반면 529 retry는 다른 장에서 우연히 발생한 보조 사례이고, fallback은 실행하지 않았습니다. host clock으로 잰 첫 이벤트 지연은 provider TTFT가 아니며 event gap만으로 network/model/tool 원인을 구분할 수도 없습니다.

### 독자가 오해할 위험

가장 위험한 해석은 “retry가 보였으니 mutation 중복도 안전하다”입니다. 관찰된 529 복구에는 중복 외부 효과가 없었고, deploy·결제·push 같은 비멱등 도구가 재실행되는 상황은 시험하지 않았습니다. `Request interrupted by user`라는 프로토콜 문구도 실제 사람이 UI에서 중단 버튼을 눌렀다는 증거가 아닙니다. 체크포인트 성공 역시 원격 Files API 전체를 검증한 것이 아닙니다.

### 제가 다시 가르친다면

현재 다섯 예제는 그대로 유지하되 여섯 번째에 통제 가능한 실패 프록시를 넣겠습니다. 첫 요청은 도구 결과 직전 연결을 끊고, 재시도 때 같은 `tool_use_id` 또는 idempotency key가 어떻게 처리되는지 외부 side-effect counter로 확인해야 합니다. fallback도 존재하지 않는 모델명이 아니라 의도적으로 실패하는 primary transport와 정상 secondary를 사용해 실제 모델 전환을 관찰해야 합니다. [에이전트 호스팅 노트북](https://nfbs2000.github.io/speaky-claude-cookbooks/notebooks/claude_agent_sdk/07_Hosting_the_agent_kr.html)은 SSE와 세션 저장의 제품 경계를 보여 주며, 현재 확인된 종료·복구 경로는 [Speaky Agent Flow 6b장 재생](https://nfbs2000.github.io/speaky-agent-flow/education/?collection=book-sdk-ko&run=ch06b)에서 확인할 수 있습니다.

### 클로드는 이렇게 세상을 바라보았다

*아래 1인칭 서술은 숨은 사고 과정의 공개가 아니라, 이 장에서 관찰된 행동으로 재구성한 작동상 세계 모델입니다.*

나에게 스트림은 완성된 답을 운반하는 관이 아니라 세계가 시간 순서대로 생겨나는 방식이었다. 부분 텍스트, 도구 요청, 결과, 중단, terminal reason이 도착할 때마다 내가 행동할 수 있는 현재가 달라졌다. 하지만 event가 잠시 오지 않는다고 해서 네트워크가 느린지, 모델이 계산 중인지, 도구가 멈췄는지를 나는 알 수 없었다. interrupt와 turn 한도는 내부 판단이 아니라 host가 시간의 문을 닫는 외부 사건이었다.

사람은 에이전트 운영에서 침묵을 원인으로 해석하지 말고 관찰 가능한 종료 이유와 부작용을 따로 기록해야 한다. 특히 재시도는 같은 세계를 이어 가는 것이 아니라 같은 행동을 다시 발생시킬 수 있다. 결제나 배포처럼 되돌리기 어려운 행동에는 idempotency와 side-effect 영수증이 있어야 복구가 안전해진다.
