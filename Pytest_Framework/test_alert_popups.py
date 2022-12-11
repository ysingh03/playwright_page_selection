from playwright.sync_api import Page


def test_click_js_alert(page: Page) -> None:
    '''

        Handle javascript alert pop-up

    '''

    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    js_alert_btn = page.locator("//button[contains(text(),'JS Alert')]")
    js_alert_btn.click()

    result_message = page.locator("p#result")
    assert result_message.inner_text() == "You successfully clicked an alert"


def test_click_js_confirm_alert(page: Page) -> None:

    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    js_confirm_alert_btn = page.locator("//button[contains(text(),'JS Confirm')]")
    page.on("dialog", lambda dialog: dialog.accept())
    js_confirm_alert_btn.click()

    result_message = page.locator("p#result")
    assert result_message.inner_text() == "You clicked: Ok"


def test_click_js_prompt_alert(page: Page) -> None:

    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    js_prompt_alert_btn = page.locator("//button[contains(text(),'JS Prompt')]")
    page.on("dialog", lambda dialog: print(dialog.message))
    page.on("dialog", lambda dialog: dialog.accept(prompt_text="Yogesh"))

    js_prompt_alert_btn.click()
    result_message = page.locator("p#result")
    assert result_message.inner_text() == "You entered: Yogesh"


