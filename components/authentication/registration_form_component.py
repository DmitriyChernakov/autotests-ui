import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page=page, locator='registration-form-email-input', name='Email')
        self.username_input = Input(page=page, locator='registration-form-username-input', name='Username')
        self.password_input = Input(page=page, locator='registration-form-password-input', name='Password')

    @allure.step("Fill registration form")
    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(value=email)
        self.email_input.check_have_value(value=email)

        self.username_input.fill(value=username)
        self.username_input.check_have_value(value=username)

        self.password_input.fill(value=password)
        self.password_input.check_have_value(value=password)

    @allure.step("Check visible registration form")
    def check_visible(self, email: str, username: str, password: str):
        self.email_input.check_visible()
        self.email_input.check_have_value(value=email)

        self.username_input.check_visible()
        self.username_input.check_have_value(value=username)

        self.password_input.check_visible()
        self.password_input.check_have_value(value=password)
