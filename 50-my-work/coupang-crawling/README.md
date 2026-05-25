# 쿠팡 카테고리별 판매 순위 크롤링 프로젝트

> 쿠팡 쇼핑몰에서 카테고리별 판매량 높은 제품 정보를 수집하는 프로젝트

---

## 목표

- 쿠팡 카테고리 순위 페이지에서 상품 정보(이름, 가격, 별점, 리뷰수, URL) 추출
- 카테고리별 베스트셀러 데이터를 CSV/JSON으로 정리
- 반복 가능한 자동화 흐름 구축

---

## 대상 URL 구조

```
https://www.coupang.com/np/campaigns/{campaignId}/components/{componentId}
```

예시: `https://www.coupang.com/np/campaigns/82/components/115573`

---

## WAF 차단 상황

쿠팡은 **Akamai Bot Manager**를 사용하여 자동화 접근을 차단함.

### 시도한 방법과 결과

| 방법 | 도구 | 결과 | 비고 |
|------|------|------|------|
| TLS 임퍼소네이션 격자 | insane-search engine (curl_cffi) | 실패 (403/challenge) | 13회 시도 모두 차단 |
| Headless 브라우저 | Playwright + Chromium | 실패 (403) | 봇 탐지 |
| Real Chrome 자동화 | Playwright + channel="chrome" | 실패 (Access Denied) | 자동화 감지 |
| 사용자 프로필 활용 | Playwright persistent context | 실패 | Chrome 이미 실행 중 충돌 |
| API URL 패턴 추정 | curl_cffi | 404 | /n-api/, /vp/ 등 시도 |
| reco.coupang.com | curl_cffi | 접근 성공, 데이터 없음 | WAF 없음, 추천 전용 서버 |
| **페이지 소스 수동 저장 → 파싱** | **Python regex** | **성공** | JSON-LD 구조화 데이터 추출 |

### 발견한 API 엔드포인트

| URL | 용도 | WAF |
|-----|------|-----|
| `https://www.coupang.com/n-api/reliability` | 상태 확인 | 없음 |
| `https://www.coupang.com/n-api/web-adapter/cart-count` | 장바구니 수 | 없음 |
| `https://reco.coupang.com/api/v2/viewed-products` | 최근 본 상품 | 없음 |
| `https://ljc.coupang.com/api/v3/web/submit` | 로그/추적 | 없음 |
| `https://www.coupang.com/vp/products/{id}/reviews` | 상품 리뷰 | 없음 (브라우저 세션 필요) |

---

## 현재 동작하는 방법

### 수집 흐름

```
[수동] 크롬에서 카테고리 순위 페이지 열기
  ↓
[수동] Ctrl+U → Ctrl+A → Ctrl+C → 메모장에 저장 (.txt)
  ↓
[자동] Python 스크립트로 HTML 파싱 (JSON-LD 추출)
  ↓
[자동] CSV + JSON 파일 저장
```

### 추출 원리

쿠팡 순위 페이지는 SEO를 위해 **JSON-LD (Schema.org)** 구조화 데이터를 HTML에 포함함:

```json
{
  "@type": "ItemList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Product",
        "name": "상품명",
        "image": ["이미지URL"],
        "offers": { "price": 4130, "priceCurrency": "KRW" },
        "aggregateRating": { "ratingValue": 4.5, "reviewCount": 5941 },
        "url": "https://www.coupang.com/vp/products/..."
      }
    }
  ]
}
```

### 추출 스크립트

파일 위치: `sandbox/extract_final.py`

실행:
```powershell
python sandbox/extract_final.py
```

---

## 추출되는 데이터 항목

| 필드 | 설명 | 예시 |
|------|------|------|
| rank | 순위 | 1 |
| name | 상품명 | 스카치브라이트 쓰리엠 유리닦이 |
| price | 가격(원) | 4130 |
| currency | 통화 | KRW |
| rating | 별점 | 4.5 |
| review_count | 리뷰수 | 5941 |
| url | 상품 페이지 URL | https://www.coupang.com/vp/products/6504753059?... |
| product_id | 상품ID | 6504753059 |
| item_id | 아이템ID | 24886651074 |
| vendor_item_id | 판매자아이템ID | 92227242722 |
| image | 썸네일 이미지 URL | //thumbnail.coupangcdn.com/... |

---

## 첫 수집 결과 (2026-05-24)

카테고리: 청소용품 순위 (campaigns/82/components/115573)

| 순위 | 상품명 | 가격 | 별점 | 리뷰수 |
|------|--------|------|------|--------|
| 1 | 스카치브라이트 쓰리엠 유리닦이 | 4,130원 | 4.5 | 5,941 |
| 2 | 엠비코 빗자루 쓰레받기 세트 A | 7,020원 | 4.5 | 5,632 |
| 3 | 꼬까 다용도 세제 청소 브러쉬 | 1,170원 | 4.5 | 2,439 |
| 4 | 코멧 분리수거 배접 비닐봉투 100개 20L | 3,990원 | 5.0 | 26,486 |
| 5 | 리빙채널 5in1 v자 바닥 화장실 청소솔 | 12,900원 | 5.0 | 304 |
| 6 | 코멧 일회용 변기 클리너 24입 세트 | 10,990원 | 4.5 | 12,772 |
| 7 | 홈스타일즈 양면모 욕실 유리창 청소솔 | 2,500원 | 4.5 | 5,148 |
| 8 | HB153 스팀모프 커피 잔여물 다용도청소솔 | 5,900원 | 5.0 | 1,466 |
| 9 | 락앤락 테이블탑 이동형 45892 | 14,300원 | 5.0 | 13,854 |
| 10 | 아이뽀얀 프로페셔널 2in1 욕실 바닥 청소솔 | 5,470원 | 4.5 | 1,882 |

---

## 현재 한계점

| 문제 | 설명 |
|------|------|
| 수동 저장 필요 | 매번 Ctrl+U로 소스를 저장해야 함 |
| 페이지당 최대 10개 | JSON-LD에 10개까지만 포함됨 |
| 한 페이지씩만 | 여러 카테고리를 한번에 수집 불가 |
| 실시간 자동화 불가 | Akamai 때문에 자동 반복 수집 안 됨 |
| 판매량 직접 데이터 없음 | 리뷰수로 인기도 추정만 가능 |

---

## 다음 단계 (개선 방향)

### 1. Chrome 원격 디버깅 연결 (수동 저장 제거)

Chrome을 특수 모드로 열면 Python이 직접 접속 가능:

```powershell
# Chrome 완전 종료 후 실행
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
```

그 후 Python에서 CDP(Chrome DevTools Protocol)로 연결하여 자동으로 페이지 소스 가져오기.

### 2. 여러 카테고리 자동 수집

카테고리 URL 목록을 입력하면 순서대로 수집:

```python
categories = [
    ("청소용품", "/np/campaigns/82/components/115573"),
    ("주방용품", "/np/campaigns/82/components/XXXXX"),
    ("욕실용품", "/np/campaigns/82/components/YYYYY"),
]
```

### 3. 리뷰 API로 상세 데이터 보강

수집한 product_id로 리뷰 API를 호출하여 상세 리뷰 데이터 추가:

```
https://www.coupang.com/vp/products/{product_id}/reviews
```

### 4. 쿠팡 파트너스 API (공식)

- 가입: 쿠팡 파트너스 사이트
- API 키 발급 후 안정적으로 상품 검색/카테고리 조회 가능
- 합법적이고 WAF 차단 없음

### 5. 10개 제한 돌파

- 페이지 소스 외에 실제 렌더된 DOM에서 추출 (CDP 연결 시 가능)
- 또는 카테고리 내 하위 페이지들을 각각 수집하여 합산

---

## 파일 구조

```
50-my-work/coupang-crawling/
├── README.md              ← 이 파일
sandbox/
├── capture_coupang.py     ← Playwright 네트워크 캡처 (실패)
├── capture_coupang2.py    ← Real Chrome 캡처 (실패)
├── capture_coupang3.py    ← 사용자 프로필 캡처 (실패)
├── try_coupang_api.py     ← API 패턴 추정 테스트
├── try_napi.py            ← /n-api/ 패턴 테스트
├── try_napi2.py           ← /n-api/web-adapter/ 테스트
├── try_reco.py            ← reco.coupang.com 테스트
├── parse_coupang.py       ← HTML 파싱 초기 버전
├── extract_products.py    ← 파싱 v2
├── extract_products2.py   ← 파싱 v3
├── extract_final.py       ← 최종 동작 버전 ★
바탕화면 출력물/
├── coupang_products.csv   ← 엑셀용 결과
├── coupang_products.json  ← 프로그래밍용 결과
```

---

## 메모

- 쿠팡 WAF: Akamai Bot Manager (매우 강력, curl/Playwright 모두 차단)
- 핵심 발견: 순위 페이지에 JSON-LD 구조화 데이터가 포함되어 있음
- `reco.coupang.com`은 WAF 없이 접근 가능 (활용 가능성 있음)
- 리뷰 API는 브라우저 세션(쿠키)이 있으면 접근 가능
