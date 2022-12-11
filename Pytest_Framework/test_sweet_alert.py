from playwright.sync_api import Page


def test_sweet_alert(page: Page) -> None:

    page.goto("https://sweetalert2.github.io/")
    page.wait_for_timeout(5000)
    message = page.locator("//button[contains(text(),'success message')]")

    message.click()

    alert_msg = page.locator("h2#swal2-title", timeout= 10000)
    msg_text = alert_msg.inner_text()
    assert msg_text == "Good job!"
    page.locator("button.swal2-confirm").click()

    assert not alert_msg.is_visible(), 'The sweet alert pop-up is not get close'
    