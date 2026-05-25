from curl_cffi import requests as cffi_requests
import json

# Now we know the prefix is /n-api/
# Original page: /np/campaigns/82/components/115573
urls_to_try = [
    "https://www.coupang.com/n-api/reliability",
    "https://www.coupang.com/n-api/campaigns/82/components/115573",
    "https://www.coupang.com/n-api/campaigns/82",
    "https://www.coupang.com/n-api/products?campaignId=82&componentId=115573",
    "https://www.coupang.com/n-api/component/115573",
    "https://www.coupang.com/n-api/component/115573/products",
    "https://www.coupang.com/n-api/goldbox?campaignId=82&componentId=115573",
    "https://www.coupang.com/n-api/bestcategory?componentId=115573",
    "https://www.coupang.com/n-api/campaigns/82/components/115573/products",
    "https://www.coupang.com/n-api/campaigns/82/components/115573/items",
    "https://m.coupang.com/n-api/campaigns/82/components/115573",
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "application/json, text/html, */*",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Referer": "https://www.coupang.com/np/campaigns/82/components/115573",
}

print("Testing /n-api/ patterns...\n")

for url in urls_to_try:
    try:
        resp = cffi_requests.get(
            url,
            headers=headers,
            impersonate="chrome131",
            timeout=10,
            allow_redirects=True
        )
        body = resp.text[:800]
        is_challenge = "sec-if-cpt-container" in body or "Access Denied" in body
        has_json_data = body.strip().startswith("{") or body.strip().startswith("[")
        has_products = any(kw in body for kw in ["productId", "itemName", "price", "productName", "productImage"])

        if resp.status_code == 200 and not is_challenge:
            icon = "PRODUCT!" if has_products else "OK"
            print(f"[{icon}] {url}")
            print(f"    Status: {resp.status_code} | Size: {len(resp.content):,}B | JSON: {has_json_data}")
            print(f"    Body: {body[:400]}")
            print()
        else:
            status_msg = "BLOCKED" if is_challenge else str(resp.status_code)
            print(f"[{status_msg}] {url} (Size: {len(resp.content):,}B)")
    except Exception as e:
        print(f"[ERROR] {url}: {str(e)[:80]}")

print("\nDone!")
