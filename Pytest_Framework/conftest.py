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

