# 8d장: 동적 프롬프트 레이어 — 세션, 메모리, 팀, MCP가 뒤에 붙는 법

> 공개 GitHub Pages 투영판: [8d장: 동적 프롬프트 레이어 — 세션, 메모리, 팀, MCP가 뒤에 붙는 법](https://nfbs2000.github.io/speaky-claude-cookbooks/book/part2/ch08d/)

8c장에서 기본 성격을 살펴봤다면, 이번 8d장에서는 이번 세션만의 조건을 함께 들여다볼게요.

같은 Claude Code preset을 사용하더라도 프로젝트가 바뀌고, `cwd`가 바뀌고, `CLAUDE.md`가 바뀌고, 스킬과 플러그인이 바뀌고, MCP 서버가 붙으면 모델 행동도 조금씩 달라진답니다. 바로 이 레이어가 동적 프롬프트예요.

## 8d.1 핵심 질문

> 지금 세션에만 붙은 문맥은 무엇이며, 그 문맥이 어떤 도구 선택과 응답을 만들었는가?

## 8d.2 동적 레이어 목록

원본 관점의 동적 레이어는 다음과 같아요. 이 SDK 책에서는 이를 `Options` 구성값, `SDKSystemMessage.init`, `SDKHook` 메시지, `tool_use`/`tool_result` 후속 행동으로 다시 차근차근 접지해 봅니다.

| 동적 레이어 | 의미 | SDK 표면 |
| --- | --- | --- |
| session guidance | 현재 모드/진행 제약 | prompt append, user prompt, hook context |
| memory / CLAUDE.md | 프로젝트/사용자 지침 | `settingSources`, `InstructionsLoaded` hook |
| env info | cwd, OS, git, model 관련 정보 | `SDKSystemMessage.init.cwd/model` |
| language/output style | 응답 언어/스타일 | assistant text |
| MCP instructions | 외부 도구 서버 설명 | `mcpServers`, `SDKSystemMessage.init.mcp_servers` |
| skills | 작업 능력 설명 | `skills`, `SDKSystemMessage.init.skills` |
| plugins | command/agent/hook bundle | `plugins`, `SDKSystemMessage.init.plugins` |
| team/agent definitions | 역할별 subagent prompt | `agents`, `AgentDefinition` |

이 중 일부는 SDK `init` 메시지에 바로 보이고, 일부는 후속 tool/hook 이벤트를 통해서만 드러난답니다.

## 8d.3 `Options.systemPrompt`와 `SYSTEM_PROMPT_DYNAMIC_BOUNDARY`

TypeScript SDK 타입은 `systemPrompt`를 배열로 받을 수 있는데요, 그 안에 `SYSTEM_PROMPT_DYNAMIC_BOUNDARY`를 넣어 정적 prefix와 동적 suffix를 나눠 줄 수 있어요. 이 장의 Python 0.2.128 실험에서는 이 배열을 사용하지 않았고, preset/setting sources/skills/MCP를 각각 관찰했습니다.

```typescript
systemPrompt: [
  staticCoursePolicy,
  SYSTEM_PROMPT_DYNAMIC_BOUNDARY,
  [
    `chapter=${chapterId}`,
    `chapterFile=${chapterFile}`,
    `selectedText=${selectedText}`,
  ].join("\n"),
]
```

강의 관점에서 이 경계는 두 가지 의미를 지녀요.

첫째, 캐시와 재현성이에요. 매번 바뀌는 chapter/selection을 앞쪽 정적 정책에 섞어 두면 같은 실험을 비교하기가 어려워집니다.

둘째, 시각화예요. 캔버스에서 “항상 적용되는 규칙”과 “이번 실습에만 적용된 문맥”을 깔끔하게 분리할 수 있답니다.

여기서 한 가지 기억해 두면 좋은 점은, 이 구분이 Configured 입력이라는 거예요. 실제로 어떤 동적 문맥이 사용됐는지는 Observed 이벤트로 확인해 봐야 합니다. 예를 들어 `Options.includeHookEvents: true`를 켜면 `hook_started`, `hook_progress`, `hook_response` 계열 `SDKHook` 메시지를 수집할 수 있습니다. 그러나 옵션을 켰다는 사실만으로 `InstructionsLoaded`나 `ConfigChange`가 반드시 도착했다고 쓰면 안 됩니다. 실제 hook event가 있는지 raw stream에서 별도로 확인해야 합니다.

```typescript
const stream = query({
  prompt,
  options: {
    cwd,
    systemPrompt: [staticPolicy, SYSTEM_PROMPT_DYNAMIC_BOUNDARY, sessionContext],
    settingSources: ["project"],
    includeHookEvents: true,
    includePartialMessages: true,
  },
});
```

## 8d.4 `CLAUDE.md`와 설정 로딩

SDK의 `settingSources`는 파일 시스템 설정을 얼마나 로드할지 정해 줍니다.

| 설정 | 의미 |
| --- | --- |
| omitted | CLI 기본과 유사하게 설정 로딩 |
| `["project"]` | 프로젝트 설정/지침 중심 |
| `["user", "project"]` | 사용자 전역 + 프로젝트 |
| `[]` | SDK isolation에 가까운 모드 |

여기서 눈여겨볼 점은, `CLAUDE.md` 같은 프로젝트 지침이 “사용자 문서”이면서 동시에 모델 행동을 바꾸는 프롬프트 표면이기도 하다는 거예요. 책 캔버스는 어떤 지침 파일이 로드됐는지를 `includeHookEvents`로 받은 `InstructionsLoaded` hook, `ConfigChange` hook, 또는 `SDKSystemMessage.init` session metadata로 표시해 주면 좋습니다.

## 8d.5 스킬/플러그인/MCP는 동적 능력 표면이다

`skills`, `plugins`, `mcpServers`는 모델이 사용할 수 있는 능력 자체를 바꿔 줍니다.

```typescript
options: {
  skills: ["book-evidence"],
  plugins: [{ type: "local", path: "./plugins/course-lab" }],
  mcpServers: {
    docs: { command: "node", args: ["./mcp/docs.js"] },
  },
}
```

이 설정은 `SDKSystemMessage.init`에 목록으로 드러날 수 있어요. 다만 목록만으로는 조금 부족합니다. 후속 이벤트에서 실제로 해당 skill/plugin/MCP tool이 행동에 영향을 줬는지까지 연결해 봐야 해요. `init.skills`에 이름이 있고 별도 `Skill` tool이 없다는 두 사실은 모순이 아닙니다. skill이 문맥으로 로드되는 것과 Skill tool을 호출하는 것은 다른 표면일 수 있습니다.

```text
init.skills includes "book-evidence"
  -> tool_use search_evidence
  -> returned sentence
  -> claim card
```

## 8d.6 캔버스 표현

동적 레이어는 prompt stack 형태로 보여주면 한눈에 들어와요.

```text
Dynamic Context Stack
  cwd
  chapter file
  selected paragraph
  loaded instructions
  skills
  plugins
  mcp servers
  active agents
```

각 항목에는 상태를 함께 붙여 줍니다.

| 상태 | 의미 |
| --- | --- |
| loaded | init 또는 instruction 행동으로 세션 로딩을 확인 |
| used | 실제 tool/result 또는 고유 행동으로 사용을 확인 |
| stale | 로드됐지만 현재 세션과 안 맞음 |
| missing | 프롬프트가 기대했지만 init/event에 없음 |

## 8d.7 실제 Opus 5 동적 레이어 실행

2026-08-03에 Python SDK 0.2.128과 실제 `claude-opus-5`로 세 case를 순차 실행했습니다.

> 전체 raw 판독: [8d장 실제 Python SDK 관찰](../evidence/ch08d-live.md)

| case | configured | observed | 판정 경계 |
| --- | --- | --- | --- |
| project instructions `105511-0c4575df` | `setting_sources=["project"]`, marker는 `CLAUDE.md`에만 존재, tools 0 | assistant가 무작위 marker를 정확히 반환 | dedicated instruction hook은 0개 |
| isolation `105549-8fc27cde` | 같은 파일을 만들되 `setting_sources=[]`, tools 0 | marker 미출현, assistant `MISSING` | text 안의 Bash 호출/출력은 실제 tool event가 아님 |
| skill + MCP `105633-ee1cdfa1` | `skills=["dynamic-evidence"]`, in-process MCP | init.skills/MCP/tools와 실제 MCP use seq 16/result seq 19 | skill 문구의 단독 인과 효과는 미확정 |

isolation case에서 파일 자체를 지운 것이 아닙니다. host probe는 `CLAUDE.md`를 workspace에 쓴 뒤 settings loading만 껐습니다. 모델은 marker 부재는 정확히 보고했으나, seq 28의 일반 `TextBlock` 안에 Bash 호출 문법과 `ls` 출력처럼 보이는 문자열을 만든 뒤 “workspace is empty, no `CLAUDE.md`”라고 결론 냈습니다. 이 attempt의 init tools는 빈 배열이고 `ToolUseBlock`, `ToolResultBlock`, host `tool.execution`은 모두 0개입니다. 따라서 화면에 명령과 출력처럼 보이는 문자열이 있어도 typed SDK 사건이 없으면 실제 실행 증거로 취급하면 안 됩니다.

또한 `setting_sources=[]`인 init에도 기본 skill 이름들과 기본 agent 이름들은 남았습니다. 이 옵션은 이번 무작위 project marker를 제외했지만 세션의 모든 능력 목록을 비우는 완전한 격리 스위치라고 일반화할 수 없습니다.

skill + MCP case에서 init은 `dynamic-evidence` skill과 connected MCP server를 표시했고, 모델은 `mcp__dynamic__read_dynamic_context(scope="session")`를 실제 호출해 session-only marker를 받았습니다. 별도 Skill tool/hook은 없었습니다. 더구나 user prompt도 `dynamic-evidence`를 사용하라고 직접 지시했고 사용 가능한 도구는 해당 MCP 하나뿐이었습니다. 따라서 “skill이 목록에 로드됨”, “MCP가 실제 사용됨”, “SKILL.md 문구가 호출의 단독 원인임”을 각각 loaded/observed/not proven으로 나눕니다. final의 “dynamic-evidence skill이 exposed되지 않았다”는 설명도 `init.skills`와 충돌합니다. `Skill` tool이 없다는 사실과 skill registry에 이름이 없다는 주장은 구분해야 합니다.

세 실행 모두 hook callback과 permission callback은 0개였습니다. `include_hook_events=True`는 수집을 요청한 구성일 뿐, `InstructionsLoaded` 같은 dedicated hook이 발생했다는 증거가 아닙니다. OTel의 `oracle.verdict=CAPTURED`, assertion count 0도 판정 합격이 아니라 raw 수집 완료 표식입니다.

project attempt는 Opus 5만 사용했지만 isolation과 skill+MCP Result의 `model_usage`에는 primary Opus 5 외에 Haiku 4.5 보조 사용도 기록됐습니다. 화면에서 “actual model=Opus 5”를 “모든 provider 사용이 Opus 5뿐”으로 읽으면 안 됩니다.

local plugin은 이번 장에서 실제 package 로딩과 후속 사건을 검증하지 않았습니다. `not observed/TODO`이며 init 예시만으로 사용됐다고 쓰지 않습니다.

attempt manifest는 장 원문 hash와 option summary를 묶지만 probe source, 실제 `CLAUDE.md`/`SKILL.md` 내용, user prompt 전문, MCP handler source를 hash로 묶지 않았습니다. 이 장의 fixture 설명은 host source와 함께 확인한 것이며, 이후 실험에서는 exact config와 fixture hash를 provenance에 포함해야 합니다.

## 8d.8 학생 실습

```text
AI 에이전트 세션에 들어갈 정적 지침과 동적 지침을 분리해 줘.

동적 지침에는 cwd, 프로젝트 문서, skill, plugin, MCP, 현재 작업 목표를 포함해라.
각 항목이 SDK에서 어떤 옵션, init metadata, hook event로 관찰될 수 있는지도 적어라.
```

## Takeaway

동적 프롬프트 레이어는 에이전트를 지금 이 프로젝트에 접지시키는 운영 계층이에요. 동시에 캐시와 재현성을 깨뜨리는 가장 큰 원인이기도 하니, 정적 정책과는 분리해서 설계하고 시각화해 주는 게 좋습니다.

## 관련 읽기

- [부록 M: Claude 시스템 프롬프트 버전 진화 지도](../appendix/appendix-m.md)

Claude Code의 full/lean prompt와 agents·skills 주입 채널 변화는 “같은 내용도
어느 메시지에 들어가는가”가 실행과 관측에 영향을 준다는 실제 비교 사례입니다.
