from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://saucedemo.com")
    
    title = page.title()
    print(title)
    
    page.locator('//input[@placeholder="Username"]').fill('standard_user')
    page.locator('[data-test="password"]').fill('secret_sauce')
    page.locator('[id="login-button"]').click()
    page.pause()
    
    # page.close()
    