# 책 본문

이 섹션은 한국어 Claude Agent SDK 책의 장 구조를 유지하면서, 각 장을 공개 Python cookbook과 공식 SDK 문서에 맞춰 다시 쓴 공개판입니다.

1장은 수동으로 상세 작성했고, 나머지 장은 `docs/data/book_projection.yml`의 근거와 원문 절 구조를 기반으로 생성했습니다. 각 장은 cookbook 링크, 공식 문서 링크, 공개 경계, 실습 방향을 함께 제공합니다.

## 제1부: 아키텍처

- [1장: AI 코딩 에이전트의 전체 기술 스택](part1/ch01.md)
- [2장: 도구 시스템 - 모델의 손이 되는 40개 이상의 도구](part1/ch02.md)
- [3장: 에이전트 루프 - 사용자 입력에서 모델 응답까지의 전체 생명주기](part1/ch03.md)
- [4장: 도구 실행 오케스트레이션 - 권한, 동시성, 스트리밍, 인터럽트](part1/ch04.md)
- [4b장: 플랜 모드 - 뛰기 전에 살펴보기](part1/ch04b.md)

## 제2부: 프롬프트 엔지니어링

- [5장: 시스템 프롬프트 아키텍처](part2/ch05.md)
- [6장: 프롬프트를 통한 동작 제어](part2/ch06.md)
- [6b장: API 통신 계층 - 재시도, 스트리밍, 성능 저하 대응](part2/ch06b.md)
- [7장: 모델별 튜닝과 A/B 테스트](part2/ch07.md)
- [8장: 마이크로 하니스로서의 도구 프롬프트](part2/ch08.md)
- [8c장: 정적 시스템 프롬프트 - SDK에서 보이는 기본 성격](part2/ch08c.md)
- [8d장: 동적 프롬프트 레이어 - 세션, 메모리, 팀, MCP가 뒤에 붙는 법](part2/ch08d.md)
- [8e장: 도구 설명 프롬프트 - Bash, Read, Grep, Agent는 어떻게 행동을 유도하나](part2/ch08e.md)
- [8f장: 권한/분류기 프롬프트 - 자동 승인, CLAUDE.md prefix, deny 규칙의 숨은 제어 평면](part2/ch08f.md)

## 제3부: 세션과 메시지 관측

- [9장: 자동 컴팩션 - 언제, 어떻게 컨텍스트가 압축되는가](part3/ch09.md)
- [10장: 컴팩션 이후의 파일 상태 보존](part3/ch10.md)
- [11장: 마이크로 컴팩션 - 정밀한 컨텍스트 가지치기](part3/ch11.md)
- [12장: 토큰 예산 전략](part3/ch12.md)

## 제4부: 프롬프트 캐싱

- [13장: 캐시 아키텍처와 브레이크포인트 설계](part4/ch13.md)
- [14장: 캐시 브레이크 감지 시스템](part4/ch14.md)
- [15장: 캐시 최적화 패턴](part4/ch15.md)

## 제5부: 안전성과 권한

- [16장: 권한 시스템](part5/ch16.md)
- [17장: YOLO 분류기](part5/ch17.md)
- [17b장: 프롬프트 인젝션 방어](part5/ch17b.md)
- [18장: 훅 - 사용자 정의 가로채기 지점](part5/ch18.md)
- [18b장: 샌드박스 시스템 - 격리된 실행 환경](part5/ch18b.md)
- [19장: CLAUDE.md - 사용자 지침의 오버라이드 계층](part5/ch19.md)

## 제6부: 고급 서브시스템

- [20장: 에이전트 생성과 오케스트레이션](part6/ch20.md)
- [20b장: 팀과 멀티프로세스 협업](part6/ch20b.md)
- [20c장: Ultraplan - 원격 멀티 에이전트 계획 수립](part6/ch20c.md)
- [21장: Effort, Fast Mode, 그리고 Thinking](part6/ch21.md)
- [22장: Skills 시스템 - 기본 제공에서 사용자 정의까지](part6/ch22.md)
- [22b장: 플러그인 시스템 - 패키징에서 마켓플레이스 확장 엔지니어링까지](part6/ch22b.md)
- [23장: 비공개 기능 파이프라인 - 기능 플래그와 재현 조건](part6/ch23.md)
- [23b장: 기능 플래그의 생명주기 - 실험에서 재현 조건까지](part6/ch23b.md)
- [24장: 세션 간 메모리 - 망각에서 지속적 학습으로](part6/ch24.md)

## 제7부: AI 에이전트 구축자를 위한 교훈

- [25장: 하니스 엔지니어링 원칙](part7/ch25.md)
- [26장: 핵심 역량으로서의 세션과 메시지 관측](part7/ch26.md)
- [27장: 프로덕션급 AI 코딩 패턴](part7/ch27.md)
- [28장: Claude Code의 한계](part7/ch28.md)
- [29장: 옵저버빌리티 엔지니어링 - logEvent에서 프로덕션급 텔레메트리까지](part7/ch29.md)
- [30장: 나만의 AI 에이전트 만들기 - Claude Code 패턴에서 실전까지](part7/ch30.md)

## 부록

- [부록 A: 주요 파일 인덱스](appendix/appendix-a.md)
- [부록 B: 환경 변수 참조](appendix/appendix-b.md)
- [부록 C: 용어집](appendix/appendix-c.md)
- [부록 D: 기능 플래그 전체 목록](appendix/appendix-d.md)
- [부록 E: 버전 진화 로그](appendix/appendix-e.md)
- [부록 F: 엔드투엔드 사례 추적](appendix/appendix-f.md)
- [부록 G: 인증 및 구독 시스템](appendix/appendix-g.md)
- [부록 H: 프롬프트 표면 인덱스](appendix/appendix-h.md)
- [부록 I: 강좌 플러그인 배포 청사진](appendix/appendix-i.md)
