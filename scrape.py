import asyncio
from playwright.async_api import async_playwright

URLS = [
    "https://sanand0.github.io/tdsdata/js_table/?seed=72",
    "https://sanand0.github.io/tdsdata/js_table/?seed=73",
    "https://sanand0.github.io/tdsdata/js_table/?seed=74",
    "https://sanand0.github.io/tdsdata/js_table/?seed=75",
    "https://sanand0.github.io/tdsdata/js_table/?seed=76",
    "https://sanand0.github.io/tdsdata/js_table/?seed=77",
    "https://sanand0.github.io/tdsdata/js_table/?seed=78",
    "https://sanand0.github.io/tdsdata/js_table/?seed=79",
    "https://sanand0.github.io/tdsdata/js_table/?seed=80",
    "https://sanand0.github.io/tdsdata/js_table/?seed=81",
]

async def get_sum(page, url):
    await page.goto(url, wait_until="networkidle")
    cells = await page.query_selector_all("table td, table th")
    total = 0
    for cell in cells:
        text = (await cell.inner_text()).strip()
        try:
            total += float(text)
        except:
            pass
    return total

async def main():
    grand_total = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        for url in URLS:
            s = await get_sum(page, url)
            print(f"Seed {url.split('=')[-1]}: {s}")
            grand_total += s
        await browser.close()
    print(f"Grand Total: {grand_total}")

asyncio.run(main())
