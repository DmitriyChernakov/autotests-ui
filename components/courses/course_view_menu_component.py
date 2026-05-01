import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page=page, locator='course-view-menu-button', name='Menu')
        self.edit_menu_button = Button(page=page, locator='course-view-edit-menu-item', name='Edit')
        self.delete_menu_button = Button(page=page, locator='course-view-delete-menu-item', name='Delete')

    @allure.step("Open course menu at index {index} and click edit")
    def click_edit(self, index: int):
        self.menu_button.click(nth=index)

        self.edit_menu_button.check_visible(nth=index)
        self.edit_menu_button.click(nth=index)

    @allure.step("Open course menu at index {index} and click delete")
    def click_delete(self, index: int):
        self.menu_button.click(nth=index)

        self.delete_menu_button.check_visible(nth=index)
        self.delete_menu_button.click(nth=index)
