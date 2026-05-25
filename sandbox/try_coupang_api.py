"""
Try common Coupang internal API URL patterns.
The campaign page is /np/campaigns/82/components/115573
Internal APIs often use /vp/ prefix or different path structures.
"""
from curl_cffi import requests as cffi_requests
import json

# Common API URL patterns to try based on campaign URL structure
urls_to_try = [
    # vp (viewpoint) pattern - common internal API prefix
    "https://www.coupang.com/vp/campaigns/82/components/115573",
    # API pattern with JSON
    "https://www.coupang.com/vp/goldbox/deals?campaignId=82&componentId=115573",
    # Component API
    "https://www.coupang.com/vp/component/115573",
    # Category best
    "https://www.coupang.com/vp/bestcategory/component/115573",
    # Mobile API (often less protected)
    "https://m.coupang.com/vm/campaigns/82/components/115573",
    "https://m.coupang.com/vm/goldbox/deals?campaignId=82&componentId=115573",
    # Product list from component
    "https://www.coupang.com/vp/campaigns/82/components/115573/products",
    # Alternative patterns
    "https://www.coupang.com/vp/component/115573/products?page=1&size=20",
    "https://www.coupang.com/np/api/campaigns/82/components/115573",
]

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Accept": "application/json, text/html, */*",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Referer": "https://www.coupang.com/",
}

print("Testing Coupang API patterns...\n")
print("=" * 70)

for url in urls_to_try:
    try:
        resp = cffi_requests.get(
            url,
            headers=headers,
            impersonate="safari17_0",
            timeout=10,
            allow_redirects=True
        )
        content_type = resp.headers.get("content-type", "unknown")
        body = resp.text[:500] if resp.status_code == 200 else resp.text[:200]

        # Check if it's a bot challenge or actual content
        is_challenge = "sec-if-cpt-container" in body or "Access Denied" in body
        has_json = "json" in content_type
        has_products = any(kw in body for kw in ["productId", "itemName", "price", "productName"])

        status_icon = "OK" if resp.status_code == 200 and not is_challenge else "BLOCKED" if is_challenge else str(resp.status_code)

        print(f"\n[{status_icon}] {url}")
        print(f"    Status: {resp.status_code} | Type: {content_type[:50]} | Size: {len(resp.content):,}B")

        if has_products:
            print(f"    >>> PRODUCT DATA FOUND! <<<")
            print(f"    Preview: {body[:300]}")
        elif resp.status_code == 200 and not is_challenge:
            print(f"    Preview: {body[:200]}")
    except Exception as e:
        print(f"\n[ERROR] {url}")
        print(f"    {str(e)[:100]}")

print("\n" + "=" * 70)
print("\nDone. Looking for patterns that returned product data...")
