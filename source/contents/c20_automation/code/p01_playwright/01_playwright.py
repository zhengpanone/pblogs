from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.baidu.com")
    page.fill('#kw', "Playwright")
    page.click('#su')
    page.screenshot(path="baidu.png")
    print(page.title())
    browser.close()