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
