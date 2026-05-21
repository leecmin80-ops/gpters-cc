# GPTers Claude Code Study

GPTers Claude Code 스터디 1~2주차 실습용 워크스페이스입니다.

- 1주차: Claude Code 하네스 이해, alias/hook/plugin 흐름 확인, 스킬 2개 제작, 리뷰
- 토요일 과제: PRD 기반 한 화면 웹앱 만들기와 배포 URL 준비
- 2주차: 토요일 결과를 바탕으로 웹앱 작업 워크스페이스 정리

---

## 빠른 시작

이 저장소를 받은 뒤 Claude Code에서 폴더를 엽니다.

```bash
git clone https://github.com/fivetaku/gpters-cc.git
cd gpters-cc
claude
```

Claude Code 안에서 입력합니다.

```text
/gpters-week01
```

슬래시 커맨드가 보이지 않으면 이렇게 말해도 됩니다.

```text
지피터스 1주차 스터디 시작하자.
```

---

## 1주차에 하는 일

1주차 목표는 Claude Code를 그냥 쓰는 것이 아니라, 내가 반복해서 쓸 수 있는 작업 흐름을 스킬로 만드는 것입니다.

진행 흐름:

1. 하네스 엔지니어링 개념을 정리합니다.
2. `cc`, `ccd`, `ccr` alias와 실행 모드를 확인합니다.
3. 알림 hook과 위험 명령 차단 hook의 역할을 이해합니다.
4. GPTaku Plugin 설치 흐름을 봅니다.
5. `cardnews-maker` 스킬을 만듭니다.
6. `stock-news-analyst` 스킬을 만듭니다.
7. `kkirikkiri`로 두 스킬을 리뷰합니다.
8. 토요일 웹앱 과제를 준비합니다.

주요 플러그인:

- `show-me-the-prd` — 아이디어를 PRD 문서로 정리
- `skillers-suda` — 반복 작업을 Claude Code 스킬로 정리
- `kkirikkiri` — 리뷰 팀 구성과 역할 분리
- `insane-search` — 검색과 자료 조사 보조

---

## 오늘 남길 결과물

결과물은 `50-my-work/` 아래에 저장합니다.

- `50-my-work/cardnews-maker/` — 카드뉴스 기획서, HTML 샘플, 스킬 초안
- `50-my-work/stock-news-analyst/` — 뉴스 URL, 중복 정리, 분석 리포트, 스킬 초안
- `50-my-work/kkirikkiri-review/` — 두 스킬에 대한 리뷰 결과
- `50-my-work/saturday-webapp-assignment/` — 토요일 웹앱 아이디어, PRD 초안, 제출 메모

`stock-news-analyst`는 투자 조언 도구가 아닙니다. 뉴스 기반으로 이슈를 정리하고 확인할 질문을 만드는 실습입니다.

---

## 토요일 과제

토요일 과제는 웹앱을 크게 만드는 시간이 아닙니다.

목표:

- 한 화면에서 핵심 기능 하나가 작동하는 MVP를 정합니다.
- PRD 초안을 만듭니다.
- 필요한 역할과 작업 순서를 나눕니다.
- Vercel 또는 GitHub Pages 같은 배포 URL을 준비합니다.
- 완성하지 못했다면 막힌 지점과 다음 작업을 적습니다.

제출 양식은 `30-templates/saturday-webapp-submission.md`를 참고합니다.

---

## 2주차 방향

2주차는 토요일 과제를 다시 정리해서 PRD 기반 웹앱 작업 워크스페이스로 만드는 시간입니다.

진행 흐름:

1. 토요일 결과를 공유합니다.
2. `show-me-the-prd`로 요구사항을 다시 정리합니다.
3. 데이터 구조와 화면 목록을 정합니다.
4. 목표와 완료 기준을 잡습니다.
5. 웹앱 작업 폴더에 README, 실행 명령, 배포 기준을 둡니다.
6. `kkirikkiri`로 기획, UI, 구현, QA 역할을 나눠 점검합니다.

---

## 폴더 안내

- `CLAUDE.md` — Claude Code가 따를 학습 하네스 규칙
- `.claude/commands/` — Claude Code 슬래시 커맨드
- `.claude/skills/gpters-week01/` — 1주차 진행 스킬과 참고 자료
- `00-system/` — 답변 언어와 기본 톤 규칙
- `10-curriculum/` — 수강생용 요약 가이드
- `20-references/` — 실습 중 추가 참고 자료를 적는 곳
- `30-templates/` — 복붙 프롬프트, 리뷰 프롬프트, 제출 양식
- `40-mock-data/` — 샘플 입력과 테스트 데이터
- `50-my-work/` — 수강생 실습 결과 저장 위치
- `90-archive/` — 더 이상 쓰지 않는 파일 보관 위치
- `artifacts/` — 공유 가능한 결과물 보관 위치
- `outputs/` — 정리된 최종 산출물 보관 위치
- `sandbox/` — 임시 실험 파일

---

## 막혔을 때

- 에러가 나면 에러 메시지를 그대로 Claude Code에 붙여넣습니다.
- 뭘 입력해야 할지 모르겠으면 `~하려는데 어떻게 해?`라고 묻습니다.
- 어디 저장할지 모르겠으면 `50-my-work/` 아래에 결과물별 폴더를 만듭니다.
- 스킬이 프롬프트 모음처럼 보이면 입력, 처리 단계, 출력 파일, 완료 기준을 추가합니다.
- 웹앱 범위가 커지면 첫 화면에서 한 가지 핵심 행동만 남깁니다.
