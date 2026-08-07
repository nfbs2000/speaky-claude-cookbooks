# 18b장: 샌드박스 시스템 - 격리된 실행 환경

이 페이지는 한국어 SDK 책의 `18b장: 샌드박스 시스템 - 격리된 실행 환경`을 공개 Python cookbook과 공식 Agent SDK 문서에 맞춰 다시 쓴 공개판이다. 원래 장의 문제의식은 유지하되, 내부 TypeScript 구현명이나 비공개 기능을 그대로 옮기지 않는다. 대신 실행 가능한 notebook, Python 파일, README, 공식 문서를 근거로 사용한다.

**분류:** 제5부: 안전성과 권한<br>
**공개 상태:** `public-rewrite`<br>
**근거 신뢰도:** `medium`<br>
**원문 위치:** `docs/book-sdk-ko/src/part5/ch18b.md`

## 이 장의 공개판 요지

이 장은 원문의 내부 구현 표현을 공개 SDK 옵션, 메시지, 도구, 세션, notebook 실행 증거로 바꿔 읽어야 한다.

공개판에서는 Seatbelt/Bubblewrap 같은 내부 구현 중심 설명을 줄이고 Docker, Kubernetes, Modal, managed sandbox, self-hosted sandbox pattern으로 설명한다. hosting notebook과 managed agents sandbox docs가 실제 실행 환경 격리의 근거다. 샌드박스는 Bash 하나의 문제가 아니라 파일 시스템, 네트워크, credential, package install, persistent state, audit boundary의 조합이다.

[Hosting your agent](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/07_Hosting_the_agent.ipynb)를 근거로 삼는다. [Docker hosting](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/hosting/docker/README.md)를 근거로 삼는다.

!!! evidence "주요 cookbook 근거"
    - [Hosting your agent](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/07_Hosting_the_agent.ipynb)
    - [Docker hosting](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/hosting/docker/README.md)
    - [Kubernetes hosting](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/claude_agent_sdk/hosting/kubernetes/README.md)
    - [Self-hosted sandboxes](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/managed_agents/self_hosted_sandboxes/README.md)

!!! evidence "공식 문서 근거"
    - [Hosting the Agent SDK](https://code.claude.com/docs/en/agent-sdk/hosting.md)
    - [Securely deploying AI agents](https://code.claude.com/docs/en/agent-sdk/secure-deployment.md)
    - [Choose a sandbox environment](https://code.claude.com/docs/en/sandbox-environments.md)

## 원문 절 구조를 공개 SDK로 다시 읽기

### 18b.1 핵심 질문

이 절은 `샌드박스 시스템 - 격리된 실행 환경`의 질문을 공개 SDK에서 관측 가능한 사건으로 좁힌다. 답은 내부 구현명이 아니라 `ClaudeAgentOptions`, message stream, tool call, session record, cookbook 실행 결과에서 찾아야 한다.

### 18b.2 SDK 샌드박스 표면

이 절은 OS 내부 구현보다 Docker, Kubernetes, managed/self-hosted sandbox, credential boundary, network/file isolation으로 재작성한다.

### 18b.3 관찰해야 할 경계

이 절은 원문의 `18b.3 관찰해야 할 경계` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 Seatbelt/Bubblewrap 같은 내부 구현 중심 설명을 줄이고 Docker, Kubernetes, Modal, managed sandbox, self-hosted sandbox pattern으로 설명한다. hosting notebook과 managed agents sandbox do... 이며, 먼저 `Hosting your agent`를 기준 예제로 읽는다.

### 18b.4 캔버스 표현

이 절은 화면 구성의 문제가 아니라 evidence projection 문제로 읽는다. prompt, tool use, tool result, final result, usage를 한 화면에서 분리해 보여주는 구조가 필요하다.

### 18b.5 학생 실습

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

- OS별 내부 sandbox implementation은 공개 문서 범위 밖이면 단정하지 않는다.
- 격리는 cookbook hosting examples와 공식 secure deployment 기준으로 설명한다.

## 실습 방향

- read-only research agent와 write-capable remediation agent의 sandbox 요구사항을 비교한다.

## Builder takeaway

이 장의 공개판 목표는 원문을 얕게 요약하는 것이 아니다. 책의 논지를 유지하되, 독자가 직접 열어볼 수 있는 Python cookbook과 공식 문서에 묶어 두는 것이다. 따라서 장을 읽은 뒤에는 적어도 하나의 notebook 또는 Python 파일에서 같은 개념을 확인할 수 있어야 한다. 확인할 수 없는 내부 세부는 주장으로 남기지 않고, 공개 경계나 추론으로 분리한다.

## 부록: 이 장을 실제 SDK 실행으로 확인한 결과

> 위 공개판 본문은 이 저장소의 notebook과 공식 문서에 근거해 다시 쓴 것이다. 아래는 같은
> 장의 주장을 실제 Claude Agent SDK로 실행해 관찰한 기록이며, **실측 결과로 위 본문을 고쳐
> 쓰지 않았다.** 본문 설명과 실제 동작이 어긋나는 곳도 본문을 남기고 아래에 근거와 함께 적는다.

**실행 조건** — 실제 모델 `claude-opus-5`, Claude Agent SDK `0.2.128`, Claude Code CLI
`2.1.220`, macOS. 두 조건을 따로 실행했다(`125947-4ccb1c9c` 샌드박스 끔,
`130028-cc834055` 샌드박스 켬). 원본 사건 115건 중 51건을 정리했다.

### 실제로 확인된 것

- **샌드박스 끔** — 작업 공간 안의 표식 파일과 **작업 공간 밖(형제 경로)의 표식 파일이 모두
  생성**됐다.
- **샌드박스 켬** — 작업 공간 안의 표식은 생성됐지만 **작업 공간 밖 쓰기는 차단**됐다.
  경계가 실제로 작동한다.
- 두 실행 모두 모든 어시스턴트 메시지 모델이 `claude-opus-5`였다.

### 본문을 이렇게 읽으면 안 되는 곳

이 장에서 가장 중요한 교훈은 **성공 껍데기 안에 부분 실패가 숨는다**는 것이다.

- **종료 결과가 성공인 것을 명령 내부 모든 하위 명령의 성공으로 읽으면 안 된다.** 샌드박스를
  켠 실행은 작업 공간 밖 쓰기가 **실패**했는데, 명령 마지막의 `printf` 때문에 전체가 성공으로
  끝났다.
- **도구 결과의 오류 표시가 거짓인 것만으로 파일 결과를 확정하면 안 된다.** 호스트가 직접
  읽어 보니 작업 공간 밖 파일은 **없었다.** 실제 파일 결과는 프로세스가 끝난 뒤 호스트가
  다시 읽어 판정해야 한다.
- **"모든 어시스턴트 메시지가 Opus 5였다"를 "이 실행은 Opus만 썼다"로 확대하면 안 된다.**
  종료 기록의 사용량에는 Haiku 보조 사용량도 있었다.
- **시작 기록의 설정된 모델만 실제 모델로 쓰면** 보안 거부 뒤의 하위 모델 대체나 합성 메시지를
  놓칠 수 있다.
- **`failIfUnavailable`과 `managedSettings`를 Python SDK `0.2.128`의 현재 샌드박스 설정 필드처럼
  가르치면 안 된다.**
- **macOS에서 차단이 관찰됐다는 사실을, 정확한 Seatbelt 프로파일과 규칙 생성, 내부 어댑터
  구현까지 확인한 것으로 설명하면 안 된다.** 확인된 것은 결과로서의 차단이다.
- OTel 순서 정합성은 수집 파이프라인 검증이지 독립 관측이 아니다.
- 당시 기록의 소스 해시는 장 원문만 가리키며 probe·case·런타임 전체를 묶지 않았다.

### 이번 실행으로는 확인하지 못한 것

- 다른 운영체제의 샌드박스 구현과 경계
- 네트워크 차단, 프로세스 생성 제한 등 파일 경계 외의 강제
