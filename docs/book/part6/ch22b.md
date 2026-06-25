# 22b장: 플러그인 시스템 - 패키징에서 마켓플레이스 확장 엔지니어링까지

이 페이지는 한국어 SDK 책의 `22b장: 플러그인 시스템 - 패키징에서 마켓플레이스 확장 엔지니어링까지`을 공개 Python cookbook과 공식 Agent SDK 문서에 맞춰 다시 쓴 공개판이다. 원래 장의 문제의식은 유지하되, 내부 TypeScript 구현명이나 비공개 기능을 그대로 옮기지 않는다. 대신 실행 가능한 notebook, Python 파일, README, 공식 문서를 근거로 사용한다.

**분류:** 제6부: 고급 서브시스템<br>
**공개 상태:** `public`<br>
**근거 신뢰도:** `medium`<br>
**원문 위치:** `docs/book-sdk-ko/src/part6/ch22b.md`

## 이 장의 공개판 요지

이 장은 공개 SDK와 cookbook 예제로 대부분 직접 설명할 수 있다.

플러그인은 공개판에서 skills, agents, hooks, MCP servers를 묶어 배포하는 확장 단위로 설명한다. cookbook에는 완전한 plugin marketplace 구현은 없지만 skills, managed agent skill files, MCP examples가 구성 요소를 보여준다. 따라서 이 장은 plugin 내부 registry를 단정하기보다 공개 plugin docs를 기준으로 패키징 체크리스트를 제공한다.

[Slack managed agent skill](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/managed_agents/slack/skill.md)를 근거로 삼는다. [Linear managed agent skill](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/managed_agents/linear/skill.md)를 근거로 삼는다.

!!! evidence "주요 cookbook 근거"
    - [Slack managed agent skill](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/managed_agents/slack/skill.md)
    - [Linear managed agent skill](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/managed_agents/linear/skill.md)
    - [CMA MCP skill](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/managed_agents/cma-mcp/skill.md)
    - [Custom skill development](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/skills/notebooks/03_skills_custom_development.ipynb)

!!! evidence "공식 문서 근거"
    - [Plugins in the SDK](https://code.claude.com/docs/en/agent-sdk/plugins.md)
    - [Create plugins](https://code.claude.com/docs/en/plugins.md)
    - [Plugins reference](https://code.claude.com/docs/en/plugins-reference.md)

## 원문 절 구조를 공개 SDK로 다시 읽기

### 22b.1 핵심 질문

이 절은 `플러그인 시스템 - 패키징에서 마켓플레이스 확장 엔지니어링까지`의 질문을 공개 SDK에서 관측 가능한 사건으로 좁힌다. 답은 내부 구현명이 아니라 `ClaudeAgentOptions`, message stream, tool call, session record, cookbook 실행 결과에서 찾아야 한다.

### 22b.2 플러그인이 담는 것

이 절은 skills, agents, hooks, MCP를 묶어 배포하는 확장 단위로 설명한다. 내부 marketplace 로직은 공개판의 대상이 아니다.

### 22b.3 관측 기준

이 절은 원문의 `22b.3 관측 기준` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 플러그인은 공개판에서 skills, agents, hooks, MCP servers를 묶어 배포하는 확장 단위로 설명한다. cookbook에는 완전한 plugin marketplace 구현은 없지만 skills, managed agent skill files, MCP examples가 구성 요소를 보여준... 이며, 먼저 `Slack managed agent skill`를 기준 예제로 읽는다.

### 22b.4 학생용 배포 관점

이 절은 원문의 `22b.4 학생용 배포 관점` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 플러그인은 공개판에서 skills, agents, hooks, MCP servers를 묶어 배포하는 확장 단위로 설명한다. cookbook에는 완전한 plugin marketplace 구현은 없지만 skills, managed agent skill files, MCP examples가 구성 요소를 보여준... 이며, 먼저 `Slack managed agent skill`를 기준 예제로 읽는다.

### 22b.5 강사용 관측 관점

이 절은 원문의 `22b.5 강사용 관측 관점` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 플러그인은 공개판에서 skills, agents, hooks, MCP servers를 묶어 배포하는 확장 단위로 설명한다. cookbook에는 완전한 plugin marketplace 구현은 없지만 skills, managed agent skill files, MCP examples가 구성 요소를 보여준... 이며, 먼저 `Slack managed agent skill`를 기준 예제로 읽는다.

### 22b.6 플러그인 repo 최소 구조

이 절은 skills, agents, hooks, MCP를 묶어 배포하는 확장 단위로 설명한다. 내부 marketplace 로직은 공개판의 대상이 아니다.

### 22b.7 학생 실습

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

- 마켓플레이스 내부 추천/랭킹 로직은 다루지 않는다.
- 공개 plugin schema와 cookbook 구성 요소만 연결한다.

## 실습 방향

- skill, hook, MCP server를 하나의 plugin manifest로 묶는 설계 초안을 작성한다.

## Builder takeaway

이 장의 공개판 목표는 원문을 얕게 요약하는 것이 아니다. 책의 논지를 유지하되, 독자가 직접 열어볼 수 있는 Python cookbook과 공식 문서에 묶어 두는 것이다. 따라서 장을 읽은 뒤에는 적어도 하나의 notebook 또는 Python 파일에서 같은 개념을 확인할 수 있어야 한다. 확인할 수 없는 내부 세부는 주장으로 남기지 않고, 공개 경계나 추론으로 분리한다.
