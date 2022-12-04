import time

import pytest

from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.fixture(scope="session")
def create_browser_context(playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("i.fa-2x").click()
    context.storage_state(path="state.json")
    yield context


@pytest.fixture()
def setup_tear_down(create_browser_context, browser) -> None:

    context = browser.new_context(storage_state="state.json")
    #context = create_browser_context
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/secure")

    yield page
    context.clear_cookies()
    context.close()
    time.sleep(5)

