from playwright.sync_api import Page, expect

def test_inner_text_get_from_element(page) -> None:

    page.goto("https://www.saucedemo.com/")

    page.locator("#login-button").click()
    error_text = page.locator("//h3[@data-test='error']").inner_text()
    print(error_text)
    error_text_1 = page.locator("//h3[@data-test='error']").text_content()
    print(error_text_1)

    assert error_text == error_text_1
