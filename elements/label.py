from driver.driver import Driver
from elements.abstract_element import AbstractElement


class Label(AbstractElement):
    def __init__(self, locator, locator_type, name):
        super().__init__(locator, locator_type, name)

    def get_text(self):
        self.wait_for_display()
        return Driver.get_driver(). \
            find_element(self.locator_type, self.locator).text
