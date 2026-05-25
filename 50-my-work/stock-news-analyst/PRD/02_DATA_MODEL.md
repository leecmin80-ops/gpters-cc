# stock-news-analyst -- 데이터 모델

---

## 전체 구조

```
[키워드 입력] --수집--> [뉴스 목록] --정리--> [이슈 묶음] --분석--> [리포트]
```

---

## 엔티티 상세

### 입력 (Input)

| 필드 | 설명 | 예시 | 필수 |
|------|------|------|------|
| keyword | 종목명 또는 산업 키워드 | "삼성전자", "2차전지" | O |
| count | 수집 기사 수 | 30 (기본값) | X |

### 뉴스 기사 (Article)

| 필드 | 설명 | 예시 | 필수 |
|------|------|------|------|
| title | 기사 제목 | "삼성전자 노조 투표율 83%" | O |
| press_url | 언론사 원문 URL | http://... | O |
| naver_url | 네이버 뉴스 URL | https://n.news.naver.com/... | X |
| summary | 핵심 내용 1줄 | "임단협 잠정합의안 가결 관측" | O |
| pub_date | 발행 시간 | 2026-05-24 15:44 | O |

### 이슈 묶음 (Issue)

| 필드 | 설명 | 예시 | 필수 |
|------|------|------|------|
| issue_id | 이슈 번호 | 1 | O |
| title | 이슈 제목 | "DS 특별성과급 찬반투표" | O |
| summary | 핵심 요약 | "투표율 83% 가결 관측 우세" | O |
| articles | 관련 기사 목록 | [Article, ...] | O |
| article_count | 관련 기사 수 | 12 | O |

### 리포트 (Report)

| 섹션 | 내용 |
|------|------|
| Executive Summary | 전체 뉴스 흐름 3줄 요약 |
| 핵심 이슈 분석 | 이슈별 현황 + Analyst View |
| Bull Case | 긍정 요인 테이블 |
| Bear Case | 리스크 요인 테이블 |
| Key Metrics to Watch | 모니터링 지표 + 시점 |
| 후속 검색 키워드 | 다음에 확인할 키워드 5개 |
| Disclaimer | 투자 권유 아님 명시 |

---

## 산출물 파일 구조

```
50-my-work/stock-news-analyst/
├── 01-news-urls.csv           # 수집된 뉴스 목록
├── 02-deduped-news.md         # 중복 정리된 이슈 묶음
└── 03-stock-news-report.md    # 종목 분석 리포트
```
