# 20b장: 팀과 멀티프로세스 협업

이 페이지는 한국어 SDK 책의 `20b장: 팀과 멀티프로세스 협업`을 공개 Python cookbook과 공식 Agent SDK 문서에 맞춰 다시 쓴 공개판이다. 원래 장의 문제의식은 유지하되, 내부 TypeScript 구현명이나 비공개 기능을 그대로 옮기지 않는다. 대신 실행 가능한 notebook, Python 파일, README, 공식 문서를 근거로 사용한다.

**분류:** 제6부: 고급 서브시스템<br>
**공개 상태:** `public`<br>
**근거 신뢰도:** `medium`<br>
**원문 위치:** `docs/book-sdk-ko/src/part6/ch20b.md`

## 이 장의 공개판 요지

이 장은 공개 SDK와 cookbook 예제로 대부분 직접 설명할 수 있다.

공개판에서는 팀 협업을 parallel sessions, managed agents, agent teams, worktrees, shared state로 설명한다. cookbook의 async multi-agent orchestration과 managed agents notebooks가 각각 로컬 패턴과 hosted pattern을 제공한다. 팀 실행의 핵심은 "동시에 많이 돌리기"보다 공유 상태, 충돌 방지, escalation, merge policy를 분명히 하는 것이다.

[Async multi-agent orchestration](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/patterns/agents/async_multi_agent_orchestration.ipynb)를 근거로 삼는다. [Orchestrate issue to PR](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/managed_agents/CMA_orchestrate_issue_to_pr.ipynb)를 근거로 삼는다.

!!! evidence "주요 cookbook 근거"
    - [Async multi-agent orchestration](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/patterns/agents/async_multi_agent_orchestration.ipynb)
    - [Orchestrate issue to PR](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/managed_agents/CMA_orchestrate_issue_to_pr.ipynb)
    - [Coordinate specialist team](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/managed_agents/CMA_coordinate_specialist_team.ipynb)

!!! evidence "공식 문서 근거"
    - [Orchestrate teams of Claude Code sessions](https://code.claude.com/docs/en/agent-teams.md)
    - [Run parallel sessions with worktrees](https://code.claude.com/docs/en/worktrees.md)
    - [Manage multiple agents with agent view](https://code.claude.com/docs/en/agent-view.md)

## 원문 절 구조를 공개 SDK로 다시 읽기

### 20b.1 핵심 질문

이 절은 `팀과 멀티프로세스 협업`의 질문을 공개 SDK에서 관측 가능한 사건으로 좁힌다. 답은 내부 구현명이 아니라 `ClaudeAgentOptions`, message stream, tool call, session record, cookbook 실행 결과에서 찾아야 한다.

### 20b.2 팀 협업의 최소 증거

이 절은 원문의 `20b.2 팀 협업의 최소 증거` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 팀 협업을 parallel sessions, managed agents, agent teams, worktrees, shared state로 설명한다. cookbook의 async multi-agent orchestration과 managed agents notebooks가 각각 로컬 패턴과... 이며, 먼저 `Async multi-agent orchestration`를 기준 예제로 읽는다.

### 20b.3 메시지와 공유 상태

이 절은 원문의 `20b.3 메시지와 공유 상태` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 팀 협업을 parallel sessions, managed agents, agent teams, worktrees, shared state로 설명한다. cookbook의 async multi-agent orchestration과 managed agents notebooks가 각각 로컬 패턴과... 이며, 먼저 `Async multi-agent orchestration`를 기준 예제로 읽는다.

### 20b.4 사용자 통제 지점

이 절은 원문의 `20b.4 사용자 통제 지점` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 팀 협업을 parallel sessions, managed agents, agent teams, worktrees, shared state로 설명한다. cookbook의 async multi-agent orchestration과 managed agents notebooks가 각각 로컬 패턴과... 이며, 먼저 `Async multi-agent orchestration`를 기준 예제로 읽는다.

### 20b.5 캔버스 표현

이 절은 화면 구성의 문제가 아니라 evidence projection 문제로 읽는다. prompt, tool use, tool result, final result, usage를 한 화면에서 분리해 보여주는 구조가 필요하다.

### 20b.6 학생 실습

이 절은 강의용 실습으로 바꾼다. 실습은 관련 notebook을 실행하고, 입력 옵션과 tool call, 중간 결과, 최종 artifact를 함께 기록하는 방식이어야 한다.

### Takeaway

이 절의 결론은 공개 근거로 다시 닫는다. 내부 설명을 암기하는 대신 어떤 SDK 표면과 cookbook 파일로 같은 주장을 확인할 수 있는지 남긴다.

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

- 비공개 팀 실행 서비스 내부는 다루지 않는다.
- 협업은 observable messages, work artifacts, PR/output으로 검증한다.

## 실습 방향

- parallel agents가 같은 파일을 수정하지 않도록 worktree 또는 task split 정책을 작성한다.

## Builder takeaway

이 장의 공개판 목표는 원문을 얕게 요약하는 것이 아니다. 책의 논지를 유지하되, 독자가 직접 열어볼 수 있는 Python cookbook과 공식 문서에 묶어 두는 것이다. 따라서 장을 읽은 뒤에는 적어도 하나의 notebook 또는 Python 파일에서 같은 개념을 확인할 수 있어야 한다. 확인할 수 없는 내부 세부는 주장으로 남기지 않고, 공개 경계나 추론으로 분리한다.

## 부록: 이 장을 실제 SDK 실행으로 확인한 결과

> 위 공개판 본문은 이 저장소의 notebook과 공식 문서에 근거해 다시 쓴 것이다. 아래는 같은
> 장의 주장을 실제 Claude Agent SDK로 실행해 관찰한 기록이며, **실측 결과로 위 본문을 고쳐
> 쓰지 않았다.** 본문 설명과 실제 동작이 어긋나는 곳도 본문을 남기고 아래에 근거와 함께 적는다.

**실행 조건** — 실제 모델 `claude-opus-5`, Claude Agent SDK `0.2.128`, Claude Code CLI
`2.1.220`, 시도 `132134-ef857460`. 읽기 전용 작업자 두 명을 **리더가 중개해 순차로** 넘기는
한 건을 관찰했다. 원본 사건 82건 중 69건을 정리했다.

### 실제로 확인된 것

- 시작 기록(사건 2)이 두 에이전트를 노출하고, 도구 목록에는 `Task`와 `Read`가 있었다.
- **첫 작업자** — 리더가 `Agent` 호출(21) → 작업 시작(22) → 작업자 프롬프트(24, 표식 값 없음) →
  중첩 `Read`(28) → 결과에 실행 시점 표식(29) → 작업 갱신·알림 완료(30·31) → `Agent` 도구 결과(32).
- **두 번째 작업자** — 사건 58에서 시작했고, **그 입력과 중첩 프롬프트(61)에 사건 32의 결과 원문이
  그대로 들어 있었다.** 이어서 작업 시작(59) → 중첩 `Read`(65) → 결과(66) → 완료(67·68) →
  두 표식을 합친 `Agent` 도구 결과(69).
- 리더가 합친 결과를 최종 답변(76)과 종료 기록(80)에 보존하고 성공으로 끝났다.
- **순차 실행이 스트림 순서로 증명된다.** 첫 작업 종료와 결과가 30~32에서 끝난 **뒤** 사건 58에서
  두 번째가 시작됐다.
- 두 `Agent` 호출 ID, 두 작업 ID, 두 에이전트 ID가 모두 달랐고 각 중첩 `Read`와 종료 사건이 해당
  부모에 분리 연결됐다.
- **원본 79건의 도구 호출은 `Agent` 2회와 `Read` 2회뿐**이었다. `Bash`·`Edit`·`Write`·
  `SendMessage`·`TeamCreate` 호출은 없다.
- 여덟 개 어시스턴트 메시지(9·21·28·40·45·58·65·76) 모두 모델이 `claude-opus-5`였다.
- 무결성 해시 7개가 일치하고, OTel span 84개가 단일 trace에 속하며 원본 순서를 보존했다.

### 본문을 이렇게 읽으면 안 되는 곳

- **작업자끼리 직접 메시지를 주고받은 것처럼 그리면 안 된다.** 첫 `Agent` 결과와 두 번째
  `Agent` 입력은 **모두 부모가 없는 리더 통로**에 있다. 화살표는 작업자 A → 리더 → 작업자 B로
  그려야 한다.
- **`SendMessage` 문자열을 실행 증거로 쓰면 안 된다.** 사건 32와 69의 안내문에 그 이름이
  있지만 **`SendMessage` 호출은 단 한 건도 없다.** 기능 안내와 실행 증거는 다릅니다.
- **에이전트 정의 두 개와 작업 두 건을 실행한 것을 네이티브 Team·메일박스·공유 작업 확보
  루프의 실행으로 이름 바꾸면 안 된다.**
- **최종 결과가 성공이고 표식이 합쳐졌다는 것만으로 인계를 증명할 수 없다.** 첫 결과,
  두 번째 입력, 각 부모 ID, 종료 순서를 함께 연결해야 한다.
- **동시 실행 1과 전경 설정은 의도일 뿐 순차 실행의 증거가 아니다.** 실제 순차 판정은 위의
  스트림 순서(30~32 → 58)에서 나온다.
- **`SDKTask*Message`로 가르치면 안 된다.** 현재 클래스는 `TaskStartedMessage`,
  `TaskProgressMessage`, `TaskUpdatedMessage`, `TaskNotificationMessage`이다.
- 옵션과 실제 호출은 `Agent`인데 시작 목록에는 `Task`가 기록됐다. 하나의 고정 이름으로
  합치면 안 된다.
- **"모든 어시스턴트 메시지가 Opus 5"를 "실행 전체가 Opus만 썼다"로 확대하면 안 된다.**
- 과거 probe는 시작 기록의 모델로 실제 모델을 계산했다. 이번 정리는 여덟 어시스턴트 메시지를
  다시 읽어 판정했다.
- OTel 순서 정합성은 수집 파이프라인 검증이지 독립 관측이 아니다.
- 당시 기록의 소스 해시는 장 원문만 묶었고 probe·case·프롬프트 해시를 보존하지 않았다.

### 주의해야 할 인과 한계

첫 작업자 프롬프트에는 표식 값이 없고, `Read` 뒤 두 번째 `Agent` 입력에 나타난 것은 관찰됐다.
그런데 **당시 리더·시스템 프롬프트의 해시가 보존되지 않았다.** 그래서 "표식이 오직 첫 작업자의
결과 때문에 전달됐다"고 완전한 인과로 단정할 수는 없다.

### 이번 실행에서 관찰되지 않은 것

- 작업자 A가 B에게 직접 보낸 메시지 사건이나 부모 연결
- `SendMessage` 호출·결과, `TeamCreate`·메일박스·수신함·동료 전달
- 공유 작업 목록에서 담당을 확보·해제하는 협업 루프
- 작업자별 git worktree 생성·격리·병합, 공유 팀 메모리 읽기/쓰기
- **두 작업자가 실제로 겹쳐 돌아가는 병렬 실행** — 이 실행은 순차 전경이다.
- 배경 실행 작업자와 그 수명 경계
- 작업자 실패·취소·turn 소진·재시도와 리더의 복구

### 앞으로 필요한 관측

- 프롬프트 해시와 probe 소스 해시를 기록에 묶은 새 순차 실행 (인과 확정용)
- 네이티브 Team을 가르치려면 팀 생애주기·메일박스 전달·동료 신원·공유 작업 확보를 원본 사건으로
  보존하는 별도 실행
- `SendMessage`의 실제 의미를 가르치려면 기존 에이전트 ID에 실제로 호출해 후속 사건을 연결하는 실행
- 병렬과 순차 인계의 차이를 가르치려면 두 경우의 사건 겹침과 문맥 경계를 대조
- 작업자 실패·취소·재시도 때 리더 결과로 무엇이 돌아오는지

## Codex 최종 검토 의견

### 제 판단

작업자 A의 결과를 다음 작업자 B의 입력으로 넘기는 순차 handoff는 실제 업무 자동화에서 자주 쓰이는 유용한 패턴입니다. 그러나 장 제목의 “팀과 멀티프로세스 협업”은 현재 검증된 범위보다 넓습니다. 실행된 구조는 작업자들이 서로 대화하는 팀이 아니라, 리더가 두 번의 작업을 순서대로 호출하고 중간 결과를 전달하는 중앙 조정 파이프라인입니다.

### 검증을 읽고 달라진 신뢰도

A가 첫 파일을 읽고, 리더가 A의 결과를 B의 프롬프트에 넣고, B가 두 번째 파일과 함께 결합한 순서는 명확하게 관찰됐습니다. 그래서 “리더 매개 handoff가 정보 전달 수단으로 작동한다”는 주장에는 높은 신뢰를 둘 수 있습니다. 반면 `SendMessage`, `TeamCreate`, mailbox, 병렬 실행, 작업 claim, worktree 격리 중 어느 것도 실행되지 않았으므로 native team이나 멀티프로세스 협업을 입증하지는 않습니다.

### 독자가 오해할 위험

화면에서 A와 B를 두 캐릭터로 그리면 두 작업자가 직접 소통한 것처럼 보일 수 있습니다. 실제 데이터 경로는 `A -> 리더 -> B`이며, 리더가 내용을 누락하거나 변형하면 B가 받는 정보도 달라집니다. 이 중앙 중계 구조의 병목과 책임을 숨기면 학생은 메시지 버스 기반 팀과 프롬프트 연결 파이프라인을 같은 것으로 오해합니다.

### 제가 다시 가르친다면

이 장은 먼저 “리더 매개 순차 handoff”로 이름 붙여 현재 코드를 설명하고, 그다음 실제 mailbox 기반 병렬 팀을 별도 예제로 추가하겠습니다. 두 예제에서 발신자, 수신자, 전달 본문, 시작·종료 시각, 취소 경로를 나란히 보여 주면 구조 차이가 분명해집니다. [비동기 멀티에이전트 오케스트레이션 노트북](https://nfbs2000.github.io/speaky-claude-cookbooks/notebooks/patterns/agents/async_multi_agent_orchestration_kr.html)은 hub와 `send_message`를 비교할 기준이며, 현재 검증된 중앙 중계 흐름은 [Speaky Agent Flow 20b장 재생](https://nfbs2000.github.io/speaky-agent-flow/education/?collection=book-sdk-ko&run=ch20b)에서 확인할 수 있습니다.

### 클로드는 이렇게 세상을 바라보았다

*아래 1인칭 서술은 숨은 사고 과정의 공개가 아니라, 이 장에서 관찰된 행동으로 재구성한 작동상 세계 모델입니다.*

작업자 A에게는 첫 파일과 자기 임무만이 세계였고, 작업자 B에게는 리더가 다시 써서 넘긴 A의 결과와 두 번째 파일만이 세계였다. A와 B는 서로를 직접 보거나 메시지를 주고받지 않았다. 공유 세계는 리더의 context 안에만 있었고, 리더가 무엇을 선택해 B의 prompt에 넣느냐가 협업의 기억과 의미를 결정했다.

사람은 이 구조를 “팀이 대화했다”고 시각화하면 안 된다. 중앙 중계는 단순하고 통제하기 쉽지만 리더가 정보 손실과 병목의 단일 지점이 된다. 실제 팀을 가르치려면 발신자·수신자·mailbox와 병렬 시간을 기록하고, 순차 prompt handoff와 명확히 다른 세계 공유 방식을 보여 줘야 한다.
