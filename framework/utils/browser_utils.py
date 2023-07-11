from selenium.common import JavascriptException

from framework.browser.browser import Browser
from framework.utils.json_reader import JsonReader
from project.resources import path


class BrowserUtils:

    @staticmethod
    def go_to_base_url() -> None:
        url = JsonReader().read_data('url', 'base_url', directory=path.test_config_path)
        Browser.get_driver().get(url=url)

    @staticmethod
    def execute_js_script(function: str) -> None:
        try:
            Browser.get_driver().execute_script(function)
        except JavascriptException:
            pass

