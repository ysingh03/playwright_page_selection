from playwright.sync_api import Page


def get_selected_subject(page, subject):
    subjects_list = page.locator("//div[contains(@class,'subjects-auto-complete__menu-list')]/div")
    index = 0

    while index < subjects_list.count():
        if subjects_list.nth(index).inner_text() == subject:
            subjects_list.nth(index).click()
        index += 1


def get_subjects_autosuggestion(subject):
    return f"//div[contains(@class, 'subjects-auto-complete__menu-list')]/div[text()='{subject}']"



def selected_subject2(page, subject):
    subject_autoshow = page.locator(get_subjects_autosuggestion(subject))
    subject_autoshow.click()


def test_automation_dropdown(page) -> None:
    page.goto("https://demoqa.com/automation-practice-form")
    select_subject = page.locator("input#subjectsInput")
    select_subject.fill("M")
    # div.subjects-auto-complete__menu-list

    get_selected_subject(page, 'Maths')

    select_subject.fill("P")
    get_selected_subject(page, "Physics")
    select_subject.fill("E")
    get_selected_subject(page, "English")


def test_automation_dropdown1(page) -> None:
    page.goto("https://demoqa.com/automation-practice-form")
    select_subject = page.locator("input#subjectsInput")
    select_subject.fill("M")
    selected_subject2(page, "Maths")
    select_subject.fill("P")
    selected_subject2(page, "Physics")
    select_subject.fill("E")
    selected_subject2(page, "English")


