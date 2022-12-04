from playwright.sync_api import Page, expect


def test_radio_button_check_verify(page) -> None:

    page.goto("https://fs2.formsite.com/meherpavan/form2/index.html")
    page.locator("//label[contains(@for,'RESULT_RadioButton')][.='Male']").check()
    page.wait_for_timeout(3000)
    assert page.locator("//label[contains(@for,'RESULT_RadioButton')][.='Male']").is_checked()
    page.locator("//label[contains(@for,'RESULT_RadioButton')][.='Female']").check()
    page.wait_for_timeout(2000)
    assert not page.locator("//label[contains(@for,'RESULT_RadioButton')][.='Male']").is_checked()
    page.wait_for_timeout(2000)
