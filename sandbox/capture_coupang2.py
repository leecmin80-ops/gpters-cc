import asyncio
import json
from playwright.async_api import async_playwright

async def capture_network():
    api_requests = []

    async with async_playwright() as p:
        # Use real Chrome (not Chromium) to bypass bot detection
        browser = await p.chromium.launch(
            headless=False,
            channel="chrome",
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080}
        )
        page = await context.new_page()

        # Remove webdriver flag
        await page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
        """)

        async def handle_response(response):
            url = response.url
            content_type = response.headers.get("content-type", "")
            if ("json" in content_type or "/api/" in url or "/vp/" in url or
                "component" in url or "campaign" in url or "products" in url or
                "goldbox" in url or "bestcategory" in url):
                try:
                    status = response.status
                    body = b""
                    if status == 200:
                        body = await response.body()
                    api_requests.append({
                        "url": url[:500],
                        "status": status,
                        "size": len(body),
                        "content_type": content_type[:80],
                        "body_preview": body[:500].decode("utf-8", errors="ignore") if body else ""
                    })
                except:
                    pass

        page.on("response", handle_response)

        try:
            await page.goto(
                "https://www.coupang.com/np/campaigns/82/components/115573",
                wait_until="networkidle",
                timeout=45000
            )
            print("Page loaded successfully!")
            title = await page.title()
            print(f"Page title: {title}")
        except Exception as e:
            print(f"Page load note: {e}")

        # Wait for dynamic content
        await asyncio.sleep(5)

        # Try scrolling to trigger more API calls
        for i in range(3):
            await page.evaluate("window.scrollBy(0, 1000)")
            await asyncio.sleep(2)

        await browser.close()

    print(f"\n=== Found {len(api_requests)} API/JSON requests ===\n")
    for i, req in enumerate(sorted(api_requests, key=lambda x: x["size"], reverse=True)[:25]):
        print(f"[{i+1}] Status={req['status']} Size={req['size']:,}B")
        print(f"    URL: {req['url']}")
        print(f"    Type: {req['content_type']}")
        if req['body_preview'] and req['size'] > 100:
            preview = req['body_preview'][:200]
            print(f"    Preview: {preview}...")
        print()

asyncio.run(capture_network())
