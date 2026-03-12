from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    page.wait_for_timeout(1000)

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill('user.name@gmail.com')

    page.wait_for_timeout(1000)

    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill('username')

    page.wait_for_timeout(1000)

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill('password')

    page.wait_for_timeout(1000)

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    page.wait_for_timeout(1000)

    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    page.wait_for_timeout(5000)
