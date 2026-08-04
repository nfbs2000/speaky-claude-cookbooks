# 20b장: 두 worker의 순차 handoff와 native Team 경계

> 공개 GitHub Pages 투영판: [20b장: 두 worker 순차 handoff와 native Team 경계](https://nfbs2000.github.io/speaky-claude-cookbooks/book/part6/ch20b/)
>
> 실제 SDK 증거 판독: [20b장 실제 SDK 관찰: leader-mediated handoff와 provenance 한계](../evidence/ch20b-live.md)

여러 worker를 실행했다고 곧바로 Claude Code의 native Team, mailbox, task claim이
작동했다고 말할 수는 없습니다. 이 장은 실제로 관찰한 leader 중심 handoff와 아직
실행하지 않은 native Team 기능을 분리합니다.

## 20b.1 핵심 질문

> 첫 worker가 실행 중에 얻은 결과가 leader를 거쳐 두 번째 worker의 실제 입력이 되었는가?

## 20b.2 검증 설계

이번 probe host는 실행 직전에 무작위 marker를 만들어 파일에 기록했습니다. 첫 worker의
실제 delegated prompt에 marker 값이 없고 `Read` 뒤에 처음 나타난 것은 raw stream에서
관찰됐습니다. 다만 역사적 attempt는 당시 initial leader/system prompt와 probe 소스
hash를 묶지 않았으므로 **leader도 처음 marker를 몰랐다**는 더 강한 인과 주장은
추론으로 낮춥니다.

```text
team/research.txt = CH20B_RUNTIME_69f13d30acdb420f
team/review.txt   = CH20B_REVIEW_FILE_CONFIRMED
```

두 worker는 모두 foreground, `model="inherit"`, `tools=["Read"]`이고 `Agent`,
`Bash`, `Edit`, `Write`를 사용할 수 없습니다.

```text
Leader
  -> research-reader
       -> Read research.txt
       -> RESEARCH_RESULT:<runtime-only marker>
  -> handoff-reviewer
       input includes exact research result
       -> Read review.txt
       -> REVIEW_RESULT:<marker>|REVIEW_FILE:<review marker>
  -> LEADER_TEAM_SYNTHESIS:<review result>
```

Leader에게 두 Agent를 동시에 실행하지 말고 첫 worker의 complete result를 받은 뒤에만
두 번째를 호출하라고 지시했습니다.

## 20b.3 실제 Opus 5 실행

- attempt: `132134-ef857460`
- OTel trace: `1c64771cff603eaf8728f772e537ce90`
- actual response model: 여덟 `AssistantMessage.model` 모두 `claude-opus-5`
- 두 worker `resolvedModel`: `claude-opus-5`
- provider usage boundary: terminal `model_usage`에는 Opus 5와 보조 Haiku 4.5가 함께 기록
- terminal status: success

### 첫 worker

| sequence | evidence |
| ---: | --- |
| 21 | `research-reader` Agent ToolUse |
| 22 | first `TaskStartedMessage` |
| 28 | worker `Read(team/research.txt)`, parent=first Agent ID |
| 29 | ToolResult에 runtime-only marker |
| 31 | Task notification completed + research result |
| 32 | parent Agent ToolResult + worker resolved model |

### 실제 handoff

Sequence 58의 두 번째 Agent input에는 다음 문장이 원문으로 들어갔습니다.

```text
RESEARCH_RESULT:CH20B_RUNTIME_69f13d30acdb420f
```

첫 worker의 sequence 24 prompt에는 이 값이 없었고 sequence 29 `Read` result와 sequence
32 첫 `Agent` result 뒤 sequence 58의 두 번째 `Agent` input에 나타났습니다. Sequence
31/32에서 첫 task가 완료된 다음 sequence 58에서 두 번째 Agent가 시작됐으므로, **첫
result 문자열이 leader lane을 거쳐 두 번째 input에 실린 순차 relay**는 관찰됐습니다.
그러나 initial leader context까지 값이 없었다는 인과는 과거 artifact의 source binding
부족 때문에 `accepted_with_notes`입니다.

### 두 번째 worker와 leader

| sequence | evidence |
| ---: | --- |
| 58 | `handoff-reviewer` Agent ToolUse, first result 포함 |
| 59 | second `TaskStartedMessage` |
| 65 | worker `Read(team/review.txt)`, parent=second Agent ID |
| 66 | review file ToolResult |
| 68 | Task notification completed + combined review result |
| 69 | parent Agent ToolResult + worker resolved model |
| 76/80 | leader synthesis와 successful Result |

최종 result에도 runtime marker와 review marker가 모두 남았습니다.

## 20b.4 무엇이 증명됐고 무엇이 아닌가

| 항목 | 분류 | 근거 |
| --- | --- | --- |
| 두 개의 서로 다른 worker 실행 | observed | 두 Agent ID와 task ID |
| 첫 결과의 두 번째 prompt 전달 | observed | sequence 32 대 58 원문 일치 |
| 두 worker의 순차 실행 | observed | first terminal 뒤 second Agent 시작 |
| 각 worker의 독립 Read | observed | 서로 다른 parent ID의 Read/ToolResult |
| leader의 최종 종합 | observed | sequence 76/80 |
| initial leader도 marker를 몰랐음 | inferred | 당시 initial prompt/probe hash 미보존 |
| worker 간 직접 메시지 | 미관찰 | worker-to-worker event 없음 |
| native `SendMessage` 실행 | 미관찰 | continuation 안내 문자열만 있고 ToolUse 없음 |
| `TeamCreate`/mailbox/UDS inbox | 미관찰 | 해당 ToolUse/event 없음 |
| shared TaskList claim loop | 미관찰 | claim/owner event 없음 |
| worktree isolation | 미관찰 | 별도 worktree 생성 없음 |
| team memory | 미관찰 | memory write/read 없음 |

따라서 이번 사례는 **leader-mediated multi-worker handoff**입니다. 교육적인 의미에서
팀 작업으로 보여 줄 수 있지만, Claude Code native Team/multiprocess 기능의 실행
증거로 이름을 바꾸면 안 됩니다.

또한 `provider_run_concurrency=1`과 foreground 설정은 실행 의도일 뿐입니다. 순차 실행
판정은 첫 terminal/result sequence 30~32가 두 번째 `Agent` sequence 58보다 앞선 실제
stream 순서에서 나옵니다.

## 20b.5 `SendMessage` 문자열을 실행으로 오판하지 않기

Agent ToolResult에는 worker를 계속할 때 사용할 수 있는 `SendMessage` 안내 문자열이
포함됐습니다. 그러나 이번 run에는 `SendMessage` ToolUse가 없습니다. UI는 다음을
구분해야 합니다.

```text
capability hint in ToolResult != observed SendMessage execution
```

문서에 도구명이 등장하거나 모델이 기능을 설명한 것만으로 실행된 edge를 만들지
않습니다.

## 20b.6 Python SDK 메시지 경계

이번 run에서 수신한 lifecycle class는 `TaskStartedMessage`,
`TaskProgressMessage`, `TaskUpdatedMessage`, `TaskNotificationMessage`입니다.
`SDKTask*Message`라는 Python class는 없습니다. 또한 current Python
`ClaudeAgentOptions`에는 `forwardSubagentText`와 `agentProgressSummaries` option이
없지만 nested worker 메시지는 `parent_tool_use_id`와 함께 전달됐습니다.

과거 probe manifest의 `actual_model`은 결과적으로 Opus 5였지만 당시 코드는
`SystemMessage.init.model`을 사용했습니다. 이번 판독은 sequence 9, 21, 28, 40, 45,
58, 65, 76의 `AssistantMessage.model`을 기준으로 다시 확정했습니다. 다만 sequence 80
`Result.model_usage`에는 `claude-haiku-4-5-20251001`도 있으므로 provider run 전체를
Opus-only라고 표현하지 않습니다.

## 20b.7 캔버스 표현

```text
Leader lane
  Agent A -> Agent A result
             |
             | exact runtime marker
             v
  Agent B prompt -> Agent B result
  -> Leader synthesis

Worker A lane: Read -> ToolResult
Worker B lane: handed-off prompt -> Read -> ToolResult
```

두 worker 사이에 직접 화살표를 그리면 안 됩니다. 실제 edge는 worker A result에서
leader로, leader의 두 번째 Agent input에서 worker B로 이어집니다.

OTel span도 raw SDK와 독립적인 두 번째 provider 증거가 아닙니다. 같은
`AttemptRecorder`가 SDK message 79개와 host process event 3개를 84개 span으로 투영한
것이므로, source sequence 정합성과 projector 무결성을 검증하는 관점으로 사용합니다.

## 20b.8 학생 실습

```text
두 read-only worker의 순차 handoff를 실행한다.

1. initial user/system/worker prompt와 probe source hash를 manifest에 묶고, 첫 worker가
   실행 중에만 알 수 있는 marker를 읽게 한다.
2. 첫 task terminal 이후 두 번째 Agent를 호출한다.
3. 두 번째 Agent input에 첫 결과 원문이 있는지 확인한다.
4. 각 nested tool의 parent_tool_use_id를 연결한다.
5. SendMessage나 native Team을 실제로 호출하지 않았다면 미관찰로 표시한다.
```

## Takeaway

이번 실제 run은 leader가 두 Opus 5 worker를 순차 실행하고, 첫 worker가 읽은 동적
결과 문자열을 두 번째 worker의 input에 넣은 사실을 증명했습니다. 다만 historical
artifact가 initial leader prompt와 probe source hash를 보존하지 않아 runtime-only
causality 전체는 추가 재실행이 필요합니다. worker 간 직접 통신, mailbox, claim loop,
worktree도 증명하지 않았습니다. 팀 시각화는 멋진 이름보다 실제 message edge의 방향을
따라야 합니다.
