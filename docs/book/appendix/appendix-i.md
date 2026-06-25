# 부록 I: 강좌 플러그인 배포 청사진

이 페이지는 한국어 SDK 책의 `부록 I: 강좌 플러그인 배포 청사진`을 공개 Python cookbook과 공식 Agent SDK 문서에 맞춰 다시 쓴 공개판이다. 원래 장의 문제의식은 유지하되, 내부 TypeScript 구현명이나 비공개 기능을 그대로 옮기지 않는다. 대신 실행 가능한 notebook, Python 파일, README, 공식 문서를 근거로 사용한다.

**분류:** 부록<br>
**공개 상태:** `public`<br>
**근거 신뢰도:** `medium`<br>
**원문 위치:** `docs/book-sdk-ko/src/appendix/i-course-plugin-blueprint.md`

## 이 장의 공개판 요지

이 장은 공개 SDK와 cookbook 예제로 대부분 직접 설명할 수 있다.

공개판에서는 강좌 플러그인 청사진을 docs site, skills package, notebooks, generated mapping, GitHub Pages workflow로 구성한다. 이 사이트 자체가 blueprint 예제이며, `book_projection.yml`과 `build_pages_docs.py`가 책 내용을 공개 cookbook으로 투영하는 재사용 가능한 패턴이다.

[Projection data](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/docs/data/book_projection.yml)를 근거로 삼는다. [Docs generator](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/scripts/build_pages_docs.py)를 근거로 삼는다.

!!! evidence "주요 cookbook 근거"
    - [Projection data](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/docs/data/book_projection.yml)
    - [Docs generator](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/scripts/build_pages_docs.py)
    - [MkDocs configuration](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/mkdocs.yml)
    - [GitHub Pages workflow](https://github.com/nfbs2000/speaky-claude-cookbooks/blob/main/.github/workflows/deploy-pages.yml)

!!! evidence "공식 문서 근거"
    - [Plugins in the SDK](https://code.claude.com/docs/en/agent-sdk/plugins.md)
    - [Create plugins](https://code.claude.com/docs/en/plugins.md)

## 원문 절 구조를 공개 SDK로 다시 읽기

### I.1 공식 플러그인 표면

이 절은 skills, agents, hooks, MCP를 묶어 배포하는 확장 단위로 설명한다. 내부 marketplace 로직은 공개판의 대상이 아니다.

### I.2 공개 repo 기본 구조

이 절은 원문의 `I.2 공개 repo 기본 구조` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 강좌 플러그인 청사진을 docs site, skills package, notebooks, generated mapping, GitHub Pages workflow로 구성한다. 이 사이트 자체가 blueprint 예제이며, `book_projection.yml`과 `build_pages_do... 이며, 먼저 `Projection data`를 기준 예제로 읽는다.

### I.3 Manifest 초안

이 절은 원문의 `I.3 Manifest 초안` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 강좌 플러그인 청사진을 docs site, skills package, notebooks, generated mapping, GitHub Pages workflow로 구성한다. 이 사이트 자체가 blueprint 예제이며, `book_projection.yml`과 `build_pages_do... 이며, 먼저 `Projection data`를 기준 예제로 읽는다.

### I.4 Skill 계약

이 절은 원문의 `I.4 Skill 계약` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 강좌 플러그인 청사진을 docs site, skills package, notebooks, generated mapping, GitHub Pages workflow로 구성한다. 이 사이트 자체가 blueprint 예제이며, `book_projection.yml`과 `build_pages_do... 이며, 먼저 `Projection data`를 기준 예제로 읽는다.

### I.5 챕터별 실습 매핑

이 절은 원문의 `I.5 챕터별 실습 매핑` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 강좌 플러그인 청사진을 docs site, skills package, notebooks, generated mapping, GitHub Pages workflow로 구성한다. 이 사이트 자체가 blueprint 예제이며, `book_projection.yml`과 `build_pages_do... 이며, 먼저 `Projection data`를 기준 예제로 읽는다.

### I.6 학생 실행 흐름

이 절은 원문의 `I.6 학생 실행 흐름` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 강좌 플러그인 청사진을 docs site, skills package, notebooks, generated mapping, GitHub Pages workflow로 구성한다. 이 사이트 자체가 blueprint 예제이며, `book_projection.yml`과 `build_pages_do... 이며, 먼저 `Projection data`를 기준 예제로 읽는다.

### I.7 강사용 관측 연결

이 절은 원문의 `I.7 강사용 관측 연결` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 강좌 플러그인 청사진을 docs site, skills package, notebooks, generated mapping, GitHub Pages workflow로 구성한다. 이 사이트 자체가 blueprint 예제이며, `book_projection.yml`과 `build_pages_do... 이며, 먼저 `Projection data`를 기준 예제로 읽는다.

### I.8 배포 단계

이 절은 원문의 `I.8 배포 단계` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 강좌 플러그인 청사진을 docs site, skills package, notebooks, generated mapping, GitHub Pages workflow로 구성한다. 이 사이트 자체가 blueprint 예제이며, `book_projection.yml`과 `build_pages_do... 이며, 먼저 `Projection data`를 기준 예제로 읽는다.

### I.9 금지선

이 절은 원문의 `I.9 금지선` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 강좌 플러그인 청사진을 docs site, skills package, notebooks, generated mapping, GitHub Pages workflow로 구성한다. 이 사이트 자체가 blueprint 예제이며, `book_projection.yml`과 `build_pages_do... 이며, 먼저 `Projection data`를 기준 예제로 읽는다.

### I.10 참고 공식 문서

이 절은 원문의 `I.10 참고 공식 문서` 논지를 공개 Python cookbook의 실행 가능한 근거로 옮긴다. 핵심은 공개판에서는 강좌 플러그인 청사진을 docs site, skills package, notebooks, generated mapping, GitHub Pages workflow로 구성한다. 이 사이트 자체가 blueprint 예제이며, `book_projection.yml`과 `build_pages_do... 이며, 먼저 `Projection data`를 기준 예제로 읽는다.

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

- 교육용 배포는 원문 복사가 아니라 공개 근거 기반 재작성이어야 한다.

## 실습 방향

- 새 강좌를 추가할 때 source book, public evidence, omit boundary를 함께 정의한다.

## Builder takeaway

이 장의 공개판 목표는 원문을 얕게 요약하는 것이 아니다. 책의 논지를 유지하되, 독자가 직접 열어볼 수 있는 Python cookbook과 공식 문서에 묶어 두는 것이다. 따라서 장을 읽은 뒤에는 적어도 하나의 notebook 또는 Python 파일에서 같은 개념을 확인할 수 있어야 한다. 확인할 수 없는 내부 세부는 주장으로 남기지 않고, 공개 경계나 추론으로 분리한다.
