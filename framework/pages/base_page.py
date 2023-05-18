from abc import ABC, abstractmethod
from framework.utils.waits import Wait


class BasePage(ABC):

    @abstractmethod
    def __init__(self, by_locator: tuple, name: str):
        self.__by_locator = by_locator
        self.__name = name

    def is_page_open(self) -> bool:
        element = Wait.wait_element_presence(self.__by_locator)
        return element.is_displayed()
