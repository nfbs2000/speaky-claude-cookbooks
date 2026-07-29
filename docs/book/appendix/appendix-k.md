# 부록 K: Claude Code Fable 5 하니스 독해

이 페이지는 제3자 Claude Code Fable 5 캡처를 모델의 숨은 생각이 아니라
**코딩 제품이 모델에게 제공한 실행 하니스의 한 관측본**으로 읽는다.

## 구조 지도

| 층 | 학습 질문 |
| --- | --- |
| 정체성 | 일반 챗이 아니라 코딩 도우미라는 역할은 어디서 정해지는가 |
| Harness | 출력, 권한 거절, hook과 도구 선택을 어떻게 다루는가 |
| 소통 | 사용자에게 언제 진행과 결과를 보고하는가 |
| 세션 | 디렉터리, Git 상태, 지침과 날짜는 어떻게 붙는가 |
| Agent·Skill | 위임 가능한 역할과 절차를 모델이 어떻게 발견하는가 |
| Tool schema | 호출 조건과 결과 처리 규칙이 행동을 어떻게 유도하는가 |

## 읽어야 할 핵심

도구 schema는 함수 인자 목록에 그치지 않는다. 언제 호출해야 하는지, 거절이나 실패를
어떻게 해석하는지, 결과 뒤에 어떤 행동을 해야 하는지까지 적혀 있다면 작은 시스템
프롬프트로 작동한다. Agent와 Task 설명도 별도 오케스트레이터 상태 머신이 아니라
모델이 native 위임 표면을 선택하는 계약으로 읽어야 한다.

권한 거절은 도구 오류와 다르다. 사용자의 결정이므로 같은 요청을 그대로 반복하지 않고,
범위를 줄이거나 다른 방법을 제안해야 한다. hook output, tool result, 중간 system turn도
같은 채팅 문자열로 합치면 의미와 우선순위를 잃는다.

## SDK 실습

1. 최소 system prompt와 `claude_code` preset을 각각 사용한다.
2. 같은 모델, 같은 작업, 같은 도구 목록을 유지한다.
3. init metadata, assistant text, tool use/result와 final result를 저장한다.
4. agent 위임과 permission 거절을 각각 한 번 관찰한다.
5. 캡처에 문장이 있다는 사실과 실제 호출이 일어났다는 사실을 별도로 기록한다.

## 원문과 경계

- [Claude Code Fable 5 최신 캡처](https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/Claude%20Code/claude-code-fable-5.md)
- [강좌 분석 기준 고정본](https://github.com/asgeirtj/system_prompts_leaks/blob/48b9915063821f33489ff7da21ca448835bdd15b/Anthropic/Claude%20Code/claude-code-fable-5.md)
- [Claude Agent SDK 마이그레이션](https://platform.claude.com/docs/en/agent-sdk/migration-guide)

캡처 전체를 공식 Claude Code 사양으로 선언하지 않는다. 이 페이지의 결론은 캡처의
구조로 실험 질문을 만들고, 현재 SDK 실행에서 다시 확인하라는 것이다.
