import asyncio
import re
from playwright.async_api import async_playwright

async def get_price(page, url):
    print(f"Navigating to {url}...")
    # Princess site might be slow, so we give it a good timeout.
    await page.goto(url, wait_until='domcontentloaded', timeout=60000)
    
    # Let the JS execute and render the pricing blocks.
    # Princess pages usually show a skeleton and then load the price.
    await page.wait_for_timeout(5000) # Wait 5 additional seconds for any API prices to settle
    
    # Extract the visible text content from the body to find prices
    text_content = await page.evaluate("document.body.innerText")
    lines = [line.strip() for line in text_content.split('\n') if line.strip()]
    
    target_rooms = ["Balcony", "Deluxe Balcony", "Premium Deluxe Balcony", "Mini-Suite"]
    found_prices = {}
    
    for i, line in enumerate(lines):
        if line in target_rooms:
            # The price is on the line immediately preceding the title
            if i > 0 and lines[i-1].startswith('$'):
                found_prices[line] = lines[i-1]
                
    if found_prices:
        print("Prices found on page:")
        for room, price in found_prices.items():
            print(f"  {room}: {price}")
    else:
        print("No target prices found.")

async def main():
    urls = [
        "https://www.princess.com/cruise-search/stateroom-type/?voyageCode=1639&guestCount=2&stateRoomId=B",
        "https://www.princess.com/cruise-search/stateroom-type/?voyageCode=1639&guestCount=2&stateRoomId=M"
    ]
    
    async with async_playwright() as p:
        # Launching in headless mode to not interrupt the user.
        # Adding some stealth arguments.
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            viewport={'width': 1920, 'height': 1080}
        )
        page = await context.new_page()
        
        for url in urls:
            await get_price(page, url)
            print("-" * 50)
            
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
