from playwright.sync_api import Page, expect


def test_basic_auth(create_context_auth) -> None:
    page = create_context_auth

    # basic_auth_link = page.locator("//a[text()='Basic Auth']")
    # basic_auth_link.click()

    result = page.locator("//p[contains(text(),'Congratulations!')]").inner_text()

    print(result)

    #expect(result).to_contain_text("Congratulations!")
    assert "Congratulations!" in result


def test_Digest_Auth(create_context_digest_auth) -> None:

    page = create_context_digest_auth

    result = page.locator("//p[contains(text(),'Congratulations!')]").inner_text()

    print(result)

    assert "Congratulations!" in result
