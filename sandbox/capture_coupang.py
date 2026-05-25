import asyncio
from playwright.async_api import async_playwright

async def capture_network():
    api_requests = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        async def handle_response(response):
            url = response.url
            content_type = response.headers.get("content-type", "")
            if ("json" in content_type or "/api/" in url or "/vp/" in url or
                "component" in url or "campaign" in url or "product" in url):
                try:
                    status = response.status
                    body = await response.body() if status == 200 else b""
                    api_requests.append({
                        "url": url[:300],
                        "status": status,
                        "size": len(body),
                        "content_type": content_type[:80]
                    })
                except:
                    pass

        page.on("response", handle_response)

        try:
            await page.goto(
                "https://www.coupang.com/np/campaigns/82/components/115573",
                wait_until="networkidle",
                timeout=30000
            )
        except Exception as e:
            print(f"Page load note: {e}")

        await asyncio.sleep(3)
        await browser.close()

    print(f"\n=== Found {len(api_requests)} API/JSON requests ===\n")
    for i, req in enumerate(sorted(api_requests, key=lambda x: x["size"], reverse=True)[:20]):
        print(f"[{i+1}] Status={req['status']} Size={req['size']:,}B")
        print(f"    URL: {req['url']}")
        print(f"    Type: {req['content_type']}")
        print()

asyncio.run(capture_network())
