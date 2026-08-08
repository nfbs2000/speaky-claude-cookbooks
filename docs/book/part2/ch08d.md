# 8d장: 동적 프롬프트 레이어 - 세션, 메모리, 팀, MCP가 뒤에 붙는 법

이 페이지는 한국어 SDK 책의 `8d장: 동적 프롬프트 레이어 - 세션, 메모리, 팀, MCP가 뒤에 붙는 법`을 공개 Python cookbook과 공식 Agent SDK 문서에 맞춰 다시 쓴 공개판이다. 원래 장의 문제의식은 유지하되, 내부 TypeScript 구현명이나 비공개 기능을 그대로 옮기지 않는다. 대신 실행 가능한 notebook, Python 파일, README, 공식 문서를 근거로 사용한다.

**분류:** 제2부: 프롬프트 엔지니어링<br>
**공개 상태:** `public-rewrite`<br>
**근거 신뢰도:** `high`<br>
**원문 위치:** `docs/book-sdk-ko/src/part2/ch08d.md`

## 이 장의 공개판 요지

이 장은 원문의 내부 구현 표현을 공개 SDK 옵션, 메시지, 도구, 세션, notebook 실행 증거로 바꿔 읽어야 한다.

동적 레이어는 공개판에서 세션 resume, `CLAUDE.md`, skills, subagents, MCP server registration, plugins로 재분류한다. cookbook의 session browser와 observability agent는 세션과 MCP가 실제 run에 붙는 방식을 보여준다. 핵심은 prompt가 하나의 문자열이 아니라 실행 직전에 조합되는 환경이라는 점이다. 공개 SDK에서는 그 조합을 `ClaudeAgentOptions`, working directory, setting sources, mcp servers, agents/plugins 옵션으로 관찰한다.

[Session browser](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/05_Building_a_session_browser.ipynb)를 근거로 삼는다. [Observability agent with MCP](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/02_The_observability_agent.ipynb)를 근거로 삼는다.

!!! evidence "주요 cookbook 근거"
    - [Session browser](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/05_Building_a_session_browser.ipynb)
    - [Observability agent with MCP](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/02_The_observability_agent.ipynb)
    - [Custom Skills](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/skills/notebooks/03_skills_custom_development.ipynb)

!!! evidence "공식 문서 근거"
    - [Use Claude Code features in the SDK](https://code.claude.com/docs/en/agent-sdk/claude-code-features.md)
    - [Connect to external tools with MCP](https://code.claude.com/docs/en/agent-sdk/mcp.md)
    - [Work with sessions](https://code.claude.com/docs/en/agent-sdk/sessions.md)

## 원문 절 구조를 공개 SDK로 다시 읽기

### 8d.1 핵심 질문

이 절은 `동적 프롬프트 레이어 - 세션, 메모리, 팀, MCP가 뒤에 붙는 법`의 질문을 공개 SDK에서 관측 가능한 사건으로 좁힌다. 답은 내부 구현명이 아니라 `ClaudeAgentOptions`, message stream, tool call, session record, cookbook 실행 결과에서 찾아야 한다.

### 8d.2 동적 레이어 목록

이 절은 원문의 `8d.2 동적 레이어 목록` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 동적 레이어는 공개판에서 세션 resume, `CLAUDE.md`, skills, subagents, MCP server registration, plugins로 재분류한다. cookbook의 session browser와 observability agent는 세션과 MCP가 실제 run에 붙는 방식을 ... 이며, 먼저 `Session browser`를 기준 예제로 읽는다.

### 8d.3 `Options.systemPrompt`와 `SYSTEM_PROMPT_DYNAMIC_BOUNDARY`

이 절은 원문의 `8d.3 `Options.systemPrompt`와 `SYSTEM_PROMPT_DYNAMIC_BOUNDARY`` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 동적 레이어는 공개판에서 세션 resume, `CLAUDE.md`, skills, subagents, MCP server registration, plugins로 재분류한다. cookbook의 session browser와 observability agent는 세션과 MCP가 실제 run에 붙는 방식을 ... 이며, 먼저 `Session browser`를 기준 예제로 읽는다.

### 8d.4 `CLAUDE.md`와 설정 로딩

이 절은 원문의 `8d.4 `CLAUDE.md`와 설정 로딩` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 동적 레이어는 공개판에서 세션 resume, `CLAUDE.md`, skills, subagents, MCP server registration, plugins로 재분류한다. cookbook의 session browser와 observability agent는 세션과 MCP가 실제 run에 붙는 방식을 ... 이며, 먼저 `Session browser`를 기준 예제로 읽는다.

### 8d.5 스킬/플러그인/MCP는 동적 능력 표면이다

이 절은 외부 시스템을 agent runtime에 연결하는 공개 tool boundary로 읽는다. MCP server는 모델 내부 능력이 아니라 별도 권한과 오류 경계를 가진 실행 표면이다.

### 8d.6 캔버스 표현

이 절은 화면 구성의 문제가 아니라 evidence projection 문제로 읽는다. prompt, tool use, tool result, final result, usage를 한 화면에서 분리해 보여주는 구조가 필요하다.

### 8d.7 학생 실습

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

- 내부 dynamic boundary token은 사용하지 않는다.
- 동적 prompt layer는 공개 설정 파일과 SDK options로만 설명한다.

## 실습 방향

- MCP server를 켠 run과 끈 run의 tool namespace 차이를 기록한다.
- session resume이 prompt context에 주는 효과를 `05` notebook으로 확인한다.

## Builder takeaway

이 장의 공개판 목표는 원문을 얕게 요약하는 것이 아니다. 책의 논지를 유지하되, 독자가 직접 열어볼 수 있는 Python cookbook과 공식 문서에 묶어 두는 것이다. 따라서 장을 읽은 뒤에는 적어도 하나의 notebook 또는 Python 파일에서 같은 개념을 확인할 수 있어야 한다. 확인할 수 없는 내부 세부는 주장으로 남기지 않고, 공개 경계나 추론으로 분리한다.

## 부록: 이 장을 실제 SDK 실행으로 확인한 결과

> 위 공개판 본문은 이 저장소의 notebook과 공식 문서에 근거해 다시 쓴 것이다. 아래는 같은
> 장의 주장을 실제 Claude Agent SDK로 실행해 관찰한 기록이며, **실측 결과로 위 본문을 고쳐
> 쓰지 않았다.** 본문 설명과 실제 동작이 어긋나는 곳도 본문을 남기고 아래에 근거와 함께 적는다.

**실행 조건** — 실제 모델 `claude-opus-5`, Claude Agent SDK `0.2.128`. 세 조건을 따로
실행했다(`105511-0c4575df` 프로젝트 지침 적용, `105549-8fc27cde` 설정 격리,
`105633-ee1cdfa1` 스킬과 MCP). 원본 사건 105건 중 39건을 정리했다.

### 실제로 확인된 것

- **프로젝트 지침은 실제로 주입된다.** 도구를 하나도 주지 않은 상태에서, 모델이 사용자
  프롬프트에는 없는 `CLAUDE.md`의 무작위 표식을 정확히 되돌려 주고 성공으로 끝났다.
- **설정을 격리하면 그 표식이 사라진다.** `setting_sources=[]`로 둔 실행에서는 표식이 원본
  기록 어디에도 나타나지 않았고 최종 보고는 `MISSING`이었다.
- 스킬과 MCP 실행의 시작 기록에는 준비한 스킬, 연결된 서버, MCP 도구가 함께 나타났다.
- MCP 도구 호출(사건 16) → 호스트 실행(17) → 표식이 담긴 도구 결과(19) → 최종 답변이
  하나의 사슬로 이어졌다.
- 세 실행의 무결성 기록에 적힌 모든 증거 파일 해시가 현재 파일과 일치했다.

### 본문을 이렇게 읽으면 안 되는 곳

이 장에서 가장 중요한 교훈은 **모델이 문장으로 만들어 낸 "검사 결과"를 실제 검사로 착각하면
안 된다**는 것이다.

- **가짜 `Bash` 기록** — 격리 실행의 한 응답에는 `Bash` 호출과 `ls` 출력처럼 보이는 내용이
  있었다. 그런데 그 실행의 도구 수는 0이고, 타입이 있는 도구 호출/결과도, 호스트 실행
  사건도 없다. **그것은 그냥 텍스트였다.** (근거: `105549-8fc27cde` 사건 28)
- 같은 실행의 최종 보고는 "작업 공간이 비었고 `CLAUDE.md`도 없다"고 설명했지만, 파일을 실제로
  만든 것은 호스트 probe였다. 파일시스템 도구 증거도 없다. 모델의 설명이 실제 상태와
  어긋난 사례다.
- **"설정을 격리하면 능력이 모두 사라진다"고 읽으면 안 된다.** `setting_sources=[]`인
  시작 기록에도 기본 스킬 16개와 기본 에이전트 5개가 남아 있었다. 프로젝트 표식이
  빠지는 것과 능력이 없어지는 것은 다릅니다.
- **`Skill` 도구가 없다고 스킬이 노출되지 않은 것은 아니다.** 별도 `Skill` 도구는 없었지만
  시작 기록의 스킬 목록에는 준비한 스킬이 들어 있었다. 최종 보고는 이 두 표면을
  혼동했다.
- 스킬 문구의 단독 효과는 증명되지 않았다. 사용자 프롬프트도 스킬 사용을 직접 요구했고
  제공된 도구는 MCP 하나뿐이었다.
- **수집 완료 표식을 합격으로 읽으면 안 된다.** OTel의 `CAPTURED`와 단정 수 0은 "원본을
  빠짐없이 모았다"는 뜻이고, 이 장의 주장이 통과했다는 뜻이 아니다.
- 주 어시스턴트는 Opus 5였지만 종료 기록에 Haiku 4.5 보조 사용이 함께 있었다.

### 이번 실행으로는 확인하지 못한 것

- 훅 이벤트 수집을 켜 두었지만 세 실행의 훅 콜백은 0건이고, 지침 적재나 설정 변경 전용
  사건도 없었다.
- 실제 시스템 프롬프트 전문과 provider 직렬화 payload
- 유효한 로컬 플러그인 패키지와 그 뒤의 명령·에이전트·훅 사건
- 사용자/프로젝트/로컬 설정 조합의 반복 분포, 그리고 동적 레이어와 승인 행동의 관계
  (권한 콜백 0건)

## Codex 최종 검토 의견

이 장의 관찰팩은 해시나 OTel만으로 주장을 참이라고 선언하려는 장치가 아닙니다. 직접 실행 코드가 행동 증거를 만들고, 같은 실행에서 수집된 OTel이 사건 순서와 관계를 보존하며, Speaky가 두 층을 독자가 검토할 수 있는 장면으로 투영합니다. 관찰하지 못한 항목은 이 결합으로도 증명된 것이 아닙니다.

세션 지침, 프로젝트 설정, skill, plugin, MCP를 동적 레이어로 분리한 구조는 공식 Agent SDK의 구성 표면과 일치합니다. 다만 관찰팩의 시작 목록에 이름이 나타나는 것은 사용 가능성일 뿐 실제 사용 증거가 아니므로, 설정·적재·호출·결과를 나눠 봐야 합니다. 예제는 `setting_sources=[]`, `project`, `project+local`을 독립 세션으로 실행하고 각 조건에서 `CLAUDE.md` 표식과 도구 호출을 출력한 뒤 skill·plugin·MCP는 별도 예제로 분리하는 것이 좋습니다. [Chief of Staff 노트북](https://nfbs2000.github.io/speaky-claude-cookbooks/notebooks/claude_agent_sdk/01_The_chief_of_staff_agent_kr.html)이 setting source를 단계적으로 보여 주며, 이 장의 실제 적재·사용 관계는 [Speaky Agent Flow 8d장 재생](https://nfbs2000.github.io/speaky-agent-flow/education/?collection=book-sdk-ko&run=ch08d)에서 확인할 수 있습니다.
