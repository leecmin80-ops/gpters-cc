# Clip 4. GPTaku Plugin 설치하기

## 목표

| 항목 | 내용 |
|---|---|
| 목적 | 오늘 사용할 GPTaku Plugin을 설치한다 |
| 설치 대상 | `show-me-the-prd`, `skillers-suda`, `kkirikkiri`, `insane-search` |
| 원칙 | 설치 후 Claude Code를 재시작하고 동작 확인한다 |

## 설치할 플러그인

| 플러그인 | 오늘 쓰는 용도 |
|---|---|
| `show-me-the-prd` | 작업 흐름을 PRD로 정리 |
| `skillers-suda` | PRD를 바탕으로 스킬 생성 |
| `kkirikkiri` | 만든 스킬을 역할별로 리뷰 |
| `insane-search` | 네이버 뉴스 검색 결과에서 기사 URL 수집 흐름 설계 |

## 수강생 입력 프롬프트

```text
GPTaku Plugin을 설치하려고 해.

마켓플레이스 URL:
https://github.com/fivetaku/gptaku_plugins.git

오늘 설치할 플러그인:
- show-me-the-prd
- skillers-suda
- kkirikkiri
- insane-search

Claude Code에서 어떤 순서로 설치하면 되는지 안내해줘.
설치 후 재시작과 확인 방법까지 알려줘.
```

## 설치 흐름 메모

| 순서 | 할 일 |
|---:|---|
| 1 | `/plugin` 또는 플러그인 메뉴 진입 |
| 2 | Marketplace 추가 |
| 3 | `https://github.com/fivetaku/gptaku_plugins.git` 입력 |
| 4 | 플러그인 4종 설치 |
| 5 | Claude Code 재시작 |
| 6 | 설치 목록 확인 |

## 완료 기준

| 항목 | 확인 |
|---|---|
| GPTaku marketplace가 등록됐다 |  |
| 4개 플러그인 설치 대상이 확인됐다 |  |
| Claude Code 재시작 필요성을 이해했다 |  |
