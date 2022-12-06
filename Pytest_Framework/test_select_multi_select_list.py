from playwright.sync_api import Page, expect


def test_multi_selections_dropdown(page) -> None:
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    page.locator("//select[@name='Month']").select_option(value='Feb', index=6, label='October')
    page.wait_for_timeout(3000)
    page.locator("//select[@name='Month']").select_option()
    page.wait_for_timeout(2000)


def test_selected_value_from_dropdown(page) -> None:
    page.goto("https://the-internet.herokuapp.com/dropdown")
    check_select = page.locator("select[id=dropdown]").select_option(label='Option 2')
    page.wait_for_timeout(2000)
    selected_value = page.locator("select[id='dropdown'] > option[selected=selected]")

    assert selected_value.inner_text() == 'Option 2'
