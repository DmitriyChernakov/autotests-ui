import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_header = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_header).to_be_visible()
    expect(courses_header).to_have_text('Courses')

    empty_block_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_block_icon).to_be_visible()

    empty_block_header = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_block_header).to_be_visible()
    expect(empty_block_header).to_have_text('There is no results')

    empty_block_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_block_description).to_be_visible()
    expect(empty_block_description).to_have_text('Results from the load test pipeline will be displayed here')
