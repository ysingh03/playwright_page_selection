from playwright.sync_api import Page


def test_auto_await_ajax(page: Page)-> None:

    page.goto("http://uitestingplayground.com/ajax")
    ajax_btn = page.locator("button#ajaxButton")
    ajax_btn.click()

    success_msg = page.locator("p.bg-success")

    assert success_msg.inner_text() == 'Data loaded with AJAX get request.'



def test_hidden_element_visible(page: Page) -> None:

    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    start_btn = page.locator("//button[text()='Start']")
    start_btn.click()
    success_msg_hidden_ele = page.locator("//h4[text()='Hello World!']")

    assert success_msg_hidden_ele.inner_text() == "Hello World!"


def test_wait_for_visible_element(page: Page) -> None:

    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_btn = page.locator("//button[text()='Start']")
    start_btn.click()

    success_msg_hidden_ele = page.locator("//h4[text()='Hello World!']")

    assert success_msg_hidden_ele.inner_text() == "Hello World!"





