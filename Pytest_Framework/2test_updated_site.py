import pytest
from playwright.sync_api import expect, Page, Playwright


@pytest.mark.skip(reason="Not Implement")
def test_login_with_valid_credentials(playwright:Playwright, page) -> None:

    page.goto("https://www.saucedemo.com/")

    # page.locator("//input[@id='aauser-name']").fill("standard_user", timeout=1000)
    page.locator("//input[@id='user-name']").fill("standard_user", timeout=2000)
    page.locator("#password[data-test='password']").fill("secret_sauce")
    page.locator("#login-button[name='login-button']").click()

    product_header = page.locator("//span[text()='Products']")

    assert product_header.is_visible(), "User is unable to login"
    print("First test done")


@pytest.mark.xfail(reason="BugNo-1890")
def test_logout(playwright: Playwright, page) -> None:

    page.goto("https://www.saucedemo.com/")

    # page.locator("//input[@id='aauser-name']").fill("standard_user", timeout=1000)
    page.locator("//input[@id='user-name']").fill("standard_user", timeout=2000)
    page.locator("#password[data-test='password']").fill("secret_sauce")
    page.locator("#login-button[name='login-button']").click()

    product_header = page.locator("//span[text()='Products']")

    menu_data = page.locator("#react-burger-menu-btn")
    menu_data.click()

    logout_btn = page.locator("#logout_sidebar_link")
    logout_btn.click()

    login_btn = page.locator("#login-button[name='login-button']")

    assert login_btn.is_visible(), 'Logout is not done'

    print("All Tests Done")

