from playwright.sync_api import Page, Playwright, expect, sync_playwright


def test_01_login(setup_tear_down) -> None:

    # page.goto("https://the-internet.herokuapp.com/login")
    #
    # page.locator("#username").fill("tomsmith")
    # page.locator("#password").fill("SuperSecretPassword!")
    # page.locator("i.fa-2x").click()

    page = setup_tear_down

    # login_message = page.locator("#flash").inner_text()
    #
    # print(login_message)
    #
    # assert 'logged into a secure area' in login_message

    logout_buttons = page.locator("//i[text()=' Logout']/parent::a")

    assert logout_buttons.is_visible()


def test_02_login_logout(setup_tear_down) -> None:

    # page.goto("https://the-internet.herokuapp.com/login")
    #
    # page.locator("#username").fill("tomsmith")
    # page.locator("#password").fill("SuperSecretPassword!")
    # page.locator("i.fa-2x").click()
    page = setup_tear_down

    page.locator("//i[text()=' Logout']/parent::a").click()

    logout_verification_message = page.locator("div.flash").inner_text()

    print(logout_verification_message)

    assert 'logged out of the secure area' in logout_verification_message




