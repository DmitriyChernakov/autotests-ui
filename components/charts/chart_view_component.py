from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.title = Text(page=page, locator=f'{identifier}-widget-title-text', name='Title')
        self.chart = Image(page=page, locator=f'{identifier}-{chart_type}-chart', name='Chart')

    def check_visible(self, title: str):
        self.title.check_visible()
        self.title.check_have_text(text=title)

        self.chart.check_visible()
