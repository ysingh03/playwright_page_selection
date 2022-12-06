from playwright.sync_api import Page, expect


def get_loc_city(city):
    '''

    :param city:
    :return: it return xpath for city
    '''

    return f"//div[text()='{city}']"


def test_handle_dynamic_dropdown(page) -> None:

    page.goto("https://www.spicejet.com")
    from_input = page.locator("//div[@data-testid='to-testID-origin']/div/div[2]/input")
    from_input.click()
    from_input.fill("ag")
    page.locator(get_loc_city('Agra')).click()
    to_input = page.locator("//div[@data-testid='to-testID-destination']/div/div[2]/input")
    to_input.click()
    to_input.fill("ja")
    page.locator(get_loc_city('JAI')).click()
