from framework.browser.browser import Browser
from framework.utils.json_reader import JsonReader
from project.resources import path


class BrowserUtils:

    @staticmethod
    def go_to_base_url():
        url = JsonReader().read_data('url', 'base_url', directory=path.test_config_path)
        Browser.get_driver().get(url)
