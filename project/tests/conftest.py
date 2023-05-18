import pytest

from framework.browser.browser import Browser


@pytest.fixture(autouse=True)
def driver():
    web_driver = Browser.get_driver()
    yield web_driver
    Browser.quit_driver()
