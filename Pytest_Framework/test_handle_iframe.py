from playwright.sync_api import Page


def test_handle_iframe_by_locator(page) -> None:
    page.goto("https://jqueryui.com/autocomplete/")
    page.frame_locator("iframe.demo-frame").locator("input#tags").fill("Automation testing")
    page.wait_for_timeout(2000)


def test_handle_iframe_by_id(page) -> None:
    page.goto("https://the-internet.herokuapp.com/iframe")
    input_area = page.frame("mce_0_ifr")
    input_area.locator("body#tinymce").fill("")
    page.wait_for_timeout(1000)
    input_area.locator("body#tinymce").fill("Automation Testing")
    page.wait_for_timeout(1500)


def test_handle_iframe_frame_by_name(page: Page) -> None:
    page.goto("https://rediff.com")
    iframe_data = page.frame("moneyiframe")
    # iframe_data = page.main_frame.child_frames[0]
    nse_index = iframe_data.locator("span#nseindex").inner_text()
    print(nse_index)
    page.wait_for_timeout(5000)
    for iframe in page.main_frame.child_frames:
        print(iframe.name)

    print(len(page.main_frame.child_frames))


def get_frame_by_index(parent_frame, index):
    return parent_frame.child_frames[index]


def test_handle_iframe_frame_by_index(page: Page) -> None:
    page.goto("https://rediff.com")
    # iframe_data = page.main_frame.child_frames[0]
    mf = page.main_frame
    iframe_locator = get_frame_by_index(mf, 0)
    nse_index = iframe_locator.locator("span#nseindex").inner_text()
    print(nse_index)
    page.wait_for_timeout(5000)
