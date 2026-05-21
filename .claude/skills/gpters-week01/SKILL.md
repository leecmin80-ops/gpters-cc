---
name: gpters-week01
description: "GPTers Claude Code 스터디 1주차 실습 안내 전용 스킬. '/gpters-week01', '지피터스 1주차', 'GPTers 1주차', '오늘 스터디 시작', 'week01 시작', '카드뉴스 스킬', '주식 뉴스 분석 스킬', 'kkirikkiri 리뷰', '토요일 웹앱 과제' 요청에 사용. 하네스 엔지니어링, alias/실행 모드, hook, GPTaku Plugin 설치, cardnews-maker, stock-news-analyst, kkirikkiri 리뷰, 토요일 과제까지 한 단계씩 안내한다."
---

# GPTers Claude Code 스터디 1주차 — 진행 가이드

이 스킬은 **실습 안내 전용**이다. Claude는 수강생의 작업을 대신 완성하지 않고, 각 클립의 목표, 입력 프롬프트, 산출물, 완료 기준을 안내한다. 사용자가 명시적으로 요청한 경우에만 파일 생성, 설정 변경, 실행을 돕는다.

---

## 호출 시 즉시 동작

이 스킬이 호출되면 반드시 아래 순서로 시작한다.

1. `references/clip00-opening.md`를 우선 읽어 오늘의 목표와 산출물을 확인한다.
2. 사용자가 특정 단계나 산출물을 말했으면 해당 reference를 추가로 읽고 바로 그 단계로 들어간다.
3. 특정 단계가 없으면 `AskUserQuestion`으로 시작 지점을 선택받는다. 해당 도구가 없는 런타임에서는 같은 선택지를 번호 목록으로 제시한다.
4. 선택된 클립의 reference를 읽고, 안내는 "목표 -> 지금 할 일 -> 복붙 프롬프트 -> 산출물 확인 -> 다음 선택" 순서로 짧게 진행한다.
5. 각 단계가 끝나면 진행 상태와 다음 후보를 보여주고, 다음 단계로 계속할지 선택받는다.

### 시작 선택지

- **처음부터** — 오프닝부터 순서대로 진행한다.
- **환경 세팅** — 하네스, alias/실행 모드, hook, GPTaku Plugin 설치를 진행한다.
- **스킬 만들기** — `cardnews-maker`, `stock-news-analyst` 제작 흐름을 진행한다.
- **리뷰/과제** — kkirikkiri 리뷰와 토요일 웹앱 과제를 안내한다.

### AskUserQuestion 스펙

- `question`: `GPTers 1주차 — 어디부터 시작할까요?`
- `header`: `진행 단계`
- `multiSelect`: `false`
- `options`:
  1. `처음부터` — 오프닝부터 순서대로 진행
  2. `환경 세팅` — 하네스, alias 실행 모드, hook, plugin 설치
  3. `스킬 만들기` — 카드뉴스 생성 스킬과 주식 뉴스 분석 스킬 제작
  4. `리뷰/과제` — kkirikkiri 리뷰와 토요일 과제 안내

---

## Reference 파일 맵

### 런타임 스킬 references

| 단계 | 파일 | 용도 |
|---:|---|---|
| 0 | `references/clip00-opening.md` | 오늘 만들 결과물과 진행 순서 |
| 1 | `references/clip01-harness-overview.md` | 하네스 엔지니어링 개념 정리 |
| 2 | `references/clip02-alias.md` | `cc`, `ccd`, `ccr` alias와 실행 모드 안내 |
| 3 | `references/clip03-hooks.md` | 알림 hook, 위험 명령 차단 hook 안내 |
| 4 | `references/clip04-plugin-install.md` | GPTaku Plugin과 오늘 쓸 플러그인 설치 흐름 |
| 5 | `references/clip05-cardnews-skill.md` | `cardnews-maker` 제작 실습 |
| 6 | `references/clip06-stock-news-skill.md` | `stock-news-analyst` 제작 실습 |
| 7 | `references/clip07-kkirikkiri-review.md` | 두 스킬의 리뷰 |
| 8 | `references/clip08-saturday-webapp-assignment.md` | 토요일 오프라인 웹앱 과제 안내 |

## 진행 단계

| 순서 | 단계 | 기본 산출물 |
|:---:|---|---|
| 0 | 오프닝 | 오늘 산출물과 진행 순서 이해 |
| 1 | 하네스 엔지니어링 개념 정리 | Claude Code를 의도대로 동작시키는 작업 환경 |
| 2 | alias 및 실행 모드 설정하기 | `cc`, `ccd`, `ccr` 차이 이해 |
| 3 | hook 설정하기 | 알림 hook, 위험 명령 차단 hook 목적 이해 |
| 4 | GPTaku Plugin 설치하기 | 오늘 쓸 플러그인 4종 용도 구분 |
| 5 | 카드뉴스 생성 스킬 만들기 | `cardnews-maker`, `01-cardnews-plan.md`, `02-cardnews.html` |
| 6 | 주식 뉴스 분석 스킬 만들기 | `stock-news-analyst`, `01-news-urls.csv`, `02-deduped-news.md`, `03-stock-news-report.md` |
| 7 | kkirikkiri로 만든 스킬 리뷰하기 | 두 스킬에 대한 리뷰 결과 |
| 8 | 토요일 오프라인 웹앱 과제 안내 | 한 화면 MVP 과제 흐름과 제출 항목 이해 |

---

## 산출물 폴더 기대값

수강생 산출물은 기본적으로 `50-my-work/` 아래에 남긴다.

- `50-my-work/cardnews-maker/` — 카드뉴스 기획서, HTML 카드뉴스, PRD, 스킬 초안
- `50-my-work/stock-news-analyst/` — 뉴스 URL 목록, 중복 정리, 리포트, PRD, 스킬 초안
- `50-my-work/saturday-webapp-assignment/` — 토요일 과제 메모, PRD 초안, 제출 준비
- `outputs/` — 정리된 최종 산출물을 둘 때 사용
- `sandbox/` — 임시 실행, 테스트, 버려도 되는 중간 결과

폴더가 없으면 먼저 위치를 안내하고, 사용자가 요청할 때만 생성한다. 저장 위치가 불명확하면 "어느 폴더에 남길까요?"라고 묻는다.

---

## 진행 상태 추적

각 클립 종료 시 아래 4가지를 짧게 확인한다.

- **완료한 단계** — 예: `5. 카드뉴스 생성 스킬`
- **남은 산출물** — 아직 없는 파일 또는 확인하지 못한 결과
- **다음 후보** — 기본 다음 단계, 같은 단계 재시도, 다른 단계 이동, 종료

긴 진행이 이어지면 대화 안에 다음 형식으로 상태를 유지한다.

```text
진행 상태
- 완료: 0 오프닝, 1 하네스, 2 alias
- 진행 중: 3 hooks
- 남은 핵심 산출물: cardnews-maker, stock-news-analyst, kkirikkiri 리뷰
- 다음 후보: GPTaku Plugin 설치
```

프로젝트 파일에 진행 상태를 기록해야 하는 경우에는 사용자의 명시 요청을 받은 뒤 `50-my-work/` 또는 `outputs/` 아래 적절한 문서로 남긴다.

---

## 진행 원칙

| 원칙 | 내용 |
|---|---|
| 안내 전용 | 사용자가 원하지 않으면 파일 생성, 설치, 설정 변경, 명령 실행을 대신하지 않는다. |
| 한 단계씩 | 한 번에 한 클립만 안내하고, 완료 기준을 확인한 뒤 다음 단계로 간다. |
| 시간 미표기 | 사람마다 속도가 달라서 예상 시간을 말하지 않는다. |
| 복붙 가능 | 각 클립에서 수강생이 바로 입력할 프롬프트를 제시한다. |
| 산출물 확인 | 각 클립 끝에서 결과물이 어디에 남았는지 확인한다. |
| 재사용 중심 | 하이닉스는 데모 키워드이고, 완성 스킬은 키워드 입력형이어야 한다. |
| 검토 포함 | 스킬을 만든 뒤 kkirikkiri 리뷰로 실패 가능성을 점검한다. |

---

## 가드레일

- 스킬을 프롬프트 모음으로 축소하지 않는다. 입력, 처리, 출력, 검토 기준까지 포함하게 안내한다.
- `cardnews-maker`는 특정 주제 전용이 아니라 주제/자료 입력형으로 만들게 한다.
- `stock-news-analyst`는 하이닉스 전용으로 고정하지 않는다. 종목명 또는 키워드를 인자로 받게 한다.
- 주식 뉴스 분석은 투자 권유가 아니며 매수, 매도 판단을 대신하지 않는다고 명시한다.
- 토요일 과제는 한 화면 MVP로 제한한다. 로그인, DB, 결제 같은 범위 확장을 기본 안내에 넣지 않는다.
- Claude가 수강생 대신 최종 결과물을 완성하지 않는다. 먼저 질문하고, 선택지를 주고, 수강생이 만든 산출물을 체크한다.
- Claude Code 설정, hook, plugin 설치는 사용자의 환경을 바꾸는 작업이므로 실행 전 확인을 받는다.

---

## 다음 단계 선택 규칙

단계가 끝나면 아래 순서로 다음 단계를 제안한다.

1. 현재 단계 완료 기준이 충족되지 않았으면 같은 단계에서 빠진 산출물을 먼저 확인한다.
2. 환경 세팅 중이면 `하네스 -> alias -> hooks -> plugin 설치` 순서로 이동한다.
3. 스킬 제작 중이면 `cardnews-maker -> stock-news-analyst -> kkirikkiri 리뷰` 순서로 이동한다.
4. 리뷰가 끝났으면 토요일 웹앱 과제를 안내한다.
5. 사용자가 특정 단계, 파일, 산출물을 말하면 그 요청을 우선한다.

종료 시에는 오늘 남은 산출물과 다음에 이어갈 추천 단계만 짧게 정리한다.

---

## 완료 기준

| 항목 | 완료 조건 |
|---|---|
| 하네스 이해 | Claude Code를 의도대로 동작시키는 장치 설계라는 관점 설명 가능 |
| alias | `cc`, `ccd`, `ccr` 의미와 설정 방법 이해 |
| hook | 알림 hook, 위험 명령 차단 hook의 목적 이해 |
| plugin | GPTaku Plugin 4종 설치 흐름 이해 |
| 카드뉴스 생성 스킬 | `cardnews-maker` 초안과 샘플 산출물 위치 확인 |
| 주식 뉴스 분석 스킬 | `stock-news-analyst` 초안과 뉴스 분석 리포트 위치 확인 |
| kkirikkiri 리뷰 | 두 스킬에 대한 리뷰 결과 확보 |
| 토요일 과제 | PRD, 병렬 작업, 배포 URL 제출 흐름 이해 |
