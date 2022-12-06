from playwright.sync_api import Page, expect


def test_show_multi_elements(page):

    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    country_options = page.locator("select[name='country'] option")
    print(country_options.count())
    print(country_options.all_inner_texts())
    print(country_options.first.inner_text())
    print(country_options.last.inner_text())

    i = 0
    while i < country_options.count():
        print(country_options.nth(i).inner_text())
        i += 1
