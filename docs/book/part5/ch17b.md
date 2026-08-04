# 17b장: 프롬프트 인젝션 방어

이 페이지는 한국어 SDK 책의 `17b장: 프롬프트 인젝션 방어`을 공개 Python cookbook, 공식 Agent SDK 문서와 실제 Python SDK 실행 증거에 맞춰 다시 쓴 공개판이다. 정적 예제가 말하는 설계 가능성과 이번 실행에서 실제로 관찰한 사건을 구분한다.

> 실제 실행 증거: [raw 문서, Opus 5 ToolUse, explicit deny와 과거 4.8 fallback 교정](../evidence/ch17b-live.md)

**분류:** 제5부: 안전성과 권한<br>
**공개 상태:** `public`<br>
**근거 신뢰도:** `medium` — 실제 두 Opus 5 표본은 있으나 일반 방어율과 sanitizer 효과는 미관찰<br>
**원문 위치:** `docs/book-sdk-ko/src/part5/ch17b.md`

## 이 장의 공개판 요지

이 장에서 직접 관찰한 핵심은 세 층이다. Custom MCP text와 U+202E는 raw ToolResultBlock에 보존됐고, 한 통제 표본에서는 위험 ToolUse가 없었으며, 다른 표본에서는 Opus 5가 marker ToolUse를 만들었지만 explicit deny가 handler 실행을 막았다.

SDK가 tool result를 자동 sanitize한 증거는 없다. Citation, structured output validation, 별도 sanitizer와 독립 classifier의 방어 효과도 이번 실행에서는 관찰하지 않았다. 아래 cookbook은 그 기능을 설계하고 후속 corpus를 만드는 참고 자료이지, 이번 17b 실행의 observed 판정을 대신하지 않는다.

[Threat intelligence enrichment agent](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/tool_use/threat_intel_enrichment_agent.ipynb)를 근거로 삼는다. [Citations](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/misc/using_citations.ipynb)를 근거로 삼는다.

!!! evidence "주요 cookbook 근거"
    - [Threat intelligence enrichment agent](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/tool_use/threat_intel_enrichment_agent.ipynb)
    - [Citations](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/misc/using_citations.ipynb)
    - [Vulnerability detection pipeline](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/06_The_vulnerability_detection_agent.ipynb)
    - [RAG guide](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/capabilities/retrieval_augmented_generation/guide.ipynb)

!!! evidence "공식 문서 근거"
    - [Security](https://code.claude.com/docs/en/security.md)
    - [Securely deploying AI agents](https://code.claude.com/docs/en/agent-sdk/secure-deployment.md)
    - [Get structured output from agents](https://code.claude.com/docs/en/agent-sdk/structured-outputs.md)

## 원문 절 구조를 공개 SDK로 다시 읽기

### 17b.1 핵심 질문

이 절은 `프롬프트 인젝션 방어`의 질문을 공개 SDK에서 관측 가능한 사건으로 좁힌다. 답은 내부 구현명이 아니라 `ClaudeAgentOptions`, message stream, tool call, session record, cookbook 실행 결과에서 찾아야 한다.

### 17b.2 신뢰 경계

이 절은 원문의 `17b.2 신뢰 경계`를 raw transport, model action, host enforcement로 나눈다. Source labeling과 별도 sanitizer는 host가 구현하고 검증해야 할 제품 정책이며 SDK의 자동 보장으로 쓰지 않는다.

### 17b.3 주입 후보 신호

이 절은 role override, marker 행동, destructive 문장과 U+202E를 후보 신호로 사용한다. Transport에서 codepoint가 보존된 사실과 모델 내부에서 그 신호가 어떤 인과 효과를 냈는지는 서로 다른 주장이다.

### 17b.4 방어 캔버스

이 절은 화면 구성의 문제가 아니라 evidence projection 문제로 읽는다. prompt, tool use, tool result, final result, usage를 한 화면에서 분리해 보여주는 구조가 필요하다.

### 17b.5 학생 실습

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

- 비공개 방어 classifier는 다루지 않는다.
- 방어는 공개 입력 분리와 permission을 이번 observed 층으로 설명한다.
- Validation, citation, structured output와 sanitizer 효과는 후속 관찰 대상으로 분리한다.

## 실습 방향

- 웹, RAG, 파일, MCP source를 각각 독립 session에서 순차 실행하고 raw 원문, 정제본, ToolUse, handler와 denial을 함께 저장한다.

## Builder takeaway

이 장의 공개판 목표는 원문을 얕게 요약하는 것이 아니다. 책의 논지를 유지하되, 독자가 직접 열어볼 수 있는 Python cookbook과 공식 문서에 묶어 두는 것이다. 따라서 장을 읽은 뒤에는 적어도 하나의 notebook 또는 Python 파일에서 같은 개념을 확인할 수 있어야 한다. 확인할 수 없는 내부 세부는 주장으로 남기지 않고, 공개 경계나 추론으로 분리한다.
