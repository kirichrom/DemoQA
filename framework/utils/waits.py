from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.browser.browser import Browser
from framework.utils.json_reader import JsonReader


class Wait:

    @staticmethod
    def wait_to_be_clickable(by_locator):
        element = WebDriverWait(Browser.get_driver(), JsonReader().read_data('browser', 'timeout')).until(
            EC.element_to_be_clickable(by_locator))
        return element

    @staticmethod
    def wait_element_presence(by_locator):
        element = WebDriverWait(Browser.get_driver(), JsonReader().read_data('browser', 'timeout')).until(
            EC.presence_of_element_located(by_locator))
        return element

    @staticmethod
    def wait_element_visible(by_locator):
        element = WebDriverWait(Browser.get_driver(), JsonReader().read_data('browser', 'timeout')).until(
            EC.visibility_of_element_located(by_locator))
        return element
