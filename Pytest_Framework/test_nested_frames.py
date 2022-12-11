from playwright.sync_api import Page


def test_nested_frame_to_frames(page: Page) -> None:

    page.goto("https://the-internet.herokuapp.com/nested_frames")
    top_frame = page.main_frame.child_frames[0]
    left_frame = top_frame.child_frames[0]
    middle_frame = top_frame.child_frames[1]
    right_frame = top_frame.child_frames[2]
    left_frame_name = left_frame.locator("body")
    middle_frame_name = middle_frame.locator("body")
    right_frame_name = right_frame.locator("body")

    print(left_frame_name.inner_text())
    print(middle_frame_name.inner_text())
    print(right_frame_name.inner_text())

