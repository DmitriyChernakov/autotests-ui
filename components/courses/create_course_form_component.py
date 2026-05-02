import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = Input(page=page, locator='create-course-form-title-input', name='Title')
        self.estimated_time_input = Input(
            page=page,
            locator='create-course-form-estimated-time-input',
            name='Estimated time',
        )
        self.description_textarea = Textarea(
            page=page,
            locator='create-course-form-description-input',
            name='Description',
        )
        self.max_score_input = Input(page=page, locator='create-course-form-max-score-input', name='Max score')
        self.min_score_input = Input(page=page, locator='create-course-form-min-score-input', name='Min score')

    @allure.step("Fill create course form for course {title}")
    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title_input.fill(value=title)
        self.title_input.check_have_value(value=title)

        self.estimated_time_input.fill(value=estimated_time)
        self.estimated_time_input.check_have_value(value=estimated_time)

        self.description_textarea.fill(value=description)
        self.description_textarea.check_have_value(value=description)

        self.max_score_input.fill(value=max_score)
        self.max_score_input.check_have_value(value=max_score)

        self.min_score_input.fill(value=min_score)
        self.min_score_input.check_have_value(value=min_score)

    @allure.step("Check visible create course form")
    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title_input.check_visible()
        self.title_input.check_have_value(value=title)

        self.estimated_time_input.check_visible()
        self.estimated_time_input.check_have_value(value=estimated_time)

        self.description_textarea.check_visible()
        self.description_textarea.check_have_value(value=description)

        self.max_score_input.check_visible()
        self.max_score_input.check_have_value(value=max_score)

        self.min_score_input.check_visible()
        self.min_score_input.check_have_value(value=min_score)
