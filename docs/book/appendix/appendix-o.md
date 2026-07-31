# 부록 O: TradingAgents 멀티에이전트 금융 워크플로 읽기

[TradingAgents 한국어 소스 해설](https://nfbs2000.github.io/speaky-TradingAgents/)은
금융 분석가, 강세·약세 연구자, 트레이더, 위험 분석가와 포트폴리오 매니저를 고정된
LangGraph로 연결한 공개 프로젝트를 소스 기준으로 설명한다.

이 사례가 Claude Agent SDK 강좌에 주는 비교점은 “에이전트 수”보다 다음 계약이다.

- 각 역할이 읽을 수 있는 데이터와 도구
- 다음 역할에 넘기는 typed state와 보고서
- 토론 순서와 종료를 결정하는 conditional router
- 데이터 부재, 구조화 출력 실패와 중단 재개를 드러내는 failure contract

TradingAgents의 팀은 실행 중 새 동료를 만드는 Claude SDK Team이 아니다. 선택한 분석가와
토론자가 코드에 정의된 순서로 움직이는 LangGraph workflow다. Anthropic 모델을 provider로
선택할 수는 있지만, 그것만으로 Claude Agent SDK의 `Agent` 도구, child session 또는 Team
이벤트가 생기는 것은 아니다.

그러므로 이 자료는 Claude SDK native team의 실행 증거가 아니라, **도메인별 역할·근거·상태·
라우팅을 명시적으로 설계한 다른 멀티에이전트 방식**을 비교해 보는 부록으로 읽는다.

- [한국어 해설 전체 보기](https://nfbs2000.github.io/speaky-TradingAgents/)
- [소스 지도와 출처](https://nfbs2000.github.io/speaky-TradingAgents/source-map.html)
- [원 프로젝트 TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
