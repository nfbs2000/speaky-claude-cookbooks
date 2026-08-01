# 부록 P: 공개 GitHub Pages 통합 목차

이 부록은 강의 중 흩어져 보이는 공개 GitHub Pages를 한 번에 찾기 위한 목차다.
여기서 말하는 “공개”는 URL이 브라우저에서 열리는 정적 페이지라는 뜻이다. 강좌의
정본은 여전히 `docs/book-sdk-ko`의 Markdown이고, 실행 증거의 정본은 SDK raw event,
OTel, Opik, sanitized bundle이다.

2026-08-01 기준으로 GitHub Pages API에서 `nfbs2000` 계정의 Pages 활성 repository를
확인했고, 아래 루트 URL은 HTTP 200 응답을 확인했다. 다만 모든 하위 장과 모든
deep link를 매번 검증했다는 뜻은 아니다. 하위 목차는 각 사이트의 자체 목차나
이 저장소의 `online.md`를 함께 본다.

## P.1 먼저 열 사이트

| 목적 | 먼저 열 URL | 언제 쓰는가 |
| --- | --- | --- |
| SDK 강좌 공개 보조판 | [speaky-claude-cookbooks/book](https://nfbs2000.github.io/speaky-claude-cookbooks/book/) | SDK 책 장별 공개 설명을 보여 줄 때 |
| SDK 슬라이드 | [slides/book-sdk-ko](https://nfbs2000.github.io/speaky-claude-cookbooks/slides/book-sdk-ko/) | CourseGraph 기반 장면과 녹화 보조 화면을 열 때 |
| SDK Runtime City | [speaky-PGSimCity/education/claude-sdk-runtime-city](https://nfbs2000.github.io/speaky-PGSimCity/education/claude-sdk-runtime-city/) | Claude SDK와 DashScope 관측 bundle을 정적 replay로 설명할 때 |
| SDK Agent Flow | [speaky-agent-flow/education](https://nfbs2000.github.io/speaky-agent-flow/education/) | SDK agent flow 증거 리플레이를 열 때 |
| TinyTroupe 글쓰기 팀 | [speaky-TinyTroupe/education](https://nfbs2000.github.io/speaky-TinyTroupe/education/) | 팀 글쓰기 실험과 evidence anchor를 설명할 때 |
| Mineflayer 봇 팀 | [speaky-mineflayer](https://nfbs2000.github.io/speaky-mineflayer/) | Minecraft 봇 팀, Claude skills와 Mineflayer runtime 경계를 설명할 때 |
| TradingAgents 팀·스킬 | [speaky-TradingAgents/part5/ch12-claude-team-skills](https://nfbs2000.github.io/speaky-TradingAgents/part5/ch12-claude-team-skills.html) | TradingAgents 포크의 `.claude` agent team과 skill 운영층을 설명할 때 |

## P.2 SDK 강좌 공개 자산

이 표는 `docs/book-sdk-ko/public-resources.json`에 들어 있는 공개 또는 운영 링크를
학생에게 안내하기 쉽게 다시 정리한 것이다.

| 링크 | 종류 | 접근 | 역할 |
| --- | --- | --- | --- |
| [공개 책 보조판](https://nfbs2000.github.io/speaky-claude-cookbooks/book/) | book | public | SDK 책 장별 공개 설명과 공개 보조 목차 |
| [Claude Cookbook 공개 페이지](https://nfbs2000.github.io/speaky-claude-cookbooks/) | cookbook | public | Cookbook 루트, recipe, reference와 공개 보조판의 허브 |
| [Book SDK 공개 슬라이드](https://nfbs2000.github.io/speaky-claude-cookbooks/slides/book-sdk-ko/) | slide | public | CourseGraph 장면 기반 강의 보조 화면 |
| [Claude SDK Runtime City](https://nfbs2000.github.io/speaky-PGSimCity/education/claude-sdk-runtime-city/) | city-game | public | 실제 provider 실행을 도시형 replay로 보여 주는 표면 |
| [Claude SDK Agent Flow 증거 리플레이](https://nfbs2000.github.io/speaky-agent-flow/education/) | agent-flow | public | agent flow, tool result와 evidence replay를 연결하는 표면 |
| [TinyTroupe Claude 글쓰기 팀](https://nfbs2000.github.io/speaky-TinyTroupe/education/) | team-writing-lab | public | 팀 기반 글쓰기 실험과 evidence anchor |
| [Dive into Claude Code 한국어 동반판](https://nfbs2000.github.io/speaky-Dive-into-Claude-Code/) | source-reference | public | Claude Code를 하니스 관점에서 읽는 외부 연구 동반판 |
| [Claude Code from Source 한국어 동반판](https://nfbs2000.github.io/speaky-claude-code-from-source/) | source-reference | public | Claude Code source 분석 자료의 선택 참고판 |
| [Claude Code 소스 탐색 가이드](https://nfbs2000.github.io/speaky-claude-code/) | source-reference | public | 비공식 Claude Code source snapshot을 찾는 지도 |
| [TradingAgents 한국어 소스 해설](https://nfbs2000.github.io/speaky-TradingAgents/) | source-reference | public | LangGraph 기반 멀티에이전트 금융 workflow 비교 자료 |
| [TradingAgents Claude 팀과 스킬](https://nfbs2000.github.io/speaky-TradingAgents/part5/ch12-claude-team-skills.html) | team-skills | public | TradingAgents `.claude/TEAM.md`, `agents/`, `skills/` 운영층 해설 |

아래 두 항목은 repository의 Pages 루트는 살아 있지만, SDK 강좌용 특정 공개 자산은
`public-resources.json`에서 아직 `pending`으로 남아 있다.

| 항목 | Pages 루트 | 현재 상태 |
| --- | --- | --- |
| Pixel Agents Claude SDK 게임 | [speaky-pixel-agents](https://nfbs2000.github.io/speaky-pixel-agents/) | SDK 강좌용 `pixel-game` URL은 아직 미확정 |
| Claude SDK Observation Ordeal | [speaky-hypnagonia](https://nfbs2000.github.io/speaky-hypnagonia/) | SDK 강좌용 `hypnagonia-game` URL은 아직 미확정 |

GitHub Pages는 아니지만 강의 운영에서 함께 쓰는 접근 조건 링크도 있다.

| 링크 | 접근 | 역할 |
| --- | --- | --- |
| [Notion SDK 자료](https://app.notion.com/p/38246e2fca248102b8c1e73224d381a0) | 초대 필요 | 강사용 확장 설명과 장별 자료 |
| [Opik Cloud 증거](https://www.comet.com/opik/shin-yunho/projects/019f21e5-e0fa-738d-8e02-a04d251673ea/dashboards?dashboardId=template%3Aproject-overview&dashboard_time_range=past30days) | 로그인 필요 | 실제 trace, attachment, trajectory 평가를 설명하는 운영 표면 |

## P.3 Pages 활성 repository 전체

아래 표는 GitHub Pages API로 확인한 활성 repository 목록이다. `branch/path`는
Pages source 설정이며, `상태`는 API의 build status 또는 루트 URL HTTP 확인 결과다.

| Repository | Pages URL | branch/path | 확인 | 강좌에서의 위치 |
| --- | --- | --- | --- | --- |
| `speaky-claude-cookbooks` | [site](https://nfbs2000.github.io/speaky-claude-cookbooks/) | `main` / `/docs` | built, HTTP 200 | SDK 공개 책, Cookbook, projection, slide 허브 |
| `speaky-PGSimCity` | [site](https://nfbs2000.github.io/speaky-PGSimCity/) | `main` / `/docs` | built, HTTP 200 | Runtime City와 course replay |
| `speaky-agent-flow` | [site](https://nfbs2000.github.io/speaky-agent-flow/) | `main` / `/docs` | built, HTTP 200 | SDK agent flow evidence replay |
| `speaky-TinyTroupe` | [site](https://nfbs2000.github.io/speaky-TinyTroupe/) | `main` / `/docs` | built, HTTP 200 | synthetic team, writing lab, evidence demo |
| `speaky-pixel-agents` | [site](https://nfbs2000.github.io/speaky-pixel-agents/) | `main` / `/docs` | built, HTTP 200 | Pixel Agents 강좌/게임 계열 |
| `speaky-hypnagonia` | [site](https://nfbs2000.github.io/speaky-hypnagonia/) | `main` / `/docs` | built, HTTP 200 | observation ordeal 게임 계열 |
| `speaky-mineflayer` | [site](https://nfbs2000.github.io/speaky-mineflayer/) | `master` / `/docs` | built, HTTP 200 | Mineflayer runtime, Claude Minecraft 봇 팀 |
| `speaky-gemini-cli` | [site](https://nfbs2000.github.io/speaky-gemini-cli/) | `gh-pages` / `/` | built, HTTP 200 | Gemini CLI runtime 해부 온라인판 |
| `speaky-opencode` | [site](https://nfbs2000.github.io/speaky-opencode/) | `dev` / `/docs` | built, HTTP 200 | OpenCode source 해설 온라인판 |
| `speaky-oh-my-openagent` | [site](https://nfbs2000.github.io/speaky-oh-my-openagent/) | `dev` / `/docs` | built, HTTP 200 | OMAO/OpenAgent plugin architecture 온라인판 |
| `speaky-codex` | [site](https://nfbs2000.github.io/speaky-codex/) | `gh-pages` / `/` | built, HTTP 200 | Codex source 해설 온라인판 |
| `speaky-claude-code` | [site](https://nfbs2000.github.io/speaky-claude-code/) | `main` / `/docs` | built, HTTP 200 | Claude Code 소스 탐색 가이드 |
| `speaky-claude-code-from-source` | [site](https://nfbs2000.github.io/speaky-claude-code-from-source/) | `main` / `/docs` | built, HTTP 200 | Claude Code from Source 동반판 |
| `speaky-Dive-into-Claude-Code` | [site](https://nfbs2000.github.io/speaky-Dive-into-Claude-Code/) | `main` / `/docs` | built, HTTP 200 | Dive into Claude Code 동반판 |
| `speaky-TradingAgents` | [site](https://nfbs2000.github.io/speaky-TradingAgents/) | `main` / `/docs` | built, HTTP 200 | TradingAgents 소스 해설, Claude Code 팀·스킬 해설 |
| `speaky-CopilotKit` | [site](https://nfbs2000.github.io/speaky-CopilotKit/) | `main` / `/` | Pages active, HTTP 200 | CopilotKit 공개 source/coursegraph 참고 |
| `speaky-cocos4` | [site](https://nfbs2000.github.io/speaky-cocos4/) | `v4.0.0` / `/` | Pages active, HTTP 200 | Cocos 계열 공개 Pages |
| `speaky-sim` | [site](https://nfbs2000.github.io/speaky-sim/) | `main` / `/` | Pages active, HTTP 200 | Sim 계열 공개 Pages |

## P.4 온라인 책 목차가 따로 있는 자료

아래 자료는 각 책의 `online.md`가 장별 링크 목차 역할을 한다. SDK 책에서는 이
부록을 허브로 삼고, 장별 세부 링크는 해당 `online.md`를 원전으로 본다.

| 책 원본 | 온라인 목차 | 로컬 목차 파일 | 성격 |
| --- | --- | --- | --- |
| Gemini CLI 런타임 해부 | [speaky-gemini-cli](https://nfbs2000.github.io/speaky-gemini-cli/) | `docs/book-gemini-runtime-ko/src/online.md` | Gemini CLI를 Claude Code/SDK 책과 같은 질문으로 비교 |
| Codex 온라인판 | [speaky-codex](https://nfbs2000.github.io/speaky-codex/) | `docs/book-ko-codex/src/online.md` | Codex source 탐색과 1장 진입 링크 |
| OMAO/OpenAgent 온라인판 | [speaky-oh-my-openagent](https://nfbs2000.github.io/speaky-oh-my-openagent/) | `docs/book-omo-ko/src/online.md` | OpenCode 위 플러그인 하니스와 확장 계약 |
| OpenCode 온라인판 | [speaky-opencode](https://nfbs2000.github.io/speaky-opencode/) | `docs/book-opencode/src/online.md` | OpenCode core, surface, plugin, permission architecture |

## P.5 SDK 공개 보조판의 주요 세부 진입점

`speaky-claude-cookbooks` 안에는 SDK 책, projection, slide, recipe와 reference가
같이 있다. 강의 중에는 아래 순서로 열면 된다.

| 진입점 | URL | 역할 |
| --- | --- | --- |
| 공개 책 | [book](https://nfbs2000.github.io/speaky-claude-cookbooks/book/) | 장별 공개 설명의 기본 목차 |
| 강의 projection | [projection](https://nfbs2000.github.io/speaky-claude-cookbooks/projection/) | CourseGraph/장별 projection 탐색 |
| 장 지도 | [projection/chapter-map](https://nfbs2000.github.io/speaky-claude-cookbooks/projection/chapter-map/) | 공개 projection의 장 목록 |
| SDK 슬라이드 | [slides/book-sdk-ko](https://nfbs2000.github.io/speaky-claude-cookbooks/slides/book-sdk-ko/) | 녹화와 강의 진행용 slide runtime |
| Cookbook recipes | [recipes](https://nfbs2000.github.io/speaky-claude-cookbooks/recipes/) | Cookbook 예제와 SDK 강좌 연결 |
| Agent SDK recipes | [recipes/agent-sdk](https://nfbs2000.github.io/speaky-claude-cookbooks/recipes/agent-sdk/) | Agent SDK 예제 묶음 |
| 공개 경계 | [reference/public-boundary](https://nfbs2000.github.io/speaky-claude-cookbooks/reference/public-boundary/) | 공개/비공개 경계 설명 |
| 소스 정책 | [reference/source-policy](https://nfbs2000.github.io/speaky-claude-cookbooks/reference/source-policy/) | 출처와 재배포 경계 |

## P.6 Mineflayer 팀 페이지

`speaky-mineflayer`는 Minecraft 봇 조작 자체보다 “Mineflayer runtime 위에 Claude
Code 스킬과 팀을 어떻게 올리는가”를 보여 주는 비교 자료다.

| 진입점 | URL | 역할 |
| --- | --- | --- |
| Mineflayer Pages 홈 | [speaky-mineflayer](https://nfbs2000.github.io/speaky-mineflayer/) | Docsify 문서 홈 |
| 한국어 소스 해설 | [source guide](https://nfbs2000.github.io/speaky-mineflayer/#/ko/source-guide) | Mineflayer를 관찰/행동 runtime으로 읽기 |
| Claude 스킬 팀 해설 | [skills and team](https://nfbs2000.github.io/speaky-mineflayer/#/ko/claude-minecraft-team) | `minecraft-team`, `minecraft-operate`, 역할별 봇 팀 소개 |

## P.7 TradingAgents 팀·스킬 페이지

`speaky-TradingAgents`의 새 팀·스킬 페이지는 TradingAgents Python LangGraph
파이프라인이 아니라, 이 포크를 Claude Code로 읽고 고치고 검증하기 위한 `.claude`
운영층을 설명한다.

| 진입점 | URL | 역할 |
| --- | --- | --- |
| TradingAgents Pages 홈 | [speaky-TradingAgents](https://nfbs2000.github.io/speaky-TradingAgents/) | 한국어 소스 해설 홈 |
| Claude Code 팀과 스킬 | [team and skills](https://nfbs2000.github.io/speaky-TradingAgents/part5/ch12-claude-team-skills.html) | `ta-lead`, specialist agents, runtime research team과 `ta-*` skills 소개 |
| 소스 지도와 출처 | [source map](https://nfbs2000.github.io/speaky-TradingAgents/source-map.html) | Python pipeline source와 `.claude` 운영층 진입점 |

## P.8 사용 규칙

1. 강좌 정본은 공개 Pages가 아니라 `docs/book-sdk-ko` Markdown이다.
2. 공개 Pages는 학생에게 열어 줄 수 있는 보조판, replay, game, source guide다.
3. GitHub Pages 루트가 HTTP 200이어도 SDK 강좌용 deep link가 완성됐다는 뜻은 아니다.
4. `public-resources.json`에서 `pending`인 항목은 수업에서 완성된 공개 자산처럼 말하지 않는다.
5. Notion과 Opik은 GitHub Pages가 아니며 각각 초대와 로그인 조건을 설명해야 한다.
6. 외부 source 해설은 공식 SDK contract를 대체하지 않고, 본문 실습의 보조 비교 자료로만 쓴다.
7. 새 공개 Pages가 생기면 이 부록과 `docs/book-sdk-ko/public-resources.json` 중 어느 쪽이 원전인지 먼저 정하고 갱신한다.

## Takeaway

이 부록의 목적은 URL을 많이 나열하는 것이 아니라, 학생과 강사가 같은 공개 표면을
같은 이름으로 부르게 만드는 것이다. SDK 책, 공개 보조판, slide, replay, source
guide와 게임이 서로 다른 저장소에 있어도, 강의에서는 이 부록을 마지막 허브로 삼아
필요한 표면으로 이동한다.
