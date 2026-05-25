# stock-news-analyst -- Phase 분리 계획

---

## Phase 1: MVP

### 목표
키워드 입력만으로 뉴스 수집 → 중복 정리 → 분석 리포트가 자동 생성된다

### 기능
- [ ] 키워드 입력 → NaverSearch MCP로 뉴스 30건 수집
- [ ] 수집 기사 CSV 저장 (01-news-urls.csv)
- [ ] 중복·유사 이슈 묶기 (02-deduped-news.md)
- [ ] 월가 스타일 분석 리포트 (03-stock-news-report.md)
- [ ] Disclaimer 자동 포함
- [ ] `50-my-work/stock-news-analyst/`에 자동 저장

### Phase 1 시작 프롬프트
```
이 PRD를 읽고 Phase 1을 구현해주세요.
@PRD/01_PRD.md
@PRD/02_DATA_MODEL.md

Phase 1 범위:
- 키워드 → 뉴스 30건 수집 (NaverSearch MCP)
- 중복 정리 (이슈별 묶음)
- 분석 리포트 (Executive Summary, Bull/Bear, Key Metrics)
- Disclaimer 필수 포함
```

---

## Phase 2: 확장

### 기능
- [ ] 수집 건수 선택 (15/30/50건)
- [ ] 영문 키워드 → 구글 뉴스 fallback
- [ ] 기사 본문 요약 (insane-search + Jina Reader)
- [ ] 이전 리포트와 비교 (변화 추적)

---

## Phase 3: 고도화

### 기능
- [ ] 정기 실행 스케줄 (매일/매주)
- [ ] 복수 종목 동시 분석
- [ ] 섹터 비교 리포트

---

## Phase 로드맵 요약

| Phase | 핵심 기능 | 상태 |
|-------|----------|------|
| Phase 1 (MVP) | 키워드 → 뉴스 수집 → 중복 정리 → 리포트 | 시작 전 |
| Phase 2 | 건수 선택, 영문 지원, 본문 요약 | Phase 1 완료 후 |
| Phase 3 | 정기 실행, 복수 종목, 섹터 비교 | Phase 2 완료 후 |
