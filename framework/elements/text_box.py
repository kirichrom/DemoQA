from framework.elements.base_element import BaseElement
from framework.utils.actions import Action


class TextBox(BaseElement):

    def __init__(self, by_locator: tuple, name: str):
        super(TextBox, self).__init__(by_locator=by_locator, name=name)

    def send_text(self, text: str):
        Action.send_text(self._by_locator, text)
