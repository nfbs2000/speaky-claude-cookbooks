# 8e장: 도구 설명 프롬프트 - Bash, Read, Grep, Agent는 어떻게 행동을 유도하나

이 페이지는 한국어 SDK 책의 `8e장: 도구 설명 프롬프트 - Bash, Read, Grep, Agent는 어떻게 행동을 유도하나`을 공개 Python cookbook과 공식 Agent SDK 문서에 맞춰 다시 쓴 공개판이다. 원래 장의 문제의식은 유지하되, 내부 TypeScript 구현명이나 비공개 기능을 그대로 옮기지 않는다. 대신 실행 가능한 notebook, Python 파일, README, 공식 문서를 근거로 사용한다.

**분류:** 제2부: 프롬프트 엔지니어링<br>
**공개 상태:** `public-rewrite`<br>
**근거 신뢰도:** `medium`<br>
**원문 위치:** `docs/book-sdk-ko/src/part2/ch08e.md`

## 이 장의 공개판 요지

이 장은 원문의 내부 구현 표현을 공개 SDK 옵션, 메시지, 도구, 세션, notebook 실행 증거로 바꿔 읽어야 한다.

공개판에서는 built-in tool의 내부 설명을 복원하지 않고, tool affordance와 permission consequences를 중심으로 설명한다. Read/Grep/Glob는 관측 도구, Bash/Edit/Write는 변경 도구, Agent/subagents는 위임 경계, MCP tools는 외부 시스템 경계로 분류한다. cookbook의 vulnerability detection agent는 Read/Grep/Glob만 허용해 read-only 분석을 수행하고, SRE agent는 MCP write tools와 safety hooks를 함께 보여준다. 이것이 도구 설명을 행동 정책으로 읽는 공개 근거다.

[Read-only vulnerability detection agent](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/06_The_vulnerability_detection_agent.ipynb)를 근거로 삼는다. [SRE read-write agent](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/03_The_site_reliability_agent.ipynb)를 근거로 삼는다.

!!! evidence "주요 cookbook 근거"
    - [Read-only vulnerability detection agent](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/06_The_vulnerability_detection_agent.ipynb)
    - [SRE read-write agent](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/03_The_site_reliability_agent.ipynb)
    - [Orchestrator workers](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/patterns/agents/orchestrator_workers.ipynb)

!!! evidence "공식 문서 근거"
    - [Tools reference](https://code.claude.com/docs/en/tools-reference.md)
    - [Subagents in the SDK](https://code.claude.com/docs/en/agent-sdk/subagents.md)
    - [Configure permissions](https://code.claude.com/docs/en/agent-sdk/permissions.md)

## 원문 절 구조를 공개 SDK로 다시 읽기

### 8e.1 핵심 질문

이 절은 `도구 설명 프롬프트 - Bash, Read, Grep, Agent는 어떻게 행동을 유도하나`의 질문을 공개 SDK에서 관측 가능한 사건으로 좁힌다. 답은 내부 구현명이 아니라 `ClaudeAgentOptions`, message stream, tool call, session record, cookbook 실행 결과에서 찾아야 한다.

### 8e.2 Bash는 운영 정책 문서다

이 절은 원문의 `8e.2 Bash는 운영 정책 문서다` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 built-in tool의 내부 설명을 복원하지 않고, tool affordance와 permission consequences를 중심으로 설명한다. Read/Grep/Glob는 관측 도구, Bash/Edit/Write는 변경 도구, Agent/subagents는 위임 경계, MCP tool... 이며, 먼저 `Read-only vulnerability detection agent`를 기준 예제로 읽는다.

### 8e.3 Read는 “필요한 만큼 읽기” 습관을 만든다

이 절은 원문의 `8e.3 Read는 “필요한 만큼 읽기” 습관을 만든다` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 built-in tool의 내부 설명을 복원하지 않고, tool affordance와 permission consequences를 중심으로 설명한다. Read/Grep/Glob는 관측 도구, Bash/Edit/Write는 변경 도구, Agent/subagents는 위임 경계, MCP tool... 이며, 먼저 `Read-only vulnerability detection agent`를 기준 예제로 읽는다.

### 8e.4 Grep은 단어 게임의 핵심 장치다

이 절은 원문의 `8e.4 Grep은 단어 게임의 핵심 장치다` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 built-in tool의 내부 설명을 복원하지 않고, tool affordance와 permission consequences를 중심으로 설명한다. Read/Grep/Glob는 관측 도구, Bash/Edit/Write는 변경 도구, Agent/subagents는 위임 경계, MCP tool... 이며, 먼저 `Read-only vulnerability detection agent`를 기준 예제로 읽는다.

### 8e.5 Agent 설명은 위임 정책이다

이 절은 원문의 `8e.5 Agent 설명은 위임 정책이다` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 built-in tool의 내부 설명을 복원하지 않고, tool affordance와 permission consequences를 중심으로 설명한다. Read/Grep/Glob는 관측 도구, Bash/Edit/Write는 변경 도구, Agent/subagents는 위임 경계, MCP tool... 이며, 먼저 `Read-only vulnerability detection agent`를 기준 예제로 읽는다.

### 8e.6 ToolSearch와 deferred schema

이 절은 built-in tools, custom tools, MCP tools, tool result schema의 문제로 재작성한다. 도구는 모델의 능력이 아니라 외부 세계와 만나는 계약이다.

### 8e.7 커스텀 도구 설명 테스트

이 절은 built-in tools, custom tools, MCP tools, tool result schema의 문제로 재작성한다. 도구는 모델의 능력이 아니라 외부 세계와 만나는 계약이다.

### 8e.8 학생 실습

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

- Bash, Read, Grep, Agent의 숨은 prompt 원문은 다루지 않는다.
- 도구별 행동 유도는 공개 tool category와 실행 결과로 설명한다.

## 실습 방향

- Read/Grep/Glob만 허용한 task와 Bash까지 허용한 task의 행동 차이를 비교한다.

## Builder takeaway

이 장의 공개판 목표는 원문을 얕게 요약하는 것이 아니다. 책의 논지를 유지하되, 독자가 직접 열어볼 수 있는 Python cookbook과 공식 문서에 묶어 두는 것이다. 따라서 장을 읽은 뒤에는 적어도 하나의 notebook 또는 Python 파일에서 같은 개념을 확인할 수 있어야 한다. 확인할 수 없는 내부 세부는 주장으로 남기지 않고, 공개 경계나 추론으로 분리한다.
