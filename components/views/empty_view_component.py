from playwright.sync_api import Page
import allure
from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page=page, locator=f'{identifier}-empty-view-icon', name='Icon')
        self.title = Text(page=page, locator=f'{identifier}-empty-view-title-text', name='Title')
        self.description = Text(page=page, locator=f'{identifier}-empty-view-description-text', name='Description')

    @allure.step("Check visible empty view {title}")
    def check_visible(self, title: str, description: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(text=title)

        self.description.check_visible()
        self.description.check_have_text(text=description)
