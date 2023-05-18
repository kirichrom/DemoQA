from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from framework.utils.json_reader import JsonReader


class BrowserFactory:
    @staticmethod
    def get_webdriver():
        browser_name = JsonReader().read_data('browser', 'browser_name')
        browser_options = JsonReader().read_data('browser', 'options')
        if browser_name == 'firefox':
            firefox_options = webdriver.FirefoxOptions()
            for option in browser_options:
                firefox_options.add_argument(option)
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                     options=firefox_options)

        elif browser_name == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            for option in browser_options:
                chrome_options.add_argument(option)
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

