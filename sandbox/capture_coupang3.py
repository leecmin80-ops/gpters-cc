import asyncio
import os
from playwright.async_api import async_playwright

async def capture_network():
    api_requests = []
    user = os.environ.get("USERNAME", "leecmin")
    chrome_user_data = f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data"

    async with async_playwright() as p:
        # Launch using the user's actual Chrome profile
        context = await p.chromium.launch_persistent_context(
            user_data_dir=chrome_user_data,
            headless=False,
            channel="chrome",
            args=[
                "--disable-blink-features=AutomationControlled",
                "--profile-directory=Default"
            ],
            viewport={"width": 1920, "height": 1080},
            no_viewport=False
        )

        page = context.pages[0] if context.pages else await context.new_page()

        async def handle_response(response):
            url = response.url
            content_type = response.headers.get("content-type", "")
            # Capture broadly - any JSON response or URLs with relevant keywords
            if ("json" in content_type or "javascript" in content_type or
                "/api/" in url or "/vp/" in url or "component" in url or
                "campaign" in url or "products" in url or "goldbox" in url or
                "category" in url or "best" in url or "ranking" in url):
                try:
                    status = response.status
                    body = b""
                    if status == 200:
                        try:
                            body = await response.body()
                        except:
                            pass
                    api_requests.append({
                        "url": url[:500],
                        "status": status,
                        "size": len(body),
                        "content_type": content_type[:80],
                        "body_preview": body[:1000].decode("utf-8", errors="ignore") if body else ""
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
            title = await page.title()
            print(f"Page title: {title}")
        except Exception as e:
            print(f"Page load: {e}")

        # Wait and scroll to trigger lazy-loaded API calls
        await asyncio.sleep(5)
        for i in range(5):
            await page.evaluate("window.scrollBy(0, 800)")
            await asyncio.sleep(2)

        await context.close()

    print(f"\n=== Found {len(api_requests)} relevant requests ===\n")
    # Sort by size, show top results
    sorted_reqs = sorted(api_requests, key=lambda x: x["size"], reverse=True)
    for i, req in enumerate(sorted_reqs[:30]):
        print(f"[{i+1}] Status={req['status']} Size={req['size']:,}B")
        print(f"    URL: {req['url']}")
        print(f"    Type: {req['content_type']}")
        if req['body_preview'] and req['size'] > 500:
            # Show first part of body to identify product data
            preview = req['body_preview'][:300].replace('\n', ' ')
            print(f"    Preview: {preview}")
        print()

asyncio.run(capture_network())
