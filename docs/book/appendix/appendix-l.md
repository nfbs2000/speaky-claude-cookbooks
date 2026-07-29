# 부록 L: Fable 5와 Opus 5를 공정하게 비교하기

모델 비교는 이름이 다른 두 프롬프트 파일의 길이를 비교하는 작업이 아니다.
claude.ai 캡처와 Claude Code 캡처를 먼저 분리하고, 모델 차이와 제품 하니스 차이를
각각 통제해야 한다.

## 비교를 오염시키는 변수

- 서로 다른 제품 표면
- 캡처 날짜와 Claude Code 버전
- tool schema, agent와 skill 목록
- 사용자 지침과 MCP
- permission mode와 working directory
- 모델 외에 함께 바뀐 system prompt

## 세 가지 실험

| 실험 | 고정할 것 | 바꿀 것 |
| --- | --- | --- |
| 모델 비교 | SDK 버전, prompt, tools, task | model ID |
| 하니스 비교 | model, tools, task | 최소 prompt와 Claude Code preset |
| 제품 캡처 비교 | 제품·버전·캡처 조건 | 인접 캡처 파일 |

각 실행에서는 최종 답변만 비교하지 않는다. tool 선택, 호출 순서, permission 처리,
완료 상태, token/latency와 사람이 검토한 결과 품질을 함께 기록한다. 한 번의 결과를
모델 고유 성향으로 일반화하지 않는다.

## 공개 원문

- [claude.ai Fable 5 캡처](https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/claude-fable-5.md)
- [claude.ai Opus 5 캡처](https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/claude-opus-5.md)
- [Claude Code Fable 5 캡처](https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/Claude%20Code/claude-code-fable-5.md)
- [Claude Code Opus 5 캡처](https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/Claude%20Code/claude-code-opus-5.md)

좋은 결론은 “어느 모델이 더 낫다”가 아니라 “통제된 조건에서 무엇이 관찰됐고,
어떤 변수는 아직 분리하지 못했는가”를 말한다.
