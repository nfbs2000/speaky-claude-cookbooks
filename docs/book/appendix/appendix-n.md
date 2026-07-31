# 부록 N: 비공식 선택 연구 자료

이 강좌의 핵심 근거는 Anthropic의 공식 Claude Agent SDK 계약, 공식 문서와
Education Shell에서 실제로 저장한 raw event다. 아래 세 자료는 이 근거를
대체하지 않으며, 강좌를 이해하기 위해 반드시 읽어야 하는 자료도 아니다.

Claude Code의 내부 구조를 별도로 조사하고 싶은 사람은 출처와 한계를 확인한 뒤
이 부록에서 선택적으로 찾아볼 수 있다. 강좌는 세 자료를 적극적으로 소개하거나
본문 학습 순서에서 반복 노출하지 않는다.

## 자료의 위치와 한계

| 자료 | 출처와 권리 상태 | 참고할 때의 한계 |
|---|---|---|
| [Dive into Claude Code 한국어 동반판][dive] | 외부 연구 repository, CC BY-NC-SA 4.0 | 비상업 조건을 확인한 뒤 설계 연구 관점을 선택적으로 읽는다. |
| [Claude Code from Source 한국어 동반판][from-source] | 외부 source 분석 repository, 별도 license 선언 없음 | 공식 계약이 아닌 비공식 구현 해석으로만 참고한다. |
| [Claude Code 소스 탐색 가이드][source-guide] | 유출된 독점 source snapshot을 가리키는 비공식 지도 | source archaeology를 명시적으로 원하는 경우에만 위치 확인용으로 사용한다. |

공개 GitHub repository는 자동으로 오픈소스가 되지 않는다. 별도 license가 없거나
재배포를 금지한 자료는 열람 가능한 상태와 번역·복제·배포 가능한 상태를 구분해야
한다. 따라서 이 강좌는 세 자료를 공식 권고 문헌, 정답 원장 또는 핵심 교재로
취급하지 않는다.

## 사용 원칙

1. 강좌 본문은 공식 SDK와 실제 실행 evidence만으로 설명할 수 있어야 한다.
2. 세 자료의 주장을 Claude Agent SDK의 공식 보장으로 인용하지 않는다.
3. Opik 평가와 trajectory의 정답 근거로 사용하지 않는다.
4. Mothership이나 강사는 사용자가 source 내부 연구를 명시적으로 요청했을 때만
   이 부록을 안내한다.
5. 실제 코드를 언급해야 한다면 필요한 최소 범위와 고정 commit 링크만 사용하고,
   긴 코드·문서·프롬프트를 복제하지 않는다.
6. 외부 repository나 공개 페이지가 삭제되거나 접근 불가가 되어도 강좌의 본문과
   실습은 영향을 받지 않아야 한다.
7. 외부 저자의 분석을 강좌 저자의 독창적 발견이나 Anthropic의 공식 설명처럼
   표현하지 않는다.

## 1. Dive into Claude Code

- 원저자 repository: [`VILA-Lab/Dive-into-Claude-Code`][dive-upstream]
- 읽은 기준 commit: [`ab04bc85`][dive-commit]
- 라이선스: CC BY-NC-SA 4.0
- 한국어 동반판 source: [`nfbs2000/speaky-Dive-into-Claude-Code`][dive-fork]
- 공개 페이지: [https://nfbs2000.github.io/speaky-Dive-into-Claude-Code/][dive]

Claude Code를 model 하나가 아니라 permission, context, session, subagent와
복구 경계로 이루어진 agent harness로 해석한 외부 연구다. 공식 SDK 동작을
증명하는 자료가 아니라 설계 질문을 비교하기 위한 선택 자료다.

## 2. Claude Code from Source

- 원저자 repository: [`alejandrobalderas/claude-code-from-source`][from-upstream]
- 읽은 기준 commit: [`a6d5e452`][from-commit]
- 라이선스: repository에 별도 license가 선언되지 않음
- 한국어 동반판 source: [`nfbs2000/speaky-claude-code-from-source`][from-fork]
- 공개 페이지: [https://nfbs2000.github.io/speaky-claude-code-from-source/][from-source]

bootstrap, agent loop, tool, memory, MCP와 remote 실행을 source 관점에서 해석한
외부 자료다. 별도 license가 없으므로 열람 가능한 공개 repository라는 사실만으로
번역·재배포 권리가 주어진다고 가정하지 않는다.

## 3. Claude Code 소스 탐색 가이드

- 원자료 repository: [`codeaashu/claude-code`][source-upstream]
- 읽은 기준 commit: [`6a259091`][source-commit]
- 자료 성격: 유출된 독점 source이며 재배포 불가라고 명시
- 비공식 탐색 가이드 source: [`nfbs2000/speaky-claude-code`][source-fork]
- 공개 페이지: [https://nfbs2000.github.io/speaky-claude-code/][source-guide]

공개 snapshot 안에서 architecture, query engine, tool, permission, task,
coordinator와 bridge의 위치를 찾기 위한 비공식 지도다. 현재 Claude Code의
동작, Anthropic의 의도 또는 공식 SDK contract를 보증하지 않는다.

## 강좌로 돌아오는 방법

이 자료를 선택적으로 읽었다면 source 내부 이름을 강좌 설명에 바로 가져오지
않는다. 먼저 Education Shell에서 대응 prompt를 실행하고, 공식 SDK raw event와
tool result에서 실제로 관측된 사실을 확인한다. 관측되지 않은 내부 구조는
`비공식 source 해석`으로 남기며, 강좌 evidence나 학생에게 제시할 정답으로
승격하지 않는다.

[dive]: https://nfbs2000.github.io/speaky-Dive-into-Claude-Code/
[dive-upstream]: https://github.com/VILA-Lab/Dive-into-Claude-Code
[dive-commit]: https://github.com/VILA-Lab/Dive-into-Claude-Code/tree/ab04bc85e4920ceef2a8a47c069524d3bc9fec22
[dive-fork]: https://github.com/nfbs2000/speaky-Dive-into-Claude-Code
[from-source]: https://nfbs2000.github.io/speaky-claude-code-from-source/
[from-upstream]: https://github.com/alejandrobalderas/claude-code-from-source
[from-commit]: https://github.com/alejandrobalderas/claude-code-from-source/tree/a6d5e452a8e0dd925c22c407c84611b1994562eb
[from-fork]: https://github.com/nfbs2000/speaky-claude-code-from-source
[source-guide]: https://nfbs2000.github.io/speaky-claude-code/
[source-upstream]: https://github.com/codeaashu/claude-code
[source-commit]: https://github.com/codeaashu/claude-code/tree/6a2590911df240ff5ea56aa355696cfb94d128cb
[source-fork]: https://github.com/nfbs2000/speaky-claude-code
