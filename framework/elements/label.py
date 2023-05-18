from framework.elements.base_element import BaseElement


class Label(BaseElement):

    def __init__(self, by_locator, name):
        super().__init__(by_locator=by_locator, name=name)
