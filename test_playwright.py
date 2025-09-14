import time
from playwright.sync_api import sync_playwright
start = time.time()
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://books.toscrape.com/")
    page.wait_for_selector(".product_pod h3 a")
    title = page.get_attribute(".product_pod h3 a", "title")
    price = page.text_content(".product_pod .price_color")
    print("Playwright extracted:")
    print(f"Title: {title}")
    print(f"Price: {price}")
    browser.close()
end = time.time()
print(f"Playwright took {end - start:.2f} seconds")
