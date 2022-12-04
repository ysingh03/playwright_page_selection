import pytest
from playwright.sync_api import expect, Page, Playwright


@pytest.mark.sanity
def test_01_login_with_valid_credentials(set_up_tear_down) -> None:
    page = set_up_tear_down

    # page.locator("//input[@id='aauser-name']").fill("standard_user", timeout=1000)
    product_header = page.locator("//span[text()='Products']")

    assert product_header.is_visible(), "User is unable to login"
    print("First test done")


@pytest.mark.regression
def test_02_logout(set_up_tear_down) -> None:
    page = set_up_tear_down

    # page.locator("//input[@id='aauser-name']").fill("standard_user", timeout=1000)

    # product_header = page.locator("//span[text()='Products']")

    menu_data = page.locator("#react-burger-menu-btn")
    menu_data.click()
    page.screenshot(path="screenshot/screenshot.png")
    # page.screenshot(path="screenshot/screenshot.png", full_page=True)

    logout_btn = page.locator("#logout_sidebar_link")
    logout_btn.click()

    login_btn = page.locator("#login-button[name='login-button']")

    assert login_btn.is_visible(), 'Logout is not done'

    print("All Tests Done")


@pytest.mark.sanity
def test_03_login_invalid_credentials(set_up_tear_down_invalid):
    page = set_up_tear_down_invalid
    page.locator("//input[@id='user-name']").fill("standard_user", timeout=2000)
    page.locator("#password[data-test='password']").fill("wrong_sauce")
    page.locator("#login-button[name='login-button']").click()
    error_message = page.locator("//h3[@data-test='error']")

    error_message.wait_for()
    actual_error_text = "Username and password do not match any user in this service"

    assert actual_error_text in error_message.inner_text()


@pytest.mark.regression
@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"),
                                                ("performance_glitch_user", "secret_sauce")])
def test_04_multiple_login_credentials(set_up_tear_down_invalid, username, password):
    page = set_up_tear_down_invalid
    page.locator("//input[@id='user-name']").fill(username, timeout=2000)
    page.locator("#password[data-test='password']").fill(password)
    page.locator("#login-button[name='login-button']").click()

    product_header = page.locator("//span[text()='Products']")

    assert product_header.is_visible(), "User is unable to login"


@pytest.mark.regression
@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"),
                                                pytest.param("locked_out_user", "secret_sauce",
                                                             marks=pytest.mark.xfail),
                                                ("performance_glitch_user", "secret_sauce")])
def test_05_multiple_login_with_xfail(set_up_tear_down_invalid, username, password):
    page = set_up_tear_down_invalid
    page.locator("//input[@id='user-name']").fill(username, timeout=2000)
    page.locator("#password[data-test='password']").fill(password)
    page.locator("#login-button[name='login-button']").click()

    product_header = page.locator("//span[text()='Products']")

    assert product_header.is_visible(), "User is unable to login"
