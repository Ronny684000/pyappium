from selenium.webdriver.common.by import By

from driver.driver import Driver
from elements.abstract_element import AbstractElement


class InputField(AbstractElement):
    def __init__(self, locator, locator_type, name):
        super().__init__(locator, locator_type, name)

    def send_text(self, text_to_send):
        self.wait_for_display()
        element = Driver.get_driver(). \
            find_element(self.locator_type, self.locator)
        self.click()
        element.send_keys(text_to_send)
