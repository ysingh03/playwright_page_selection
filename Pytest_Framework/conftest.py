import pytest
from playwright.sync_api import Playwright


@pytest.fixture()
def set_up_tear_down(page) -> None:
    #page.set_viewport_size({"width": 1920, "height": 1000})
    page.goto("/")
    page.locator("//input[@id='user-name']").fill("standard_user", timeout=2000)
    page.locator("#password[data-test='password']").fill("secret_sauce")
    page.locator("#login-button[name='login-button']").click()

    yield page


@pytest.fixture()
def set_up_tear_down_invalid(page) -> None:
    #page.set_viewport_size({"width": 1920, "height": 1000})

    page.goto("/")
    yield page


@pytest.fixture()
def create_context_auth(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1500)
    context = browser.new_context(
        http_credentials={'username': 'admin', 'password': 'admin'},
        viewport={"width": 2560, "height": 1440}
    )
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    #page.set_viewport_size({"width": 2560, "height": 1440})
    yield page


@pytest.fixture()
def create_context_digest_auth(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1500)
    context = browser.new_context(
        http_credentials={'username': 'admin', 'password': 'admin'},
        viewport={"width": 2560, "height": 1440}
    )
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/digest_auth")
    #page.set_viewport_size({"width": 2560, "height": 1440})
    yield page