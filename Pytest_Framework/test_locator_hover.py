from playwright.sync_api import Page, expect


def test_element_with_hover_show(page) -> None:

    page.goto("https://globalsqa.com/demo-site")
    header_menu = page.locator("//a[text()='Free Ebooks' and @class = 'no_border']")
    #header_menu = page.locator("a.no_border", has_text="Free Ebooks")
    print(header_menu.inner_text())
    print(header_menu.text_content())
    header_menu.hover()
    page.wait_for_timeout(2000)


def get_header_submenu(submenu):
    return f"//div[@id='menu']//ul[@class='sub-menu']//a[contains(.,'{submenu}')]"


def get_sub_submenu(data):
    return f"//ul[@class='sub-menu']//div[@class='subsub_menu']//a[contains(.,'{data}')]"


def test_click_hover_menu(page) -> None:

    page.goto("https://globalsqa.com/demo-site")
    free_books_menu = page.locator("//a[text()='Free Ebooks' and @class = 'no_border']")
    free_books_menu.hover()

    page.wait_for_timeout(3000)
    all_free_ebooks = page.locator("//div[@id='menu']//li[@id='menu-item-7128']//li")
    print(all_free_ebooks.all_inner_texts())
    print(all_free_ebooks.count())

    free_deep_learning_book = page.locator(get_header_submenu('Free Deep Learning'))
    free_deep_learning_book.click()
    page.wait_for_timeout(2000)
    print(page.title())

    tester_link = page.locator("//li[@id='menu-item-2822']//a[contains(text(),'Tester’s Hub')]")
    tester_link.click()
    page.wait_for_timeout(2000)
    demo_sites = page.locator("//li[@id='menu-item-2822']//li[@id='menu-item-2823']")
    page.wait_for_timeout(2000)
    tester_hubs_books = page.locator(get_sub_submenu("Tooltip"))
    tester_hubs_books.click()
    page.wait_for_timeout(2000)
    print(page.title())

