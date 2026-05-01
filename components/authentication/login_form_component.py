import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page=page, locator='login-form-email-input', name='Email')
        self.password_input = Input(page=page, locator='login-form-password-input', name='Password')

    @allure.step("Fill login form")
    def fill(self, email: str, password: str):
        self.email_input.fill(value=email)
        self.email_input.check_have_value(value=email)

        self.password_input.fill(value=password)
        self.password_input.check_have_value(value=password)

    @allure.step("Check visible login form")
    def check_visible(self, email, password):
        self.email_input.check_visible()
        self.email_input.check_have_value(value=email)

        self.password_input.check_visible()
        self.password_input.check_have_value(value=password)
