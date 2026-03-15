from typing import Any, Generator
from playwright.sync_api import sync_playwright, Page, Playwright

import pytest


@pytest.fixture
def chromium_page(playwright: Playwright) -> Generator[Page, Any, None]:
    """Фикстура для инициализации и открытия новой страницы."""
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()
