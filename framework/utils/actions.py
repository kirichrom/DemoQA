from selenium.webdriver import ActionChains

from framework.browser.browser import Browser
from framework.utils.waits import Wait


class Action:

    @staticmethod
    def click_on_element(by_locator):
        Action.hover(by_locator)
        Wait.wait_to_be_clickable(by_locator).click()

    @staticmethod
    def get_data(by_locator: tuple, attr_name=None):
        """
        Returns the text if no parameter is passed to the function.
        Returns the attribute, if pass the attribute name.
        :param by_locator:
        :param attr_name:
        :return:
        """
        element = Wait.wait_element_presence(by_locator)
        if not attr_name:
            return element.text
        return element.get_attribute(attr_name)

    @staticmethod
    def hover(by_locator):
        element = Wait.wait_element_presence(by_locator)
        hover = ActionChains(Browser.get_driver()).move_to_element(element)
        hover.perform()

    @staticmethod
    def send_text(by_locator, text):
        text_box = Wait.wait_element_presence(by_locator)
        text_box.clear()
        text_box.send_keys(text)

    @staticmethod
    def is_visible(by_locator) -> bool:
        return Wait.wait_element_visible(by_locator).is_displayed()
