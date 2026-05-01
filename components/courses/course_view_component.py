import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements.image import Image
from elements.text import Text


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)

        self.title = Text(page=page, locator='course-widget-title-text', name='Title')
        self.image = Image(page=page, locator='course-preview-image', name='Preview')
        self.max_score_text = Text(page=page, locator='course-max-score-info-row-view-text', name='Max score')
        self.min_score_text = Text(page=page, locator='course-min-score-info-row-view-text', name='Min score')
        self.estimate_time_text = Text(
            page=page,
            locator='course-estimated-time-info-row-view-text',
            name='Estimated time'
        )

    @allure.step("Check visible course view at index {index}")
    def check_visible(self, index: int, title: str, max_score: str, min_score: str, estimated_time: str):
        self.image.check_visible(nth=index)

        self.title.check_visible(nth=index)
        self.title.check_have_text(text=title, nth=index)

        self.max_score_text.check_visible()
        self.max_score_text.check_have_text(text=f'Max score: {max_score}', nth=index)

        self.min_score_text.check_visible()
        self.min_score_text.check_have_text(text=f'Min score: {min_score}', nth=index)

        self.estimate_time_text.check_visible()
        self.estimate_time_text.check_have_text(text=f'Estimated time: {estimated_time}', nth=index)
