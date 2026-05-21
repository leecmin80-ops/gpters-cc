---
description: "GPTers Claude Code 스터디 1주차 흐름을 시작한다. gpters-week01 스킬과 reference 파일을 읽고 시작 지점 선택, 단계별 안내, 산출물 확인, 다음 단계 선택까지 진행."
---

# /gpters-week01

GPTers Claude Code 스터디 1주차 진행을 시작한다.

## 실행 흐름

1. `.claude/skills/gpters-week01/SKILL.md`를 읽고 해당 스킬의 규칙을 따른다.
2. 시작 시 `.claude/skills/gpters-week01/references/clip00-opening.md`를 확인한다.
3. 사용자가 특정 단계나 산출물을 지정하지 않았다면 `AskUserQuestion`으로 시작 지점을 선택받는다. 도구가 없는 런타임에서는 같은 선택지를 번호 목록으로 제시한다.
4. 선택된 단계의 `.claude/skills/gpters-week01/references/` 파일을 읽고, 목표, 복붙 프롬프트, 산출물, 완료 기준 순서로 안내한다.
5. 수강생의 파일 생성, 설정 변경, plugin 설치, 명령 실행은 사용자가 명시적으로 요청한 경우에만 돕는다.
6. 각 단계 끝에서 진행 상태, 남은 산출물, 다음 후보를 짧게 정리한다.

## 시작 선택지

- `처음부터` — 오프닝부터 순서대로 진행
- `환경 세팅` — 하네스, alias 실행 모드, hook, plugin 설치
- `스킬 만들기` — 카드뉴스 생성 스킬과 주식 뉴스 분석 스킬 제작
- `리뷰/과제` — kkirikkiri 리뷰와 토요일 과제 안내

## guardrails

- 수강생의 작업을 대신 완성하지 말고, 안내, 질문, 점검을 우선한다.
- 산출물은 기본적으로 `50-my-work/cardnews-maker/`, `50-my-work/stock-news-analyst/`, `50-my-work/saturday-webapp-assignment/`에 남기도록 안내한다.
- `stock-news-analyst`는 하이닉스 고정이 아니라 키워드 입력형으로 만들게 한다.
- 주식 뉴스 분석은 투자 권유가 아니라고 명시한다.
- 토요일 과제는 한 화면 MVP 범위로 제한한다.
