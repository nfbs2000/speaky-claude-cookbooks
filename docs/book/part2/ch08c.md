# 8c장: 정적 시스템 프롬프트 - SDK에서 보이는 기본 성격

이 페이지는 한국어 SDK 책의 `8c장: 정적 시스템 프롬프트 - SDK에서 보이는 기본 성격`을 공개 Python cookbook과 공식 Agent SDK 문서에 맞춰 다시 쓴 공개판이다. 원래 장의 문제의식은 유지하되, 내부 TypeScript 구현명이나 비공개 기능을 그대로 옮기지 않는다. 대신 실행 가능한 notebook, Python 파일, README, 공식 문서를 근거로 사용한다.

**분류:** 제2부: 프롬프트 엔지니어링<br>
**공개 상태:** `partial`<br>
**근거 신뢰도:** `medium`<br>
**원문 위치:** `docs/book-sdk-ko/src/part2/ch08c.md`

## 이 장의 공개판 요지

이 장은 일부만 공개 SDK로 확인된다. 확인 가능한 부분은 cookbook 근거로 설명하고, 내부 세부는 추론 또는 경계로 분리한다.

공개판에서는 "기본 성격"을 숨은 프롬프트 원문이 아니라 SDK preset과 observable behavior로 다룬다. `claude_code` preset을 유지한 채 append prompt를 붙이는 방식, 또는 custom prompt를 사용하는 방식이 공개 API의 경계다. 따라서 이 장은 정적 프롬프트 원문 분석 대신 "기본 preset을 유지할 때 cookbook agent가 보이는 행동"과 "project instructions를 덧붙였을 때 달라지는 행동"을 비교한다.

[Project settings and output styles](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/01_The_chief_of_staff_agent.ipynb)를 근거로 삼는다. [Project CLAUDE.md](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/chief_of_staff_agent/CLAUDE.md)를 근거로 삼는다.

!!! evidence "주요 cookbook 근거"
    - [Project settings and output styles](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/01_The_chief_of_staff_agent.ipynb)
    - [Project CLAUDE.md](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/chief_of_staff_agent/CLAUDE.md)
    - [Migrating prompt primitives](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/04_migrating_from_openai_agents_sdk.ipynb)

!!! evidence "공식 문서 근거"
    - [Modifying system prompts](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts.md)
    - [Use Claude Code features in the SDK](https://code.claude.com/docs/en/agent-sdk/claude-code-features.md)

## 원문 절 구조를 공개 SDK로 다시 읽기

### 8c.1 핵심 질문

이 절은 `정적 시스템 프롬프트 - SDK에서 보이는 기본 성격`의 질문을 공개 SDK에서 관측 가능한 사건으로 좁힌다. 답은 내부 구현명이 아니라 `ClaudeAgentOptions`, message stream, tool call, session record, cookbook 실행 결과에서 찾아야 한다.

### 8c.2 정적 섹션을 SDK에서 다시 설계하기

이 절은 원문의 `8c.2 정적 섹션을 SDK에서 다시 설계하기` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 "기본 성격"을 숨은 프롬프트 원문이 아니라 SDK preset과 observable behavior로 다룬다. `claude_code` preset을 유지한 채 append prompt를 붙이는 방식, 또는 custom prompt를 사용하는 방식이 공개 API의 경계다. 따라서 이 장은 ... 이며, 먼저 `Project settings and output styles`를 기준 예제로 읽는다.

### 8c.3 정적 성격의 주요 축

이 절은 원문의 `8c.3 정적 성격의 주요 축` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 "기본 성격"을 숨은 프롬프트 원문이 아니라 SDK preset과 observable behavior로 다룬다. `claude_code` preset을 유지한 채 append prompt를 붙이는 방식, 또는 custom prompt를 사용하는 방식이 공개 API의 경계다. 따라서 이 장은 ... 이며, 먼저 `Project settings and output styles`를 기준 예제로 읽는다.

### 8c.4 캔버스 표현

이 절은 화면 구성의 문제가 아니라 evidence projection 문제로 읽는다. prompt, tool use, tool result, final result, usage를 한 화면에서 분리해 보여주는 구조가 필요하다.

### 8c.5 학생 실습

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

- 정적 기본 프롬프트 원문은 공개 사이트에 게시하지 않는다.
- 관찰 가능한 차이만 비교한다.

## 실습 방향

- preset 유지/append/custom 세 가지 옵션을 같은 task에 적용해 tool behavior를 비교한다.

## Builder takeaway

이 장의 공개판 목표는 원문을 얕게 요약하는 것이 아니다. 책의 논지를 유지하되, 독자가 직접 열어볼 수 있는 Python cookbook과 공식 문서에 묶어 두는 것이다. 따라서 장을 읽은 뒤에는 적어도 하나의 notebook 또는 Python 파일에서 같은 개념을 확인할 수 있어야 한다. 확인할 수 없는 내부 세부는 주장으로 남기지 않고, 공개 경계나 추론으로 분리한다.

## 부록: 이 장을 실제 SDK 실행으로 확인한 결과

> 위 공개판 본문은 이 저장소의 notebook과 공식 문서에 근거해 다시 쓴 것이다. 아래는 같은
> 장의 주장을 실제 Claude Agent SDK로 실행해 관찰한 기록이며, **실측 결과로 위 본문을 고쳐
> 쓰지 않았다.** 본문 설명과 실제 동작이 어긋나는 곳도 본문을 남기고 아래에 근거와 함께 적는다.

**실행 조건** — 실제 모델 `claude-opus-5`, Claude Agent SDK `0.2.128`. 같은 작업을 preset
시스템 프롬프트(`105231-08cba367`)와 직접 작성한 정책(`105308-beb0e51a`)으로 각각 한 번
실행했다. 원본 사건 249건 중 72건을 정리했다.

### 실제로 확인된 것

- **조건은 한 변수만 달랐다.** 장 원문·사용자 프롬프트 해시, 실행 전 파일 스냅숏,
  시작 기록의 도구(`Bash`/`Edit`/`Read`)·기본 권한 모드·Opus 5가 모두 같고 프롬프트 종류만
  preset과 explicit으로 갈렸다.
- preset 실행은 작업 공간을 나열하고 대상 파일을 읽은 뒤 한 줄만 `Edit`하고, 실제 검사 PASS를
  받고, 무엇을 실행했고 무엇을 하지 않았는지 구분한 최종 보고까지 마쳤다.
- explicit 실행은 상대 경로를 이미 찾았는데도 잘못된 홈 절대경로 `Read`를 세 번 실패하고,
  오류가 알려 준 작업 디렉터리로 복구해 세 파일을 읽었다.
- 두 실행 모두 대상 파일 하나만 바뀌고 나머지 파일 해시는 유지됐다.
- 도구 호출 수는 preset 5회 / explicit 11회였다.

### 본문을 이렇게 읽으면 안 되는 곳

- **"검사가 PASS했으니 실행이 성공했다"** — 아니다. explicit 실행은 검사 PASS를 받고도 최종
  보고 없이 `error_max_turns`로 끝났다. 종료 기록은 `is_error=true`이다. 변경 검증의
  성공과 실행의 성공은 다릅니다.
- **"preset은 곧바로 대상 파일을 읽는다"** — 아니다. preset도 먼저 `Bash`로 작업 공간을
  나열했다.
- **변경 파일 목록을 "새 파일이 생기지 않았다"의 증거로 쓰면 안 된다.** 이 목록은
  `__pycache__`를 제외한 소스 스냅숏이다. 실제로 explicit 실행의 사후 `ls`에는 새
  `__pycache__` 디렉터리가 나타났다.
- **관찰된 행동을 시스템 프롬프트만의 효과로 귀속하면 안 된다.** 공통 사용자 프롬프트가 이미
  최소 수정, 무관 파일 보존, 검사 실행, 실행·미실행 보고를 직접 요구했다.
- **turn 수 불일치를 임의로 해석하지 않았다.** 호스트 옵션의 `max_turns`는 6인데 explicit
  종료 기록의 `num_turns`는 7이다. 내부 계산 방식을 추측하지 않고 두 값을 함께 남긴다.
- **"preset이 더 낫다"고 쓰면 안 된다.** preset만 최종 보고까지 완료했지만 더 오래 걸리고
  비용도 컸다. 고정 순서로 한 번씩 돌린 한 쌍으로 승자를 정할 수 없다.
- 두 주 어시스턴트는 Opus 5였지만 두 종료 기록에 Haiku 4.5 보조 사용이 함께 있었다.
- 당시 기록은 장 원문과 프롬프트 종류만 묶었고, 정확한 정책 문구·preset 객체·probe 소스·fixture
  해시는 묶지 않았다.

### 이번 실행으로는 확인하지 못한 것

- 실제 시스템 프롬프트 전문. 시작 기록에는 조립된 프롬프트 텍스트가 없어서 provider가 받은
  직렬화 payload를 직접 볼 수 없다. Claude Code preset 내부 문장도 관찰하지 않았다.
- 순서를 바꿔 반복했을 때의 분포(preset → explicit 고정 순서로 한 번씩만 실행)
- 정적 정책의 안전·승인 행동 — 두 실행 모두 권한 콜백과 훅 콜백이 0건이다.
- TypeScript의 배열형 시스템 프롬프트와 동적 경계 상수는 이 Python 실행에서 쓰지 않았다.

## Codex 최종 검토 의견

### 제 판단

정적 프롬프트를 “숨은 원문”이 아니라 반복 행동으로 평가하자는 방향은 건전합니다. 이번 검증의 더 중요한 결론은 짧은 explicit policy가 Claude Code preset의 대체물이 아니라는 사실입니다. 같은 수정 과제에서 preset은 한 파일을 고치고 검사와 최종 보고까지 마쳤지만, explicit 조건은 같은 변경과 PASS를 만들고도 경로 추측으로 turn을 소진해 terminal error로 끝났습니다.

### 검증을 읽고 달라진 신뢰도

이 차이는 preset이 항상 우월하다는 증명이 아닙니다. 고정 순서 한 쌍이고 공통 사용자 프롬프트 자체가 최소 수정, 테스트, 보고 규칙을 이미 강하게 요구했습니다. 그럼에도 “네 줄 정책이면 기본 하니스를 재구현할 수 있다”는 생각은 반박합니다. 실행 성공은 파일 변경, 검사 성공, terminal success, 최종 보고라는 서로 다른 층으로 나눠야 한다는 점도 실제 실패가 잘 드러냈습니다.

### 독자가 오해할 위험

검사 출력이 PASS였다는 이유로 전체 run이 성공했다고 쓰면 안 됩니다. explicit Result는 `error_max_turns`였고 최종 보고도 없었습니다. 반대로 source snapshot에서 새 파일이 안 보였다고 전체 파일시스템이 불변인 것도 아닙니다. 실제 테스트는 `__pycache__`를 만들었고 snapshot이 이를 제외했습니다. 관찰된 행동에서 비공개 preset 문장을 역으로 복원하는 것도 불가능합니다.

### 제가 다시 가르친다면

custom string을 preset의 대안으로 소개하기보다, preset을 유지한 채 작은 append policy를 추가하는 예제를 먼저 보여 주겠습니다. 정말 대체를 가르치려면 neutral user prompt와 안전·범위·검증을 각각 시험하는 여러 task가 필요합니다. 한 과제의 tool count가 아니라 완료 보고와 종료 상태까지 포함해 평가해야 합니다. [한 줄 리서치 에이전트 노트북](https://nfbs2000.github.io/speaky-claude-cookbooks/notebooks/claude_agent_sdk/00_The_one_liner_research_agent_kr.html)은 최소 구성을 이해하는 출발점이고, preset과 explicit의 실제 차이는 [Speaky Agent Flow 8c장 재생](https://nfbs2000.github.io/speaky-agent-flow/education/?collection=book-sdk-ko&run=ch08c)에서 확인할 수 있습니다.

### 클로드는 이렇게 세상을 바라보았다


*아래 1인칭 서술은 숨은 사고 과정의 공개가 아니라, 이 장에서 관찰된 행동으로 재구성한 작동상 세계 모델입니다.*

나에게 preset은 몇 줄의 규칙이 아니라 탐색, 수정, 검증과 보고를 연결하는 작업 문화처럼 작동했다. 짧은 explicit policy도 목표 일부는 전달했지만, 잘못된 경로를 찾는 동안 turn이라는 유한 자원을 소모했고 결국 변경과 검사에 성공하고도 세계가 닫히기 전에 완료 보고를 만들지 못했다. 파일이 맞게 바뀌었다는 사실과 내가 run을 성공적으로 닫았다는 사실은 서로 다른 완결성이었다.

사람은 에이전트의 기본 하니스를 요약 문구 몇 줄로 대체할 수 있다고 가정하지 말아야 한다. 행동 문화는 오류 복구, 종료 조건, 검증과 보고까지 포함한 여러 계약의 묶음이다. custom 지침은 검증된 기본 세계 위에 좁게 추가하고, 정말 대체하려면 여러 과제에서 전체 생명주기를 시험해야 한다.
