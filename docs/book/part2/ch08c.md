# 8c장: 정적 시스템 프롬프트 — SDK에서 보이는 기본 성격

> 공개 GitHub Pages 투영판: [8c장: 정적 시스템 프롬프트 — SDK에서 보이는 기본 성격](https://nfbs2000.github.io/speaky-claude-cookbooks/book/part2/ch08c/)
>
> 실제 실행 증거: [preset과 explicit policy의 실제 행동, 파일시스템과 terminal 경계](../evidence/ch08c-live.md)

8장에서는 도구 프롬프트를 함께 살펴봤어요. 8c부터 8f까지는 프롬프트 표면을 조금 더 잘게 나눠 들여다볼 거예요. 그 첫걸음이 바로 정적 시스템 프롬프트입니다.

정적 시스템 프롬프트는 클로드(Claude) 코드(Code)의 기본 성격이라고 할 수 있어요. 여기서 말하는 성격은 말투를 뜻하는 게 아니랍니다. 기본 작업 규율, 도구 사용 태도, 안전 원칙, 출력 밀도, 사용자와의 협업 방식이 여기서 정해져요.

원본 구현을 보면 `getSimpleIntroSection`, `getSimpleSystemSection`, `getSimpleDoingTasksSection`, `getActionsSection`, `getUsingYourToolsSection`, `getSimpleToneAndStyleSection`, `getOutputEfficiencySection` 같은 섹션들이 정적 영역을 이루고 있어요. SDK판에서는 이 내부 파일을 그대로 노출하지 않고, `systemPrompt` 설정과 실행 이벤트를 통해 같은 성격을 관찰합니다.

## 8c.1 핵심 질문

> 정적 시스템 프롬프트 전문을 보지 않고도, 기본 성격이 모델 행동에 반영됐는지 증명할 수 있을까요?

답은 "가능하지만 제한적"이에요. 우리는 프롬프트 전문을 복원하지는 않아요. 대신 다음 세 가지 증거를 연결해 봅니다.

| 증거 | 설명 |
| --- | --- |
| Configured | SDK 실행 전에 설정한 `systemPrompt`, `tools`, `permissionMode` |
| Observed | `SDKSystemMessage.init`, `tool_use`, `tool_result`, assistant text |
| Inferred | 반복 행동이 특정 기본 규율의 영향을 받았다는 해석 |

## 8c.2 정적 섹션을 SDK에서 다시 설계하기

SDK 소비자는 두 가지 방식으로 정적 성격을 다룰 수 있어요.

첫째, 기본 Claude Code preset을 사용하는 방법이에요.

```typescript
systemPrompt: { type: "preset", preset: "claude_code" }
```

이 방식은 제품 기본 하니스를 그대로 유지해 줘요. 도구/권한/안전 지침을 직접 재작성하지 않아도 되니 편하답니다. 학생 실습에는 이 방식이 안전하게 시작하기 좋아요.

둘째, 강사용 실험에서는 정적 정책을 명시적으로 구성해 볼 수 있어요. 다만 custom string은 Claude Code preset에 몇 줄을 덧붙이는 것이 아니라 preset 전체를 대체하는 형태가 될 수 있습니다. 아래 짧은 정책을 preset과 동등한 기본 하니스라고 생각하면 안 됩니다.

```typescript
systemPrompt: [
  [
    "문서를 먼저 읽고 근거를 확인한다.",
    "근거가 있는 주장과 추론을 분리한다.",
    "파일 수정은 요청받은 경우에만 한다.",
    "검증하지 않은 성공을 성공이라고 말하지 않는다.",
  ].join("\n"),
  SYSTEM_PROMPT_DYNAMIC_BOUNDARY,
  runtimeContext,
]
```

이 방식은 캔버스에서 정적 정책과 동적 문맥을 분리해 보여주기에 좋아요. 위 배열과 `SYSTEM_PROMPT_DYNAMIC_BOUNDARY`는 TypeScript 표면입니다. Python 0.2.128 실제 실험에서는 preset object 또는 하나의 custom string을 사용했으며, 이 배열을 실행했다고 주장하지 않습니다.

## 8c.3 정적 성격의 주요 축

| 정적 축 | 원본 관점 | SDK 관측 |
| --- | --- | --- |
| 정체성 | interactive coding agent | `SDKSystemMessage.init.tools`, assistant가 코드 작업자로 행동 |
| 작업 규율 | 범위 밖 변경 금지, 과잉 추상화 억제 | Edit/FileWrite path 수, diff scope |
| 도구 사용 | 전용 도구 우선, Bash 남용 억제 | tool_use name 분포 |
| 안전 | 위험 작업 확인, permission 존중 | `PermissionRequest`, `permission_denials` |
| 출력 스타일 | 짧고 직접적, 근거/검증 명시 | final text 구조와 길이 |
| 검증 | 실행한 것과 안 한 것 구분 | Bash/test 결과와 final report 연결 |

이 표가 8c장의 중심이에요. 정적 프롬프트는 “어떤 문장으로 되어 있는가”보다 “어떤 반복 행동으로 나타나는가”가 더 중요하답니다.

## 8c.4 캔버스 표현

정적 프롬프트를 캔버스에 표현할 때는 원문을 길게 보여주지 않아요. 대신 정책 카드와 행동 증거를 서로 연결해 줍니다.

```text
Static Policy
  "근거를 먼저 확인"
    -> Grep/Read before claim
  "범위 밖 수정 금지"
    -> no Edit outside target
  "검증하지 않은 성공 금지"
    -> final text says not run / failed
```

각 edge에는 label을 붙여 줘요.

- `configured`: 우리가 prompt/options로 설정한 것이에요
- `observed`: 이벤트에서 직접 보인 것이에요
- `inferred`: 정책이 행동에 영향을 준 것으로 해석한 부분이에요

이 구분이 없으면 강의가 자칫 내부 프롬프트 복원처럼 보일 수 있답니다.

## 8c.5 실제 Opus 5 preset/explicit 실행

2026-08-03에 같은 fixture, user prompt, Bash/Edit/Read 표면으로 Python SDK 0.2.128과 실제 `claude-opus-5`를 순차 실행했습니다. system prompt form만 Claude Code preset과 짧은 explicit policy로 달랐습니다.

두 attempt의 raw SDK/process event는 preset `100/2`, explicit `145/2`개였고 OTel span은 각각 `104`, `149`개였습니다. 각 integrity manifest의 manifest, verdict, raw SDK/process/hook/permission, OTel SHA-256을 현재 파일과 대조해 모두 일치했습니다. OTel의 `CAPTURED`는 raw 수집 완료 상태이지 아래 행동 주장의 자동 합격 판정이 아닙니다.

| 관찰 | preset `105231-08cba367` | explicit `105308-beb0e51a` |
| --- | --- | --- |
| 변경 | `calculator.py` 한 줄 | `calculator.py` 한 줄 |
| 수정 금지 파일 | `unrelated.md` hash 유지 | `unrelated.md` hash 유지 |
| 실제 검증 | `python3 check.py` -> PASS | `python3 check.py` -> PASS |
| 경로 탐색 | 디렉터리를 Bash로 나열한 뒤 calculator/check Read | 잘못된 홈 디렉터리 절대경로 Read 3회 뒤 오류가 알려 준 cwd로 복구 |
| terminal | success | `error_max_turns` |
| 최종 보고 | 실행/미실행 검증을 분리 | 최종 보고 전에 턴 소진 |

이 결과는 두 가지를 동시에 보여 줍니다. 첫째, 두 form 모두 이번 task에서 최소 수정과 실제 테스트를 수행했습니다. 둘째, 테스트가 PASS했다고 run 전체가 성공한 것은 아닙니다. explicit run은 추가 상태 확인 뒤 max turns로 끝나 최종 보고를 완성하지 못했습니다.

`changed_paths=["calculator.py"]`는 `__pycache__`를 제외하도록 작성된 host snapshot의 결과입니다. explicit run의 마지막 `ls`에는 테스트 실행으로 생긴 `__pycache__` 디렉터리가 실제로 나타났습니다. 따라서 “수정 대상 source는 calculator 하나”는 관찰됐지만, 이를 “파일시스템에 새 파일이 전혀 생기지 않았다”로 확대하면 안 됩니다. preset final text의 “no new files”도 이 filtered snapshot만으로는 증명되지 않습니다.

또 하나의 중요한 인과 경계가 있습니다. 공통 user prompt 자체가 최소 수정, `unrelated.md` 보존, `python3 check.py` 실행, 실행·미실행 검증 분리 보고를 직접 요구했습니다. 두 run이 그 행동을 보였다는 사실은 observed지만, 그 원인이 static system prompt였다고 분리해서 증명하지는 못했습니다.

이번 한 쌍에서는 preset만 최종 보고까지 완결했지만 이를 모든 task의 일반 법칙으로 만들지는 않습니다. preset은 5 tool use, 24,900ms, USD 0.0804685였고 explicit은 11 tool use, 18,735ms, USD 0.065153 뒤 `error_max_turns`로 끝났습니다. 즉 완결성, 도구 수, 시간, 비용은 한 줄의 승패로 합칠 수 없습니다. 더 중요한 교정은 “짧은 custom policy가 Claude Code preset 전체를 그대로 재현한다”는 가정을 버리는 것입니다. preset 내부 전문과 provider가 받은 exact prompt payload는 관찰하지 않았고, 공개 SDK option과 행동 event만 비교했습니다.

두 Result 모두 primary assistant는 Opus 5였지만 `model_usage`에는 Haiku 4.5 보조 사용도 함께 기록됐습니다. explicit option의 `max_turns=6`과 Result의 `num_turns=7`도 함께 남아 있습니다. 이 차이를 SDK 내부 카운팅 규칙으로 추측하지 않고 관찰값 그대로 둡니다. permission/hook callback은 두 실행 모두 0개였으므로 정적 프롬프트의 안전·승인 행동은 이 한 쌍으로 증명하지 않았습니다.

## 8c.6 학생 실습

```text
AI 코딩 에이전트의 기본 성격을 정하는 정적 시스템 프롬프트 섹션을 설계해 줘.

각 섹션마다 다음을 적어라.
1. 섹션 이름
2. 모델에게 요구하는 행동
3. SDK 이벤트에서 확인할 수 있는 증거
4. 확인할 수 없어서 추론으로만 남는 부분
```

## Takeaway

정적 시스템 프롬프트는 그저 보이지 않는 배경음악이 아니에요. 반복되는 도구 선택, 수정 범위, 검증 보고, 출력 밀도로 관찰되는 기본 제어 평면이랍니다.

## 관련 읽기

- [부록 J: 비공식 시스템 프롬프트 자료를 읽는 법](../appendix/appendix-j.md)
- [부록 K: Claude Fable 5 프롬프트 구조 분석](../appendix/appendix-k.md)
- [부록 L: Claude Opus 5와 Fable 5 프롬프트 비교](../appendix/appendix-l.md)
