# 8e장: 도구 설명 프롬프트 — Bash, Read, Grep, Agent는 어떻게 행동을 유도하나

> 공개 GitHub Pages 투영판: [8e장: 도구 설명 프롬프트 — Bash, Read, Grep, Agent는 어떻게 행동을 유도하나](https://nfbs2000.github.io/speaky-claude-cookbooks/book/part2/ch08e/)

도구 설명은 사실 매뉴얼이라기보다 하나의 프롬프트에 가깝습니다. 모델은 도구 이름, 설명, 입력 schema를 읽으면서 “이 상황에서 이 도구를 써도 될까”, “어떤 입력을 넣어야 할까”, “결과를 어떻게 해석하면 좋을까”를 스스로 정해 나갑니다.

다만 이 문장은 설계 가설입니다. 실제 실행에서 올바른 도구 입력을 보았다는 사실만으로 그
행동의 원인이 내장 도구 설명이었다고 증명할 수는 없습니다. 사용자 prompt가 같은 행동을
직접 지시했는지, 정확한 description이 provider에 전달됐는지, 대조군에서도 같은 결과가
나오는지를 함께 확인해야 합니다.

## 8e.1 핵심 질문

> 도구 설명 문장이 실제 `tool_use.name`, `tool_use.input`, `tool_result` 해석을 어떻게 바꾸는가?

## 8e.2 Bash는 운영 정책 문서다

Bash 설명은 단순히 쉘 명령을 실행한다는 안내에 그치지 않습니다. 실제 하니스에서는 Bash 설명이 다음과 같은 내용을 함께 담고 있습니다.

| 범주 | 예 |
| --- | --- |
| 안전 | 파괴적 git 명령, rm, force push 주의 |
| 작업 방식 | interactive 명령 회피, timeout 고려 |
| 전용 도구 우선 | Read/Grep/Edit/Write가 가능한 일은 Bash로 하지 않기 |
| 검증 | test/build/lint 실행 |
| 권한 | 위험 명령에서 permission request |

SDK에서 Bash 프롬프트의 품질은 `tool_use.input.command`에 자연스럽게 드러납니다.

```text
좋음: Bash("npm test -- --runInBand")
나쁨: Bash("cat file | grep ... | sed -i ...")  // 전용 도구로 나눠야 함
```

## 8e.3 Read는 “필요한 만큼 읽기” 습관을 만든다

Read 설명은 path, offset, limit, 큰 파일, 이미지/PDF 같은 입력 습관을 만들어 줍니다. 좋은 Read 사용은 대체로 다음과 같은 특징을 가집니다.

- 정확한 파일을 읽습니다.
- 필요한 구간만 읽습니다.
- 한 번 읽은 큰 파일을 반복해서 통째로 다시 읽지 않습니다.
- 응답 주장에 읽은 문장을 연결합니다.

캔버스에서는 Read 이벤트를 “문서 카드”로 변환합니다.

```text
Read
  file: ch05.md
  section: SYSTEM_PROMPT_DYNAMIC_BOUNDARY
  extracted sentence: "..."
  linked claim: "정적/동적 경계가 존재한다"
```

## 8e.4 Grep은 단어 게임의 핵심 장치다

Grep 설명은 검색을 표준화해 줍니다. 여기서 정말 중요한 것은 검색이 일어났다는 사실 자체가 아니라, 어떤 단어가 검색됐는가입니다.

| 좋은 검색 | 나쁜 검색 |
| --- | --- |
| `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` | `prompt` |
| `canUseTool` | `permission stuff` |
| `SDKAPIRetryMessage` | `retry`만 반복 |
| `AgentDefinition` | `team`만 반복 |

책 캔버스의 중심은 긴 경로가 아니라 검색 단어, 반환 문장, 그리고 그것에 연결된 주장이 되는 편이 좋습니다.

```text
keyword -> returned sentence -> claim -> answer
```

## 8e.5 Agent 설명은 위임 정책이다

Agent 도구 설명은 단순히 “subagent를 실행한다”에 머무르지 않습니다. 언제 위임할지, 어떤 역할에 위임할지, parent가 중간 결과를 엿보지 말아야 하는지, 결과가 올 때까지 조작하지 말아야 하는지까지 함께 정해 줍니다.

SDK에서는 다음을 통해 관찰할 수 있습니다. 다만 아래 옵션 이름 일부는 TypeScript 표면입니다. 이 책의 Python 0.2.128 실행에서 같은 이름을 관찰했다고 읽으면 안 됩니다.

| 항목 | SDK 표면 |
| --- | --- |
| agent 목록 | `Options.agents` |
| agent prompt | `AgentDefinition.prompt` |
| agent 도구 제한 | `AgentDefinition.tools`, `disallowedTools` |
| agent 실행 | Agent/Task 계열 `tool_use` |
| nested transcript | 공통 관찰 키 `parent_tool_use_id`; TypeScript option `forwardSubagentText` |
| 진행 요약 | TypeScript option `agentProgressSummaries`, task events |

강의에서는 팀 실행을 어렵게 포장하지 않습니다. parent가 어떤 agent를 왜 호출했고, worker가 어떤 도구 권한을 가졌고, 결과가 언제 parent에게 돌아왔는지 차근차근 보여 드립니다.

## 8e.6 ToolSearch와 deferred schema

일부 도구는 처음부터 전체 schema가 모델 컨텍스트에 들어오지는 않습니다. ToolSearch는 필요한 도구를 검색하고 schema를 여는 지연 로딩 전략입니다. 아래 흐름은 아키텍처 설명이며, 이 장의 Python 0.2.128 실제 실험에서는 ToolSearch/deferred schema를 구성하거나 관찰하지 않았습니다.

SDK/제품 관점에서 이 패턴은 꽤 중요합니다.

- 모든 도구 schema를 처음부터 넣으면 컨텍스트가 커집니다.
- 도구가 많아질수록 모델이 고르기가 더 헷갈립니다.
- 필요한 때에 schema를 여는 방식은 비용과 정확도를 함께 관리해 줍니다.

캔버스에는 다음 흐름이 보이면 좋습니다.

```text
Need capability
  -> ToolSearch query
  -> schema loaded
  -> actual tool_use
```

## 8e.7 커스텀 도구 설명 테스트

도구 구현을 테스트하기 전에, 먼저 설명을 테스트해 보면 좋습니다.

```typescript
tool(
  "extract_claims",
  [
    "문서나 답변에서 검증 가능한 주장만 추출한다.",
    "각 주장은 근거 문장, 추론 여부, 불확실성 표시를 가져야 한다.",
    "근거가 없는 해석은 grounded claim으로 표시하지 않는다.",
  ].join("\n"),
  schema,
  handler,
);
```

좋은 테스트는 최종 답변보다 `tool_use.input`을 먼저 살펴봅니다.

| 질문 | 평가 |
| --- | --- |
| schema field를 제대로 채웠는가 | input shape |
| query가 구체적인가 | keyword quality |
| 빈 결과 후 복구했는가 | repeated tool_use diff |
| 결과를 claim에 연결했는가 | graph edge |

## 8e.8 실제 Opus 5 도구 입력 실행

2026-08-03에 Python SDK 0.2.128과 실제 `claude-opus-5`로 세 case를 순차 실행했습니다.
전체 raw 판독표는 [8e장 실제 Python SDK 관찰](../evidence/ch08e-live.md)에
있습니다.

### Read와 Grep

- attempt `105914-4dbec404`: 250줄 fixture에서 prompt가 요청한 170~190줄을
  `Read(offset=170, limit=21)` 한 번으로 읽고 window marker를 반환했습니다. 전체 파일
  Read나 반복 Read는 없었습니다.
- attempt `105957-c4d885c3`: prompt가 지시한 정확한 `SDKAPIRetryMessage`를 `sources/`에서
  Grep한 뒤 matching `types.ts`를 Read해 controlled status field를 보고했습니다. Grep의
  content에는 한 줄 match가 있었지만 부가 metadata의 `numFiles`는 0이었다. content mode의
  이 값을 “검색 결과 없음”으로 해석하면 안 됩니다.

### Bash는 검증에만 사용

attempt `110040-d85664b5`에서 모델은 `subject.py`를 Read로 확인했습니다. 첫 Bash 입력 `python3 verify.py; echo "EXIT: $?"`는 복합 operation의 추가 부분이 승인 범위 밖이라 거부됐습니다. 모델은 같은 명령을 맹목 반복하지 않고 bare `python3 verify.py`로 바꿨고, 실제 tool result `PASS CH08E_BASH_VERIFICATION_...`를 받았습니다.

최종 Result는 stdout PASS는 확인했지만 별도 숫자 exit-code field는 확인하지 않았다고
구분했습니다. 이 사례는 파일 읽기와 실행 검증이 Read/Bash로 분리되고, SDK의 오류
`ToolResult`와 `Result.permission_denials` 뒤 허용된 최소 command로 복구한 사건을 보여
줍니다. 이 실행의 hook callback과 permission callback은 모두 0개이므로 이를 “permission
hook이 거부했다”고 부르면 안 됩니다.

세 case의 host snapshot은 `.git`과 `__pycache__`를 제외했습니다. 따라서
`changed_paths=[]`는 필터에 포함된 source path가 그대로였다는 증거이지 전체 filesystem에
어떤 생성도 없었다는 증거가 아닙니다. 특히 Python import가 만든 cache까지 검사한 결과로
확장하지 않습니다.

Agent 역할 선택은 8장 attempt `104843-e6d50d01`에서 실제로 관찰했습니다. ToolSearch의 `search -> schema loaded -> actual tool_use`는 아직 실제 Python 증거가 없으므로 `not observed/TODO`입니다.

### 이 세 실행이 증명하지 않는 것

세 prompt는 각각 bounded Read, exact Grep 뒤 Read, source Read 뒤 exact Bash 검증을
구체적으로 요구했습니다. 따라서 관찰된 입력은 해당 지시가 실제 tool path로 실현됐다는
증거다. 그러나 raw init에는 내장 Read/Grep/Bash의 정확한 description 전문이 없으며,
description만 바꾼 대조군도 없습니다. 이 세 건을 “내장 도구 설명이 행동을 유발했다”는
인과 증거로 쓰지 않습니다.

8장의 custom description/schema 비교는 같은 fixture와 user prompt에서 10회와 4회의 서로
다른 경로를 관찰했습니다. 하지만 fixed-order 1회씩의 비교이고 provider가 받은 exact
description receipt도 없으므로 일반적인 우열이나 인과 효과는 아직 증명되지 않았습니다.

세 8e trace에는 raw SDK message와 1:1인 `sdk.message`, host `process.event`, root span,
`oracle.verdict`가 있습니다. built-in 도구별 `tool.execution` span은 없습니다.
`oracle.verdict=CAPTURED`와 assertion 0은 수집 완료 표식일 뿐 이 장의 주장이 통과했다는
뜻이 아닙니다. Result에는 primary Opus 5 외에 Haiku 4.5 보조 사용도 기록됐습니다.

## 8e.9 학생 실습

```text
Read, Grep, Bash, Agent 도구 설명을 각각 한 문단으로 설계해 줘.

각 설명에는 다음을 포함해라.
1. 언제 써야 하는지
2. 언제 쓰면 안 되는지
3. 입력을 어떻게 골라야 하는지
4. 결과를 어떻게 주장으로 연결해야 하는지
5. SDK 이벤트에서 무엇으로 평가할 수 있는지
```

## Takeaway

도구 설명은 모델의 선택에 영향을 줄 수 있는 작은 시스템 프롬프트입니다. 그러나 좋은
입력이 한 번 관찰됐다는 사실과 description의 인과 효과는 다릅니다. 실제 `tool_use.input`,
연결된 `tool_result`, 사용자 지시, exact description receipt, 반복 대조군을 분리해야 좋은
설명이 도구 선택과 입력 정확도를 높였다고 판단할 수 있습니다.

## 관련 읽기

- [부록 J: 비공식 시스템 프롬프트 자료를 읽는 법](../appendix/appendix-j.md)
- [부록 K: Claude Fable 5 프롬프트 구조 분석](../appendix/appendix-k.md)

대형 프롬프트 캡처의 줄 수를 비교하기 전에 기본 행동과 tool schema를 분리해야
합니다. 그래야 제품이 제공한 도구 계약을 모델 고유 능력으로 오해하지 않습니다.
