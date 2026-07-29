# 부록 M: 시스템 프롬프트 버전 진화 지도

시스템 프롬프트의 역사는 모델 가중치, claude.ai 제품 prompt, Claude Code 하니스,
도구와 동적 주입 채널의 변화를 분리해서 읽어야 한다.

## 변화의 네 축

1. 모델 metadata와 fixed snapshot
2. claude.ai가 공개한 행동 프롬프트
3. Claude Code의 full/lean 하니스
4. tools, agents, skills와 reminder의 주입 위치

2024년의 짧은 공개 행동 프롬프트가 실제 제품 요청 전체였다고 단정할 수 없다.
2025년 이후 공개본이 길어진 것은 제품 행동 계약이 더 구체화됐다는 증거지만,
모델 능력 변화와 같은 뜻은 아니다. Claude Code 캡처의 길이 변화도 tool schema나
동적 목록 이동을 먼저 분리해야 해석할 수 있다.

## 버전 비교 절차

1. 공식 공개 날짜와 model ID를 기록한다.
2. 제3자 캡처 commit과 제품 버전을 기록한다.
3. 기본 행동, session context, tools, agents, skills를 별도 비교한다.
4. model string만 바뀐 diff를 분리한다.
5. 같은 SDK 설정으로 실행하고 raw event를 저장한다.
6. 예상과 관찰을 연결하되 원인을 과장하지 않는다.

## 정확한 결론의 예

- 공식 claude.ai 행동 프롬프트가 바뀌었다.
- Claude Code 기본 하니스가 full에서 lean으로 바뀌었다.
- agent·skill 목록의 주입 channel이 바뀌었다.
- 같은 실행 계약에서 model만 바꿨을 때 관찰 결과가 달라졌다.

## 공개 자료

- [Anthropic 공식 시스템 프롬프트 변경 기록](https://platform.claude.com/docs/en/release-notes/system-prompts)
- [공식 공개본 아카이브 고정본](https://github.com/asgeirtj/system_prompts_leaks/blob/48b9915063821f33489ff7da21ca448835bdd15b/Anthropic/Official/README.md)
- [Claude Code 캡처 분류 고정본](https://github.com/asgeirtj/system_prompts_leaks/blob/48b9915063821f33489ff7da21ca448835bdd15b/Anthropic/Claude%20Code/README.md)

버전 진화는 긴 프롬프트를 구경하는 일이 아니라, 어떤 실행 변수가 어느 시점에
바뀌었고 그 변화가 현재 SDK에서 관찰 가능한지를 추적하는 작업이다.
