from playwright.sync_api import Page, expect


def test_select_single_select_list(page):
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    page.locator("//select[@name='country']").select_option(index=1)
    page.wait_for_timeout(2000)
    page.locator("//select[@name='country']").select_option(value="KH")
    page.wait_for_timeout(2000)
    page.locator("//select[@name='country']").select_option(label="India")
    page.wait_for_timeout(2000)
    page.locator("//select[@name='country']").select_option()
    page.wait_for_timeout(2000)

