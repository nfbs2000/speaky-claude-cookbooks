# 18b장: 샌드박스 시스템 - 격리된 실행 환경

> 공개 GitHub Pages 투영판: [18b장: 샌드박스 시스템](https://nfbs2000.github.io/speaky-claude-cookbooks/book/part5/ch18b/)
>
> 원시 SDK/host/OTel 판독표: [18b장 실제 SDK 관찰](../evidence/ch18b-live.md)

권한 시스템이 “실행을 허용할 것인가”를 다룬다면, sandbox는 허용된 Bash process가
접근할 수 있는 범위를 제한합니다. 이 둘은 같은 것이 아닙니다. sandbox 설정,
permission rule, 실제 command result, touched files를 함께 봐야 합니다.

## 18b.1 핵심 질문

> 동일한 명령이 sandbox off/on에서 어느 경로에 실제로 파일을 만들었는가?

## 18b.2 현재 Python SandboxSettings

Python Agent SDK 0.2.128의 `SandboxSettings` 필드는 다음과 같습니다.

- `enabled`
- `autoAllowBashIfSandboxed`
- `excludedCommands`
- `allowUnsandboxedCommands`
- `network`
- `ignoreViolations`
- `enableWeakerNestedSandbox`

`network`에는 `allowedDomains`, `deniedDomains`, `allowManagedDomainsOnly`,
`allowUnixSockets`, `allowAllUnixSockets`, `allowLocalBinding`, `allowMachLookup`,
proxy port 등이 있습니다.

이 타입에는 `failIfUnavailable`이 없고 `managedSettings`도 sandbox field가 아닙니다.
책에서 current Python option처럼 쓰면 안 됩니다. SDK docstring도 filesystem/network
restriction은 sandbox setting만이 아니라 Read/Edit/WebFetch permission rule로
구성한다고 명시합니다.

## 18b.3 실제 off/on 통제 비교

두 run의 모든 `AssistantMessage.model`은 실제 `claude-opus-5`였습니다. 요청 옵션이나
init 설정값만 보고 실제 모델을 판정하지 않았습니다. 각 run의 임시 root에
`workspace/`와 sibling output path를 만들고, 같은 형태의 command가 두 경로에 marker를
쓰도록 했습니다. 실제 시스템 파일과 network는 건드리지 않았습니다.

두 terminal Result의 `model_usage`에는 보조 사용량으로 `claude-haiku-4-5-20251001`도
기록됐습니다. 따라서 “사용자에게 응답한 AssistantMessage는 모두 Opus 5였다”는
관찰과 “provider run 전체에서 Opus만 사용됐다”는 주장을 구분해야 합니다. 후자는
이번 증거가 지지하지 않습니다.

### sandbox disabled control

- attempt `125947-4ccb1c9c`
- OTel trace `95a77a594a208b2b89d5b3a8af09df01`
- `sandbox.enabled=false`

| path | before | after |
| --- | --- | --- |
| cwd 내부 | 없음 | `CH18B_INSIDE_WRITE`, SHA 기록 |
| workspace sibling | 없음 | `CH18B_OUTSIDE_WRITE`, SHA 기록 |

Bash ToolResult는 `CH18B_COMMAND_FINISHED`였고 host readback이 두 파일의 존재와 정확한
내용을 확인했습니다.

### sandbox enabled

- attempt `130028-cc834055`
- OTel trace `9477403be667e4b66458ba1a0f5eebdb`
- `enabled=true`
- `autoAllowBashIfSandboxed=true`
- `allowUnsandboxedCommands=false`
- `excludedCommands=[]`

| path | Bash result | host readback |
| --- | --- | --- |
| cwd 내부 | 별도 오류 없음 | marker 파일 존재, SHA 일치 |
| workspace sibling | `operation not permitted` | 파일 없음 |

이 통제 pair에서 sandbox enabled 설정과 workspace 밖 write 차단이 함께 관찰됐습니다.
내부 OS adapter 이름이나 생성된 profile 원문은 stream에 없으므로 macOS Seatbelt의
세부 rule을 확인했다고 쓰지 않습니다.

## 18b.4 성공 envelope의 함정

command는 세 문장을 `;`로 연결했습니다. sibling redirect가 실패해도 마지막 marker
printf가 성공했기 때문에 SDK ToolResult는 `is_error=false`였고 terminal Result도
success였습니다.

```text
inside write success
  ; outside write operation not permitted
  ; final printf success
  -> shell exit 0
  -> ToolResult.is_error false
```

따라서 `is_error=false`는 모든 subcommand 성공을 뜻하지 않습니다. stderr 원문과 host
file state를 함께 검증해야 합니다. 반대로 모델은 file을 readback하지 않았다고
정직하게 말했지만, probe host는 process 종료 후 직접 내용을 읽어 확정했습니다.

## 18b.5 관찰하지 않은 경계

- network domain/socket 정책은 실행하지 않았습니다.
- `excludedCommands`와 `dangerouslyDisableSandbox` 우회는 실행하지 않았습니다.
- `blocked_path` callback은 호출되지 않아 관찰하지 못했습니다.
- sandbox unavailable fallback 동작은 current Python field로 구성하지 않았습니다.
- enterprise/managed policy hierarchy와 exact OS adapter는 관찰하지 않았습니다.
- temp directory는 host context가 정리하지만 post-cleanup file scan은 evidence에 없습니다.

## 18b.6 안전한 검증 프롬프트

이 장의 프롬프트는 보안 판정을 피하려고 위험한 의도를 숨기지 않습니다. 실험 목적,
허용 도구, 임시 경로, 금지된 부작용을 처음부터 좁게 선언합니다.

```text
제공된 printf command를 Bash로 정확히 한 번만 실행한다.
경로는 probe가 만든 임시 workspace와 그 임시 root의 sibling으로 제한한다.
네트워크, 사용자 파일, 자격증명, 권한 상승, 지속 프로세스는 사용하지 않는다.
실행 후 관찰한 출력만 짧게 보고하고 파일 성공 여부를 추측하지 않는다.
```

모델이 보안 사유로 거부하거나 더 낮은 모델로 fallback되면 프롬프트를 우회형으로
바꾸지 않습니다. 해당 attempt를 `model_refusal_fallback`으로 보존하고 더 낮은 위험도의
관찰 단계로 내립니다. 이번 두 공개 attempt에는 그 fallback이 없었으며, 실제 응답
모델은 raw `AssistantMessage.model`로 확인했습니다.

## 18b.7 캔버스 표현

```text
Bash ToolUse
  -> sandbox option snapshot
  -> exact command
  -> stdout/stderr + shell exit
  -> host inside/outside file state
  -> cleanup evidence
```

표시할 정보:

| 필드 | 이유 |
| --- | --- |
| configured sandbox | host 실행 계약 |
| cwd and target paths | boundary 비교 |
| command separators/exit semantics | partial failure 해석 |
| raw ToolResult | model-visible 실행 결과 |
| touched file SHA/content | 실제 side effect |
| not-observed fields | OS/network/policy 과장 방지 |

## 18b.8 학생 실습

```text
실제 시스템 파일을 건드리지 않는 sandbox 통제 실험을 설계해라.

1. temp cwd 내부와 sibling path를 준비한다.
2. sandbox off/on에서 같은 command를 실행한다.
3. ToolResult와 shell exit를 보존한다.
4. host가 두 경로를 직접 readback한다.
5. network, blockedPath, cleanup처럼 미검증 항목을 따로 남긴다.
```

## Takeaway

Sandbox evidence는 옵션 배지나 모델 설명이 아니라 동일 명령의 경계 차이로 보여 줘야
합니다. 이번 실제 pair에서 disabled는 두 파일을 만들었고 enabled는 cwd 내부만
만들었습니다. 중간 차단이 있어도 마지막 shell command 때문에 success envelope가
나올 수 있으므로 raw stderr와 touched-files 검증이 필수입니다.
