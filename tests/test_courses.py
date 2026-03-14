import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        registration_email_input.fill('user.name@gmail.com')

        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        registration_username_input.fill('username')

        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_header = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_header).to_be_visible()
        expect(courses_header).to_have_text('Courses')

        empty_block_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_block_icon).to_be_visible()

        empty_block_header = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(empty_block_header).to_be_visible()
        expect(empty_block_header).to_have_text('There is no results')

        empty_block_description = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(empty_block_description).to_be_visible()
        expect(empty_block_description).to_have_text('Results from the load test pipeline will be displayed here')
