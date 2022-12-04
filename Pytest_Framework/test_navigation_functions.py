from playwright.sync_api import Playwright, expect, sync_playwright, Page


def test_navigation_operations(page) -> None:
    page.goto("https://www.google.com")

    print(page.url)
    expected_url = page.url
    actual_url = 'https://www.google.com/'

    assert actual_url == expected_url

    # Click the gmail link to open the gmail site

    page.locator("//a[text()='Gmail']").click()

    print(page.url)
    expected_url1 = page.url
    actual_url1 = "https://www.google.com/intl/en-GB/gmail/about/"

    # Navigator back
    page.go_back()

    print(page.url)
    expected_url2 = page.url
    actual_url2 = 'https://www.google.com/'
    assert actual_url2 == expected_url2

    # Navigator forward
    page.go_forward()

    print(page.url)
    expected_url3 = page.url
    actual_url3 = 'https://www.google.com/intl/en-GB/gmail/about/'
    assert actual_url3 == expected_url3
