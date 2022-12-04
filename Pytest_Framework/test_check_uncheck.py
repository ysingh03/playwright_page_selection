from playwright.sync_api import Page, expect


def get_days_check(day):
    return f"//label[contains(@for,'RESULT_CheckBox')][.='{day}']"


def test_check_uncheck_box(page) -> None:
    page.goto("https://fs2.formsite.com/meherpavan/form2/index.html")
    page.wait_for_timeout(2000)
    #page.locator(get_days_check('Thursday')).click()
    #we can use below also to click the locator
    page.locator(get_days_check('Thursday')).click(force=True)
    page.wait_for_timeout(2000)

    assert page.locator(get_days_check('Thursday')).is_checked()
    page.locator(get_days_check('Thursday')).click()
    assert not page.locator(get_days_check('Thursday')).is_checked()
