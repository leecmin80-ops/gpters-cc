from curl_cffi import requests as cffi_requests
import json

urls_to_try = [
    "https://reco.coupang.com/api/v2/viewed-products?page=0",
    "https://reco.coupang.com/api/v2/viewed-products?page=0&size=20",
    "https://reco.coupang.com/api/v2/best-products?page=0",
    "https://reco.coupang.com/api/v2/ranking?page=0",
    "https://reco.coupang.com/api/v2/popular-products?page=0",
    "https://reco.coupang.com/api/v2/category-ranking?page=0",
    "https://reco.coupang.com/api/v2/best-sellers?page=0",
    "https://reco.coupang.com/api/v2/campaigns/82/products?page=0",
    "https://reco.coupang.com/api/v2/components/115573/products?page=0",
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "application/json, */*",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Referer": "https://www.coupang.com/np/campaigns/82/components/115573",
    "Origin": "https://www.coupang.com",
}

print("Testing reco.coupang.com API patterns...\n")

for url in urls_to_try:
    try:
        resp = cffi_requests.get(url, headers=headers, impersonate="chrome131", timeout=10)
        body = resp.text[:1500]
        is_json = body.strip().startswith("{") or body.strip().startswith("[")
        has_products = any(kw in body for kw in ["productId", "productName", "productImage", "price", "salePrice", "title", "itemId"])

        if resp.status_code == 200 and is_json:
            icon = "PRODUCT!" if has_products else "JSON"
            print(f"[{icon}] {url}")
            print(f"    Size: {len(resp.content):,}B")
            print(f"    Body: {body[:600]}")
            print()
        else:
            print(f"[{resp.status_code}] {url} (Size: {len(resp.content)}B)")
    except Exception as e:
        print(f"[ERR] {url}: {str(e)[:80]}")

print("\nDone!")
