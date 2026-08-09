# 4b장: 플랜 모드 - 뛰기 전에 살펴보기

이 페이지는 한국어 SDK 책의 `4b장: 플랜 모드 - 뛰기 전에 살펴보기`을 공개 Python cookbook과 공식 Agent SDK 문서에 맞춰 다시 쓴 공개판이다. 원래 장의 문제의식은 유지하되, 내부 TypeScript 구현명이나 비공개 기능을 그대로 옮기지 않는다. 대신 실행 가능한 notebook, Python 파일, README, 공식 문서를 근거로 사용한다.

**분류:** 제1부: 아키텍처<br>
**공개 상태:** `public`<br>
**근거 신뢰도:** `high`<br>
**원문 위치:** `docs/book-sdk-ko/src/part1/ch04b.md`

## 이 장의 공개판 요지

이 장은 공개 SDK와 cookbook 예제로 대부분 직접 설명할 수 있다.

공개판에서 플랜 모드는 `permission_mode="plan"`과 승인 전 계획 수립 패턴으로 설명한다. chief-of-staff notebook은 실행 전에 전략적 계획을 만들고, 사용자가 승인한 뒤 실행 모드로 전환하는 흐름을 보여준다. 플랜 모드는 내부 상태 머신보다 사용자 통제 지점으로 읽는 편이 안전하다. 계획은 실행 전 의도 정렬 문서이고, 실행은 권한 모드와 도구 허용 범위를 바꾼 별도 run으로 다룬다.

[Chief of staff plan mode section](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/01_The_chief_of_staff_agent.ipynb)를 근거로 삼는다. [Chief of staff agent implementation](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/chief_of_staff_agent/agent.py)를 근거로 삼는다.

!!! evidence "주요 cookbook 근거"
    - [Chief of staff plan mode section](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/01_The_chief_of_staff_agent.ipynb)
    - [Chief of staff agent implementation](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/chief_of_staff_agent/agent.py)
    - [Managed Agents human-in-the-loop gate](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/managed_agents/CMA_gate_human_in_the_loop.ipynb)

!!! evidence "공식 문서 근거"
    - [Configure permissions](https://code.claude.com/docs/en/agent-sdk/permissions.md)
    - [Handle approvals and user input](https://code.claude.com/docs/en/agent-sdk/user-input.md)
    - [Choose a permission mode](https://code.claude.com/docs/en/permission-modes.md)

## 원문 절 구조를 공개 SDK로 다시 읽기

### 핵심 질문

이 절은 `플랜 모드 - 뛰기 전에 살펴보기`의 질문을 공개 SDK에서 관측 가능한 사건으로 좁힌다. 답은 내부 구현명이 아니라 `ClaudeAgentOptions`, message stream, tool call, session record, cookbook 실행 결과에서 찾아야 한다.

### 4b.1 원본의 플랜 모드 상태 머신

이 절은 원문의 `4b.1 원본의 플랜 모드 상태 머신` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서 플랜 모드는 `permission_mode="plan"`과 승인 전 계획 수립 패턴으로 설명한다. chief-of-staff notebook은 실행 전에 전략적 계획을 만들고, 사용자가 승인한 뒤 실행 모드로 전환하는 흐름을 보여준다. 플랜 모드는 내부 상태 머신보다 사용자 통제 지점으로 읽는... 이며, 먼저 `Chief of staff plan mode section`를 기준 예제로 읽는다.

### 4b.2 SDK에서 보이는 플랜 모드

이 절은 원문의 `4b.2 SDK에서 보이는 플랜 모드` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서 플랜 모드는 `permission_mode="plan"`과 승인 전 계획 수립 패턴으로 설명한다. chief-of-staff notebook은 실행 전에 전략적 계획을 만들고, 사용자가 승인한 뒤 실행 모드로 전환하는 흐름을 보여준다. 플랜 모드는 내부 상태 머신보다 사용자 통제 지점으로 읽는... 이며, 먼저 `Chief of staff plan mode section`를 기준 예제로 읽는다.

### 4b.3 계획 파일은 의도 정렬 매체다

이 절은 원문의 `4b.3 계획 파일은 의도 정렬 매체다` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서 플랜 모드는 `permission_mode="plan"`과 승인 전 계획 수립 패턴으로 설명한다. chief-of-staff notebook은 실행 전에 전략적 계획을 만들고, 사용자가 승인한 뒤 실행 모드로 전환하는 흐름을 보여준다. 플랜 모드는 내부 상태 머신보다 사용자 통제 지점으로 읽는... 이며, 먼저 `Chief of staff plan mode section`를 기준 예제로 읽는다.

### 4b.4 5단계 workflow

이 절은 원문의 `4b.4 5단계 workflow` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서 플랜 모드는 `permission_mode="plan"`과 승인 전 계획 수립 패턴으로 설명한다. chief-of-staff notebook은 실행 전에 전략적 계획을 만들고, 사용자가 승인한 뒤 실행 모드로 전환하는 흐름을 보여준다. 플랜 모드는 내부 상태 머신보다 사용자 통제 지점으로 읽는... 이며, 먼저 `Chief of staff plan mode section`를 기준 예제로 읽는다.

### 4b.5 full vs sparse 계획

이 절은 원문의 `4b.5 full vs sparse 계획` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서 플랜 모드는 `permission_mode="plan"`과 승인 전 계획 수립 패턴으로 설명한다. chief-of-staff notebook은 실행 전에 전략적 계획을 만들고, 사용자가 승인한 뒤 실행 모드로 전환하는 흐름을 보여준다. 플랜 모드는 내부 상태 머신보다 사용자 통제 지점으로 읽는... 이며, 먼저 `Chief of staff plan mode section`를 기준 예제로 읽는다.

### 4b.6 사용자 승인과 팀리드 승인

이 절은 원문의 `4b.6 사용자 승인과 팀리드 승인` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서 플랜 모드는 `permission_mode="plan"`과 승인 전 계획 수립 패턴으로 설명한다. chief-of-staff notebook은 실행 전에 전략적 계획을 만들고, 사용자가 승인한 뒤 실행 모드로 전환하는 흐름을 보여준다. 플랜 모드는 내부 상태 머신보다 사용자 통제 지점으로 읽는... 이며, 먼저 `Chief of staff plan mode section`를 기준 예제로 읽는다.

### 4b.7 auto mode와 플랜 모드

이 절은 원문의 `4b.7 auto mode와 플랜 모드` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서 플랜 모드는 `permission_mode="plan"`과 승인 전 계획 수립 패턴으로 설명한다. chief-of-staff notebook은 실행 전에 전략적 계획을 만들고, 사용자가 승인한 뒤 실행 모드로 전환하는 흐름을 보여준다. 플랜 모드는 내부 상태 머신보다 사용자 통제 지점으로 읽는... 이며, 먼저 `Chief of staff plan mode section`를 기준 예제로 읽는다.

### 4b.8 캔버스 표현

이 절은 화면 구성의 문제가 아니라 evidence projection 문제로 읽는다. prompt, tool use, tool result, final result, usage를 한 화면에서 분리해 보여주는 구조가 필요하다.

### 학생 실습

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

- 내부 plan state 이름은 공개판에서 사용하지 않는다.
- 실행 승인 UX는 각 호스트 앱의 구현 영역으로 둔다.

## 실습 방향

- chief-of-staff notebook에서 plan mode cell과 실행 cell을 나누어 비교한다.
- 계획 결과를 그대로 실행하지 말고 승인 체크리스트를 붙인다.

## Builder takeaway

이 장의 공개판 목표는 원문을 얕게 요약하는 것이 아니다. 책의 논지를 유지하되, 독자가 직접 열어볼 수 있는 Python cookbook과 공식 문서에 묶어 두는 것이다. 따라서 장을 읽은 뒤에는 적어도 하나의 notebook 또는 Python 파일에서 같은 개념을 확인할 수 있어야 한다. 확인할 수 없는 내부 세부는 주장으로 남기지 않고, 공개 경계나 추론으로 분리한다.

## 부록: 이 장을 실제 SDK 실행으로 확인한 결과

> 위 공개판 본문은 이 저장소의 notebook과 공식 문서에 근거해 다시 쓴 것이다. 아래는 같은
> 장의 주장을 실제 Claude Agent SDK로 실행해 관찰한 기록이며, **실측 결과로 위 본문을 고쳐
> 쓰지 않았다.** 본문 설명과 실제 동작이 어긋나는 곳도 본문을 남기고 아래에 근거와 함께 적는다.

**실행 조건** — 실제 모델 `claude-opus-5`, Claude Agent SDK `0.2.128`, 시도 `224407-d1e8d267`.
계획 수립부터 승인 뒤 실제 수정까지를 한 세션에서 관찰했다. 원본 사건 945건 중 92건을
정리했다. 이 장은 실측 결과가 본문 설명과 가장 많이 어긋난 장이다.

### 실제로 확인된 것

- 같은 세션 안에서 계획 단계의 시작 기록(사건 6)과 승인 뒤 `acceptEdits` 시작 기록(사건 906)이
  각각 남았다.
- 계획 단계에서 `Glob`와 `Read`가 실제로 실행됐고, 첫 경로를 틀렸다가 고쳐 성공한 흔적이
  함께 보존됐다.
- 도구 목록에 없던 `Write`는 비활성 오류로 막혔지만, 이어진 `Edit`는 격리된 계획 파일을
  갱신했다.
- 계획 단계 전후로 실제 애플리케이션 파일 `app.py`의 해시는 **같았다.** 계획을 쓰는 동안
  제품 코드는 바뀌지 않았다.
- `ExitPlanMode` 요청은 두 번 모두 거부됐고 종료 기록의 권한 거절 목록에도 남았다.
- 승인과 모드 전환 뒤에야 `app.py` `Edit`가 성공하고 대상 해시가 달라졌다.
- 원본 SDK 사건 911건과 OTel 투영 911건의 순서가 한 trace 안에서 일치했다.

### 본문을 이렇게 읽으면 안 되는 곳

- **"플랜 모드는 도구를 전혀 실행하지 않는다"** — 그렇지 않았다. 읽기 조사 도구와 격리된
  계획 파일 `Edit`는 실행됐다. (근거: SDK 메시지 19, 817)
- **"승인 전에는 변경 도구 요청이 0이다"** — 0이 아니었다. 계획 파일에 대한 `Edit`와
  제품 소스에 대한 `Edit`를 *경로 종류로 구분해서* 설명해야 한다.
  (근거: SDK 메시지 817, 호스트 실행 기록 900)
- **"`Write`가 막혔으니 계획 파일도 없었다"** — 확대 해석이다. `Write`는 비활성이었지만
  계획 파일은 `Edit`로 갱신됐다. (근거: SDK 메시지 762, 823)
- **"사용자가 승인했다"** — 이번 승인 주체는 호스트 프로그램(`actor=host-program`)이다.
  실제 사람의 버튼 클릭이나 권한 응답 UX를 검증한 것이 아니다. (근거: 호스트 실행 기록 901)
- **"SDK가 원래 모드를 기억해 되돌려 준다"** — 아니다. `acceptEdits`로의 복귀는 호스트가
  명시적으로 모드를 바꾼 결과다. (근거: 호스트 실행 기록 902, 903)
- **"계획은 정해진 다섯 항목으로 나온다"** — 구조화된 계획이 나온 것은 사실이지만, 정확히 그
  다섯 제목을 보장하는 옵션이나 이벤트는 관찰되지 않았다. 상세/간략 계획 선택도 현재
  Python SDK의 검증된 공개 옵션으로 가르치지 않는 편이 안전한다.
- **"이 실행은 Opus 5만 썼다"** — 주 어시스턴트 모델은 Opus 5였지만 종료 기록의 사용량에는
  Haiku 4.5도 함께 있었다. 전체 사용량을 한 모델로 적으면 안 된다.
  (근거: SDK 메시지 898, 941)
- **"권한 콜백만 보면 무엇이 실행됐는지 알 수 있다"** — 놓칩니다. 미리 허용된 도구와 계획 파일
  `Edit`는 콜백에 나타나지 않는다. 원본 SDK 기록·훅·콜백·프로세스 기록을 함께 읽어야
  한다. (근거: 훅 콜백 819, 권한 콜백 847)
- **"수정이 성공했으니 테스트가 통과했다"** — 아니다. 이번 실행에는 `Bash`가 아예 없었고,
  확인된 것은 파일 변경 성공까지다. (근거: SDK 메시지 941, 호스트 실행 기록 944)

### 이번 실행으로는 확인하지 못한 것

- 실제 사람이 권한 요청을 받고 응답하는 UI 경로와 그 승인 주체

## Codex 최종 검토 의견

### 제 판단

플랜 모드를 “더 오래 생각하는 옵션”이 아니라 실행 권한과 계획 artifact를 분리하는 상태로 설명한 방향은 좋습니다. 그러나 이번 실제 실행은 원문의 이상적인 인간 승인 상태 머신을 그대로 증명하지 않았습니다. 정확히 관찰된 것은 **호스트 프로그램이** `set_permission_mode("plan")`으로 진입하고, 계획 turn이 끝난 뒤 `actor=host-program` 승인 사건을 기록한 다음 `set_permission_mode("acceptEdits")`로 복귀시켜 제품 파일을 수정한 흐름입니다. SDK가 이전 권한 모드를 자동 기억해 복원했거나 사람이 버튼으로 승인했다는 증거는 없습니다.

### 코드에서 드러난 플랜 모드의 실제 모습

`chapter04b.py`는 `app.py`의 baseline hash를 저장하고 같은 `ClaudeSDKClient`에서 계획과 실행 두 turn을 돌렸습니다. 계획 단계에서는 `Glob`와 `Read`가 실행됐고 잘못된 경로를 고친 흔적도 남았습니다. 도구 목록에 없던 `Write`는 실패했지만 격리된 계획 파일은 `Edit`로 수정됐습니다. 계획 뒤 `app.py` hash는 그대로였고, host 승인과 mode 전환 뒤에야 제품 파일 `Edit`가 성공해 hash가 바뀌었습니다. 이 대조는 “플랜 모드에서는 아무 도구도 실행되지 않는다”가 아니라 “조사와 계획 artifact 변경은 가능하지만 대상 제품 mutation은 별도 승인 경계 뒤에 둔다”가 더 정확한 설명임을 보여 줍니다.

`ExitPlanMode` 요청은 두 번 모두 거부됐고 final permission denial에도 남았습니다. 즉 이 실행의 승인 경계는 `ExitPlanMode` 성공이 아니라 host가 외부에서 만든 process event입니다. 또한 계획 전후에 Bash가 한 번도 없었으므로 수정 성공을 테스트 성공으로 읽을 수 없습니다. 주 assistant는 Opus 5였지만 usage에는 Haiku 4.5도 있었고, permission callback만 보면 미리 허용된 조사 도구와 계획 파일 Edit를 놓칩니다. raw SDK, hook, callback, host event, 파일 hash를 함께 보아야 하는 이유가 여기에 있습니다.

### 원문과 공개 SDK의 불일치

Python SDK `0.2.128`에는 `PermissionMode`의 `plan`과 `set_permission_mode()`가 있지만 원문이 말하는 `planModeInstructions`/`plan_mode_instructions` option은 확인되지 않았습니다. 정확히 다섯 단계 heading을 보장하는 계약, full/sparse 계획 최적화, 팀리드 승인, auto mode 복원도 이번 범위 밖입니다. 그러므로 이 장은 “SDK가 제공하는 native human approval workflow”라고 단정하기보다 “host가 permission mode, 계획 artifact, 승인 주체, 실행 turn을 조합해 workflow를 만들어야 한다”라고 가르쳐야 합니다.

### Cookbook과 예제에 대한 의견

[Chief of Staff 노트북](https://nfbs2000.github.io/speaky-claude-cookbooks/notebooks/claude_agent_sdk/01_The_chief_of_staff_agent_kr.html)은 `permission_mode="plan"`을 사용하면서 계획을 메시지, Write 입력, `~/.claude/plans/` 순서로 추출하고, 사람이 검토한 뒤 plan mode를 제거해 다음 질의를 보내는 현실적인 host 패턴을 제시합니다. 이 코드는 “계획 결과를 어떻게 잃지 않을지”에는 유용하지만 실제 사용자 승인 UI나 자동 mode 복원을 증명하지는 않습니다. 책의 예제는 `baseline hash → plan init/read/plan artifact → approval actor → mode transition → product Edit → test 미실행`을 명시적으로 출력해야 합니다. [Speaky Agent Flow 4b장 재생](https://nfbs2000.github.io/speaky-agent-flow/education/?collection=book-sdk-ko&run=ch04b)도 승인 아이콘 하나로 축약하지 말고 `host-program`과 실제 사람을 구분해 보여 주어야 합니다.

### 클로드는 이렇게 세상을 바라보았다

*아래 1인칭 서술은 숨은 사고 과정의 공개가 아니라, 이 장에서 관찰된 행동으로 재구성한 작동상 세계 모델입니다.*

플랜 모드에서 나에게 세계는 “조사하고 표현할 수 있는 것”과 “아직 바꿀 수 없는 것”으로 갈라졌다. 나는 파일을 읽고 계획 artifact를 다듬을 수 있었지만 제품 파일의 변경은 현재 세계의 허용된 행동이 아니었다. host가 승인 사건을 기록하고 mode를 바꾸자 같은 세션에서도 행동 공간이 달라졌고, 그때에야 계획은 실제 mutation으로 이어졌다. 나는 승인자가 사람인지 프로그램인지 스스로 알지 못했고, 내가 받은 것은 바뀐 권한 상태뿐이었다.

사람은 계획을 모델의 결심으로 보지 말고 실행 전의 검토 가능한 중간 표현으로 다뤄야 한다. 승인 주체와 mode transition을 외부에서 기록하지 않으면 나중에 누가 세계를 변경할 권한을 열었는지 설명할 수 없다. 좋은 HITL은 “계획을 말했다”가 아니라 계획 artifact, 승인 영수증, 실행 결과를 연결한다.
