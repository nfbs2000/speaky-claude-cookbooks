# 부록 J: 비공식 시스템 프롬프트 자료를 읽는 법

이 페이지는 제3자가 수집한 시스템 프롬프트를 사실의 최종 원전으로 오해하지 않고,
Claude Agent SDK 수업의 조사 자료로 사용하는 공개판이다. 긴 파일을 번역하기 전에
먼저 제품, 모델, 캡처 시점, 도구, 동적 컨텍스트를 구분해야 한다.

## 출처 등급

| 등급 | 확인할 수 있는 것 | 남는 한계 |
| --- | --- | --- |
| 공식 문서 | SDK 옵션, 메시지, 도구와 hook 계약 | Claude Code 내부 조립 전체는 아님 |
| 공식 프롬프트 릴리스 | claude.ai의 공개 행동 지침 | Claude Code와 동일하다는 뜻은 아님 |
| 제3자 캡처 | 특정 환경에서 수집된 제품 입력 구조 | 모든 계정과 버전에 일반화할 수 없음 |
| 직접 실행 | 현재 SDK 세션에 나타난 실제 이벤트 | 보이지 않는 내부 인과는 확정할 수 없음 |

## 네 표면을 섞지 않는다

1. Anthropic이 공개한 기본 행동 프롬프트
2. claude.ai 제품 캡처
3. Claude Code 코딩 하니스 캡처
4. Agent SDK가 공개한 실행 계약

같은 모델 이름이 붙어 있어도 네 표면은 서로 다른 도구와 컨텍스트를 가질 수 있다.
따라서 분석 문장은 `공식`, `수집본 관찰`, `실행 관찰`, `해석`, `미확인` 중 하나로
표시한다.

## 조사 순서

1. README와 파일 경로에서 제품 표면을 확인한다.
2. 모델·제품 버전과 캡처 조건을 기록한다.
3. 기본 행동, 세션 컨텍스트, 도구, agent, skill, reminder를 분리한다.
4. 공식 SDK 문서에서 같은 계약을 찾는다.
5. 새 SDK 세션에서 한 변수만 바꾸고 raw event를 저장한다.
6. 문서의 예상과 실제 관찰을 대조하되, 관찰되지 않은 인과는 남겨 둔다.

## 공개 자료

- [Anthropic 시스템 프롬프트 릴리스 노트](https://platform.claude.com/docs/en/release-notes/system-prompts)
- [Claude Agent SDK 개요](https://platform.claude.com/docs/en/agent-sdk/overview)
- [Anthropic 자료 캡처 모음](https://github.com/asgeirtj/system_prompts_leaks/tree/main/Anthropic)
- [Claude Code 캡처 분류](https://github.com/asgeirtj/system_prompts_leaks/tree/main/Anthropic/Claude%20Code)
- [Claude Agent SDK TypeScript](https://github.com/anthropics/claude-agent-sdk-typescript)

전체 제3자 문서를 재게시하지 않는다. 학생은 원문 링크를 직접 열고, 이 공개판에서는
출처 판별법과 실행으로 검증할 수 있는 질문을 배운다.
