from elements.abstract_element import AbstractElement


class Button(AbstractElement):
    def __init__(self, locator, locator_type, name):
        super().__init__(locator, locator_type, name)
