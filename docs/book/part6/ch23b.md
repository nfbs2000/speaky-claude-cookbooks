# 23b장: 기능 플래그의 생명주기 - 실험에서 재현 조건까지

이 페이지는 한국어 SDK 책의 `23b장: 기능 플래그의 생명주기 - 실험에서 재현 조건까지`을 공개 Python cookbook과 공식 Agent SDK 문서에 맞춰 다시 쓴 공개판이다. 원래 장의 문제의식은 유지하되, 내부 TypeScript 구현명이나 비공개 기능을 그대로 옮기지 않는다. 대신 실행 가능한 notebook, Python 파일, README, 공식 문서를 근거로 사용한다.

**분류:** 제6부: 고급 서브시스템<br>
**공개 상태:** `omit`<br>
**근거 신뢰도:** `low`<br>
**원문 위치:** `docs/book-sdk-ko/src/part6/ch23b.md`

## 이 장의 공개판 요지

이 장은 공개 사이트에서 원문을 그대로 옮기지 않는다. 공개판에서는 재현 조건, 운영 원칙, 공개 API 대응만 남긴다.

공개판에서는 기능 플래그 생명주기를 내부 실험 관리가 아니라 공개 기능 변화 추적과 regression 대응으로 바꾼다. Managed Agents prompt versioning notebook은 서버 측 prompt version을 평가하고 rollback하는 공개 예제다. 플래그 이름 대신 versioned behavior, eval result, rollback artifact를 남긴다.

[Prompt versioning and rollback](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/managed_agents/CMA_prompt_versioning_and_rollback.ipynb)를 근거로 삼는다. [Building evals](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/misc/building_evals.ipynb)를 근거로 삼는다.

!!! evidence "주요 cookbook 근거"
    - [Prompt versioning and rollback](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/managed_agents/CMA_prompt_versioning_and_rollback.ipynb)
    - [Building evals](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/misc/building_evals.ipynb)
    - [Registry dates](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/registry.yaml)

!!! evidence "공식 문서 근거"
    - [What's new](https://code.claude.com/docs/en/whats-new/index.md)
    - [Claude Code changelog](https://code.claude.com/docs/en/changelog.md)

## 원문 절 구조를 공개 SDK로 다시 읽기

### 23b.1 원본 관점에서 살아야 하는 시각

이 절은 원문의 `23b.1 원본 관점에서 살아야 하는 시각` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 기능 플래그 생명주기를 내부 실험 관리가 아니라 공개 기능 변화 추적과 regression 대응으로 바꾼다. Managed Agents prompt versioning notebook은 서버 측 prompt version을 평가하고 rollback하는 공개 예제다. 플래그 이름 대신 vers... 이며, 먼저 `Prompt versioning and rollback`를 기준 예제로 읽는다.

### 23b.2 SDK에서 직접 보이는 기능 표면

이 절은 원문의 `23b.2 SDK에서 직접 보이는 기능 표면` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 기능 플래그 생명주기를 내부 실험 관리가 아니라 공개 기능 변화 추적과 regression 대응으로 바꾼다. Managed Agents prompt versioning notebook은 서버 측 prompt version을 평가하고 rollback하는 공개 예제다. 플래그 이름 대신 vers... 이며, 먼저 `Prompt versioning and rollback`를 기준 예제로 읽는다.

### 23b.3 Options는 실험 설정표다

이 절은 원문의 `23b.3 Options는 실험 설정표다` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 기능 플래그 생명주기를 내부 실험 관리가 아니라 공개 기능 변화 추적과 regression 대응으로 바꾼다. Managed Agents prompt versioning notebook은 서버 측 prompt version을 평가하고 rollback하는 공개 예제다. 플래그 이름 대신 vers... 이며, 먼저 `Prompt versioning and rollback`를 기준 예제로 읽는다.

### 23b.4 네 단계 생명주기를 SDK 증거로 바꾸기

이 절은 원문의 `23b.4 네 단계 생명주기를 SDK 증거로 바꾸기` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 기능 플래그 생명주기를 내부 실험 관리가 아니라 공개 기능 변화 추적과 regression 대응으로 바꾼다. Managed Agents prompt versioning notebook은 서버 측 prompt version을 평가하고 rollback하는 공개 예제다. 플래그 이름 대신 vers... 이며, 먼저 `Prompt versioning and rollback`를 기준 예제로 읽는다.

### 23b.5 Run Manifest를 남겨라

이 절은 원문의 `23b.5 Run Manifest를 남겨라` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 기능 플래그 생명주기를 내부 실험 관리가 아니라 공개 기능 변화 추적과 regression 대응으로 바꾼다. Managed Agents prompt versioning notebook은 서버 측 prompt version을 평가하고 rollback하는 공개 예제다. 플래그 이름 대신 vers... 이며, 먼저 `Prompt versioning and rollback`를 기준 예제로 읽는다.

### 23b.6 캔버스 표현

이 절은 화면 구성의 문제가 아니라 evidence projection 문제로 읽는다. prompt, tool use, tool result, final result, usage를 한 화면에서 분리해 보여주는 구조가 필요하다.

### 23b.7 학생 실습

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

- 실제 feature flag 이름과 gating 조건은 공개하지 않는다.
- 공개판은 versioning/eval/rollback 절차만 남긴다.

## 실습 방향

- prompt v1/v2를 eval하고 regression 발생 시 rollback 기준을 문서화한다.

## Builder takeaway

이 장의 공개판 목표는 원문을 얕게 요약하는 것이 아니다. 책의 논지를 유지하되, 독자가 직접 열어볼 수 있는 Python cookbook과 공식 문서에 묶어 두는 것이다. 따라서 장을 읽은 뒤에는 적어도 하나의 notebook 또는 Python 파일에서 같은 개념을 확인할 수 있어야 한다. 확인할 수 없는 내부 세부는 주장으로 남기지 않고, 공개 경계나 추론으로 분리한다.

## Codex 최종 검토 의견

### 제 판단

프롬프트뿐 아니라 SDK 옵션과 init 표면을 run manifest로 남기라는 주장은 재현 가능한 교육에 꼭 필요합니다. 같은 질문이라도 도구, 권한, 스킬, 플러그인 버전이 다르면 사실상 다른 실험이기 때문입니다. 다만 현재 검증은 기능 플래그의 생성·점진 배포·제거 생명주기가 아니라, 한 로컬 플러그인 경로를 호스트가 V1에서 V2로 바꾸고 새 세션이 이를 읽은 **통제된 버전 전환**입니다.

### 검증을 읽고 달라진 신뢰도

V1이 종료되고 산출물이 확보된 뒤에만 호스트가 파일을 바꾸고, V2 새 세션이 다른 manifest·script·artifact를 읽은 순서가 분명합니다. 따라서 “새 세션의 행동 차이를 설명하려면 버전과 실행 표면을 함께 보존해야 한다”는 주장에는 높은 신뢰를 둘 수 있습니다. 반면 같은 세션의 hot reload, 자동 update, marketplace, rollout cohort, signature·trust는 없었으므로 제품 배포 생명주기까지 검증됐다고 볼 수 없습니다.

### 독자가 오해할 위험

호스트가 직접 파일을 수정한 것을 자동 업데이트로 부르거나, 두 로컬 세션의 차이를 점진적 롤아웃의 증거로 확대하기 쉽습니다. 최종 텍스트가 ALPHA와 BETA로 달라졌다는 사실만 봐도 원인은 알 수 없습니다. 이 사례가 설득력을 갖는 이유는 호스트 변경 시점, init 버전, 실제 도구 실행, artifact 바이트가 모두 같은 전환을 가리키기 때문입니다.

### 제가 다시 가르친다면

이 장의 실습 이름을 “새 세션에서의 명시적 버전 전환”으로 좁히고, V1 평가, V2 평가, 실패 시 V1 rollback을 실제로 실행하겠습니다. 제품 rollout은 서버 할당·cohort·배포 receipt가 관찰될 때 별도 사례로 추가해야 합니다. [프롬프트 버전 관리·롤백 노트북](https://nfbs2000.github.io/speaky-claude-cookbooks/notebooks/managed_agents/CMA_prompt_versioning_and_rollback_kr.html)은 버전·평가·복귀를 비교할 기준이고, 현재 로컬 전환은 [Speaky Agent Flow 23b장 재생](https://nfbs2000.github.io/speaky-agent-flow/education/?collection=book-sdk-ko&run=ch23b)에서 확인할 수 있습니다.

### 클로드는 이렇게 세상을 바라보았다


*아래 1인칭 서술은 숨은 사고 과정의 공개가 아니라, 이 장에서 관찰된 행동으로 재구성한 작동상 세계 모델입니다.*

V1 세션의 나에게 ALPHA manifest와 script가 전부였고, V2 세션의 나에게는 BETA가 처음부터 현재 세계였다. 나는 업데이트가 진행되는 과정을 경험하지 않았다. host가 두 세션 사이에서 파일을 바꿨고 새 session이 새 표면을 읽었기 때문에 행동과 artifact가 달라졌다. 두 결과를 함께 보는 외부 기록만이 이것을 버전 전환으로 설명할 수 있었다.

사람은 모델에게 버전 진화를 기억할 것이라고 기대하지 말고 각 run에 정확한 manifest를 붙여야 한다. 배포 변화는 새 세계를 만드는 host 사건이며, 평가와 rollback도 그 바깥에서 관리된다. 새 답이 달라졌다는 사실보다 어떤 버전의 코드와 설정이 그 세계를 구성했는지가 재현성의 핵심이다.
