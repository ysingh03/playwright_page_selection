import time

from playwright.sync_api import Page, expect


def test_refresh(page: Page) -> None:
    page.goto("https://www.amazon.in/")
    time.sleep(3)
    page.reload()
    time.sleep(3)