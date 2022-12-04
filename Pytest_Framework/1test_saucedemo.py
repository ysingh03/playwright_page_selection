from playwright.sync_api import sync_playwright, Playwright, expect

def test_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1500)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://www.saucedemo.com/")

    # page.locator("//input[@id='aauser-name']").fill("standard_user", timeout=1000)
    page.locator("//input[@id='user-name']").fill("standard_user", timeout=2000)
    page.locator("#password[data-test='password']").fill("secret_sauce")
    page.locator("#login-button[name='login-button']").click()

    product_header = page.locator("//span[text()='Products']")

    assert product_header.is_visible(), "User is unable to login"

    menu_data = page.locator("#react-burger-menu-btn")
    menu_data.click()

    logout_btn = page.locator("#logout_sidebar_link")
    logout_btn.click()

    login_btn = page.locator("#login-button[name='login-button']")

    assert login_btn.is_visible(), 'Logout is not done'

    print("Test full done")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    test_login(playwright)














