from selenium.webdriver import ActionChains

from framework.browser.browser import Browser
from framework.utils.waits import Wait


class Action:

    @staticmethod
    def click_on_element(by_locator: tuple):
        Action.hover(by_locator=by_locator)
        Wait.wait_to_be_clickable(by_locator=by_locator).click()

    @staticmethod
    def get_data(by_locator: tuple, attr_name=None) -> str:
        """
        Returns the text if no parameter is passed to the function.
        Returns the attribute, if pass the attribute name.
        :param by_locator:
        :param attr_name:
        :return:
        """
        element = Wait.wait_element_presence(by_locator=by_locator)
        if not attr_name:
            return element.text
        return element.get_attribute(attr_name)

    @staticmethod
    def hover(by_locator: tuple) -> None:
        element = Wait.wait_element_presence(by_locator=by_locator)
        hover = ActionChains(driver=Browser.get_driver()).move_to_element(element)
        hover.perform()

    @staticmethod
    def send_text(by_locator: tuple, text: str) -> None:
        text_box = Wait.wait_element_presence(by_locator)
        text_box.clear()
        text_box.send_keys(text)
