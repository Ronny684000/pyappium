from driver.driver import Driver
from elements.abstract_element import AbstractElement


class Dropdown(AbstractElement):

    def __init__(self, locator, locator_type, option_locator_pattern, name):
        super().__init__(locator, locator_type, name)
        self.option_locator_pattern = option_locator_pattern

    def select_option(self, option_text):
        self.wait_for_display()
        self.click()
        option = Driver.get_driver().find_element(self.locator_type, self.option_locator_pattern.format(option_text))
        option.click()
