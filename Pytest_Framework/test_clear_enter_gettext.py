import time

from playwright.sync_api import Page, expect


def clear_the_data(page, loc):
    page.locator(loc).press("Control+KeyA")
    page.locator(loc).press("Backspace")


def test_example_page(page) -> None:
    page.goto("https://the-internet.herokuapp.com/login")

    page.set_viewport_size({"width": 1980, "height": 1140})

    page.locator("#username").fill("test")

    # to clear the data from username     
    # 1 to clear the data 
    # page.locator("#username").fill("")
    # 2 to clear the data by custom function
    clear_the_data(page, "#username")

    page.locator("#username").type("tomsmith")
    time.sleep(2)
