from playwright.sync_api import Page, Playwright, sync_playwright


def windows_handle(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/windows")

    page.locator("text='Click Here'").click()

    all_pages = context.pages
    page1 = all_pages[1]

    new_window_txt = page1.locator("//div[@class='example']/h3")
    print(new_window_txt.inner_text())
    print(page1.title())

    page.locator("text='Click Here'").click()
    all_pages = context.pages
    page2 = all_pages[2]
    page1.bring_to_front()
    page.wait_for_timeout(2000)

    page.bring_to_front()
    page.wait_for_timeout(2000)

    page2.bring_to_front()
    page.wait_for_timeout(2000)




    # page1 = context.new_page()
    #
    # page1.goto("https://google.com")
    page.wait_for_timeout(2000)

    context.close()
    browser.close()

with sync_playwright()  as playwright:
    windows_handle(playwright)


