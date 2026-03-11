from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Заполняем поле Email
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill('user.name@gmail.com')

    # Заполняем поле Username
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill('username')

    # Заполняем поле Password
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill('password')

    # Нажимаем на кнопку Registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # После редиректа проверяем, что заголовок Dashboard отображается
    dashboard_header = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_header).to_be_visible()
    expect(dashboard_header).to_have_text('Dashboard')
