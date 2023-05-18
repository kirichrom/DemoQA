from abc import ABC, abstractmethod

from framework.utils.actions import Action


class BaseElement(ABC):

    @abstractmethod
    def __init__(self, by_locator: tuple, name: str):
        self._by_locator = by_locator
        self._name = name

    def get_name(self) -> str:
        return self._name

    def click(self):
        Action.click_on_element(self._by_locator)

    def get_text(self) -> str:
        """
        Returns the element text.
        :return:
        """
        return Action.get_data(self._by_locator)
