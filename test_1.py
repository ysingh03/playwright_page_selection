from playwright.sync_api import Playwright, sync_playwright, expect, Page


# def test_run(playwright: Playwright)-> None:
#     browser = playwright.chromium.launch(headless=False, slow_mo=3000)
#     context = browser.new_context()
#
#     page = context.new_page()
#
#     page.goto("https://google.com")
#
#     page.locator()

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.goto("https://www.way2automation.com/way2auto_jquery/index.php")
    page.get_by_role("heading", name="Dummy Registration Form").click()
    page.locator("input[name='name']").click()
    page.locator("input[name='name']").fill("Yogesh")
    page.locator("input[name=\"phone\"]").click()
    page.locator("input[name=\"phone\"]").fill("123456")
    page.locator("input[name=\"phone\"]").press("Tab")
    page.locator("input[name=\"email\"]").fill("abc@abc.com")
    page.locator("input[name=\"email\"]").press("Tab")
    page.get_by_role("combobox").select_option("India")
    page.get_by_role("combobox").press("Tab")
    page.locator("input[name=\"city\"]").fill("Mathura")
    page.locator("input[name=\"city\"]").press("Tab")
    page.get_by_role("button", name="Submit").click()

    context.tracing.stop(path="trace.zip")

    context.close()
    browser.close()
