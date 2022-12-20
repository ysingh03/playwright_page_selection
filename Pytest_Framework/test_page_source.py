from playwright.sync_api import Page


def test_page_source_view(page: Page) -> None:

    page.goto("https://google.com")
    site_page = page.content()
    print(site_page)
