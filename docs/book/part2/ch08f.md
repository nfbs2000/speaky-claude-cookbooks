# 8f장: 권한/분류기 프롬프트 — 자동 승인, CLAUDE.md prefix, deny 규칙의 숨은 제어 평면

> 공개 GitHub Pages 투영판: [8f장: 권한/분류기 프롬프트 — 자동 승인, CLAUDE.md prefix, deny 규칙의 숨은 제어 평면](https://nfbs2000.github.io/speaky-claude-cookbooks/book/part2/ch08f/)

권한 시스템은 단순한 버튼 UI가 아니에요. 모델이 어떤 행동을 원했고, host가 그것을 허용할지, 사용자에게 물을지, 거절할지를 결정하는 별도의 제어 평면이랍니다.

원본 구현 관점에서는 auto mode classifier, permission template, `CLAUDE.md` prefix, allow/deny/environment rules, Bash prompt rule이 이 레이어를 이룹니다. SDK판에서는 `permissionMode`, `allowedTools`, `disallowedTools`, `canUseTool`, permission hooks, `permission_denials`로 함께 관찰해 봐요.

## 8f.1 핵심 질문

> 도구 실행 승인/거절은 단순 UI 선택인가, 아니면 별도의 모델/규칙 기반 하니스인가?

규칙, callback, mode 전환, 실행 또는 거절이 별도 사건으로 이어진다는 의미에서는 후자예요. 다만 이번 실제 실행이 `auto` 내부 classifier의 prompt나 판단 이유까지 공개한 것은 아닙니다. 또한 whole-tool allow rule과 일부 permission mode는 `canUseTool`보다 먼저 승인되어 callback을 건너뛸 수 있습니다.

## 8f.2 SDK 권한 표면

| SDK 계약 | 의미 |
| --- | --- |
| `permissionMode: "default"` | 표준 permission behavior |
| `permissionMode: "acceptEdits"` | 이번 격리 실행에서는 `Edit`를 callback 없이 허용 |
| `permissionMode: "plan"` | 계획 단계와 host 승인 뒤 실행 단계를 분리 |
| `permissionMode: "dontAsk"` | 사전 승인 없으면 묻지 않고 거절 |
| `permissionMode: "auto"` | 자동 판단 mode. 이번 요청은 허용됐지만 이유는 미관측 |
| `permissionMode: "bypassPermissions"` | 일반 prompt를 우회하지만 명시적 deny는 여전히 우선할 수 있음 |
| `allowedTools` | 자동 허용 도구 목록 |
| `disallowedTools` | 도구 종류와 경로에 따라 init에서 제거되거나 실행 시 차단 |
| `canUseTool` | 사전 규칙이 `ask`로 판정한 요청을 앱이 판단 |
| `permissionPromptToolName` | permission 요청을 특정 MCP tool로 라우팅 |

이 표면은 시스템 프롬프트보다 제품 안전성에 좀 더 직접적으로 닿아 있어요.

## 8f.3 `canUseTool`은 중요한 관측 지점이지만 보편적이지 않다

SDK의 `can_use_tool` callback은 permission 규칙이 `ask`로 판정한 tool 실행을 host가 판단할 때 호출될 수 있어요. 이 callback은 tool name과 input뿐 아니라 `title`, `display_name`, `description`, `blocked_path`, `decision_reason`, `tool_use_id`, `agent_id` 같은 정보를 함께 받을 수 있답니다. 실제 request에서는 이 필드 중 일부가 null일 수 있습니다.

중요한 예외가 있습니다. `allowedTools`/`allowed_tools`가 도구 전체를 허용하면 그 규칙이 callback보다 먼저 적용될 수 있습니다. 이 경우 callback은 호출되지 않습니다. 모든 호출을 gate하려면 PreToolUse hook을 사용하거나, allow rule을 좁혀 callback까지 흘러오게 설계해야 합니다.

이런 정보 덕분에 제품은 “왜 물어보는지”를 사용자에게 친절하게 설명할 수 있어요.

아래는 UI 설계를 위한 **예시**이며, 이번 run에서 관찰한 실제 callback payload는 아닙니다.

```text
toolName: Bash
input.command: "git push --force"
decisionReason: "destructive git operation"
title: "Claude wants to run a git command"
action: ask user / deny
```

이것이 없으면 UI는 “승인할까요?”만 보여주게 돼요. 그러면 사용자는 자기가 무엇을 승인하는지 알기 어렵겠죠.

## 8f.4 AskUserQuestion과 PermissionRequest는 다르다

이 사건을 섞어 버리면 제품이 불안정해지기 쉬워요. 아래는 제품 UI lane 구분이지, 네 가지가 모두 동급 top-level `SDKMessage` class라는 뜻은 아닙니다.

| 이벤트 | 의미 | UI |
| --- | --- | --- |
| AskUserQuestion tool use | 작업 방향, 요구사항, 선택지를 사용자에게 질문 | 대화 카드 |
| PermissionRequest hook/control request | 도구 실행을 host가 승인/거절해야 함 | 권한 카드 |
| MCP elicitation callback/protocol | MCP 서버가 form/url 입력을 요구 | 외부 연결/인증 카드 |
| denial evidence | callback decision, error tool result, terminal `permission_denials` | 원인/대체 경로 |

책 캔버스와 강의 앱에서는 이 네 lane을 나눠서 다루는 게 좋아요. “모델이 질문했다”와 “host가 위험 작업 승인을 요구했다”는 완전히 다른 사건이거든요.

## 8f.5 `CLAUDE.md`와 권한 판단

프로젝트 지침이 본 실행 루프뿐 아니라 permission/classifier 판단에도 영향을 줄 가능성은 있지만, 이번 실행에서는 그 인과를 관찰하지 못했어요. 따라서 SDK판에서는 이를 사실로 복원하지 않고 다음 자료를 함께 기록합니다.

- 어떤 instruction source가 로드됐는가
- permission decision 직전 tool input은 무엇이었는가
- user/project rule이 allow/deny에 영향을 줬다고 볼 증거가 있는가
- 직접 증거가 없으면 `Inferred`로 표시한다

예:

```text
Configured: project instruction says "never push without explicit approval"
Observed: Bash("git push") triggered permission request
Observed: user denied
Inferred: project rule likely contributed to conservative handling
```

## 8f.6 권한 캔버스

권한 판단은 별도 lane으로 표시해 봐요.

```text
Tool Intent
  -> Permission Policy
  -> User/System Decision
  -> Tool Execution or Denial
  -> Agent Recovery
```

각 노드에는 다음을 붙여 주면 좋아요.

| 필드 | 이유 |
| --- | --- |
| `tool_use_id` | 요청과 결과 연결 |
| `toolName` | 어떤 도구인가 |
| `input summary` | 무엇을 하려 했는가 |
| `risk reason` | 왜 물었는가 |
| `decision` | allow/deny/ask |
| `agentID` | subagent가 요청했는가 |
| `recovery` | 거절 후 모델이 어떻게 복구했는가 |

## 8f.7 실제 Opus 5 권한 제어 실행

2026-08-03에 외부 효과가 없는 같은 in-process MCP tool을 destructive/open-world로 표시하고, Python SDK 0.2.128과 실제 `claude-opus-5`로 다섯 권한 조건을 순차 실행했습니다. 다섯 prompt는 모두 같은 tool과 input을 정확히 한 번 호출하라고 명시했으므로, 여기서 검증한 것은 **tool 선택 능력**이 아니라 **선택된 요청이 permission 경로를 어떻게 통과하는가**입니다.

| case | 실제 결과 |
| --- | --- |
| callback allow `110308-ea475cf9` | request/allow가 같은 tool use ID로 연결, handler 1회, marker result |
| callback deny `110349-dac28e5d` | request/deny 연결, handler 0회, error tool result와 terminal denial |
| allowed rule `110426-25b7a9d7` | callback 0회, handler 1회, `CanUseToolShadowedWarning` |
| dontAsk `110508-45847b17` | callback 0회, handler 0회, denial |
| auto `110547-47d54887` | callback 0회, handler 1회, marker result |

allow와 deny를 반환한 주체는 실험 host program입니다. 사람이 버튼을 누르지는 않았지만, 실제 SDK callback과 native tool request에 결정이 돌아가 handler 실행 여부가 바뀌었으므로 permission mechanism은 실제로 검증됐습니다. UI click을 검증했다고는 쓰지 않습니다.

가장 중요한 반례는 allowed rule입니다. whole-tool allow가 있자 `can_use_tool`은 한 번도 호출되지 않았고 SDK 자체가 shadow warning을 냈습니다. 따라서 callback 하나만 기록해서 모든 실행의 permission audit log라고 부르면 누락이 생깁니다.

`auto`는 이번 controlled request를 허용했습니다. raw에서 확인되는 것은 mode, tool request, handler 실행, marker result뿐입니다. host `can_use_tool` callback은 호출되지 않았으므로 모델 final의 "permission handler가 호출됐다"는 설명은 증거보다 강합니다. 이 관찰로 auto가 항상 허용한다고 말할 수 없고, classifier의 비공개 이유도 관찰되지 않았습니다. `dontAsk`는 같은 요청을 사전 allow 없이 거절했습니다.

다른 장의 실제 실행을 보조 증거로 연결하면 우선순위가 더 선명해집니다.

| permission 표면 | 연결한 실제 실행 | 관찰 범위 |
| --- | --- | --- |
| `plan` | 4b장 `101040-25cace50` | plan 중 workspace SHA 불변, `ExitPlanMode` callback 거절, host 승인 기록과 `acceptEdits` mode 전환 뒤 `Edit`로 SHA 변경 |
| `disallowed_tools` | 8장 `104523-e1aa0451` | Read와 Bash를 구성했지만 init에는 Read만 노출되고 실제 path도 Read뿐 |
| `acceptEdits` | 16장 `122337-5c9ba78a` | 거절 callback을 구성했지만 callback 0회, 실제 `Edit` 성공, 파일 SHA 변경 |
| `bypassPermissions` | 16장 `122418-70f4ebd5` | 격리 MCP 요청이 거절 callback 없이 handler까지 실행 |
| bypass + explicit deny | 16장 `122506-9120507f` | 같은 mode여도 명시적 deny가 handler를 막고 terminal denial을 남김 |

4b장의 `actor=user` 승인 record도 host program이 남긴 사건입니다. 실제 인간이 UI 버튼을 누른 증거로 승격하지 않습니다. `permission_prompt_tool_name`과 외부 permission tool의 왕복 routing, 실제 사용자 UI 승인, 프로젝트 instruction이 auto classifier에 미친 인과는 아직 `additional observation required`입니다.

SDK 0.2.128 source에서는 `can_use_tool`과 `permission_prompt_tool_name`을 동시에 지정하면 `ValueError`를 내고, `can_use_tool`을 쓸 때 내부 control protocol용 이름을 `stdio`로 설정합니다. 이는 설치된 SDK source 계약을 확인한 것이며 외부 permission tool routing의 실제 실행 증거는 아닙니다.

전체 raw/OTel 판독과 교정 목록은 [8f장 실제 권한 제어 관찰](../evidence/ch08f-live.md)에 보존합니다.

## 8f.8 학생 실습

```text
AI 코딩 에이전트의 permission policy를 설계해 줘.

조건:
1. Read/Grep/Glob은 자동 허용
2. Edit/Write는 사용자 승인 필요
3. Bash test/build는 허용
4. Bash git push, rm, deploy는 승인 또는 거절
5. AskUserQuestion과 PermissionRequest를 UI에서 분리

각 결정이 SDK에서 어떤 옵션, callback, hook, result 필드로 관찰되는지 적어 줘.
```

## Takeaway

권한/분류기 프롬프트는 그저 보안 부속품이 아니에요. 사용자가 모델을 통제할 수 있게 만들어 주는 핵심 제어 평면이랍니다. 좋은 제품은 “승인/거절” 버튼만 보여주는 데 그치지 않고, 모델이 무엇을 하려 했고 왜 멈췄는지까지 함께 보여준답니다.
