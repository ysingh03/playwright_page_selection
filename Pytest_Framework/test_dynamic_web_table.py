from playwright.sync_api import Page, expect


def test_dynamic_web_table(page) -> None:

    page.goto("https://primefaces.org/primeng/table")

    rows = page.locator("//*[@class = 'card']//tr")

    row = rows.locator(":scope", has_text="Lenna Paprocki")

    checkbox = row.locator("div.p-checkbox-box")
    checkbox.click()

    expect(checkbox).to_be_checked()

    # print all data from the table

    index = 1

    while index < rows.count():
        print(rows.nth(index).inner_text())
        index += 1


    # get the balance of a customer

    balance = rows.locator(":scope", has_text='Simona Morasca').locator("//span[text()='Balance']/parent::td")
    print(balance.inner_text())
    print(balance.text_content())

    expect(balance).to_contain_text('50,041.00')


