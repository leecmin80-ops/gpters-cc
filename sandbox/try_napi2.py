from curl_cffi import requests as cffi_requests

# Pattern found: /n-api/web-adapter/
# Campaign page: /np/campaigns/82/components/115573
urls_to_try = [
    "https://www.coupang.com/n-api/web-adapter/campaigns/82/components/115573",
    "https://www.coupang.com/n-api/web-adapter/campaigns/82",
    "https://www.coupang.com/n-api/web-adapter/component/115573",
    "https://www.coupang.com/n-api/web-adapter/component/115573/products",
    "https://www.coupang.com/n-api/web-adapter/goldbox/campaigns/82/components/115573",
    "https://www.coupang.com/n-api/web-adapter/products?campaignId=82&componentId=115573",
    "https://www.coupang.com/n-api/web-adapter/bestcategory/115573",
    "https://www.coupang.com/n-api/web-adapter/campaign-products?campaignId=82&componentId=115573&page=1",
    "https://www.coupang.com/n-api/web-adapter/np/campaigns/82/components/115573",
    "https://www.coupang.com/n-api/web-adapter/deals?campaignId=82&componentId=115573",
    "https://www.coupang.com/n-api/web-adapter/ranking/products?componentId=115573",
    "https://www.coupang.com/n-api/web-adapter/categories/products?componentId=115573",
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "application/json, */*",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Referer": "https://www.coupang.com/np/campaigns/82/components/115573",
    "X-Requested-With": "XMLHttpRequest",
}

print("Testing /n-api/web-adapter/ patterns...\n")

for url in urls_to_try:
    try:
        resp = cffi_requests.get(url, headers=headers, impersonate="chrome131", timeout=10, allow_redirects=True)
        body = resp.text[:1000]
        is_challenge = "sec-if-cpt-container" in body or "Access Denied" in body
        has_products = any(kw in body for kw in ["productId", "itemName", "price", "productName", "salePrice", "productImage", "title"])
        is_json = body.strip().startswith("{") or body.strip().startswith("[")

        if resp.status_code == 200 and not is_challenge and is_json:
            icon = "PRODUCT!" if has_products else "JSON-OK"
            print(f"[{icon}] {url}")
            print(f"    Size: {len(resp.content):,}B")
            print(f"    Body: {body[:500]}")
            print()
        elif resp.status_code == 200 and not is_challenge:
            print(f"[OK-{resp.status_code}] {url} (Size: {len(resp.content):,}B) Type: {resp.headers.get('content-type','?')[:40]}")
        else:
            print(f"[{resp.status_code}] {url}")
    except Exception as e:
        print(f"[ERR] {url}: {str(e)[:60]}")

print("\nDone!")
