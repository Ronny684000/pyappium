import logging

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from driver.driver import Driver


class AbstractElement:
    def __init__(self, locator, locator_type, name):
        self.locator = locator
        self.name = name
        self.locator_type = locator_type

    def wait_for_display(self):
        try:
            return WebDriverWait(Driver.get_driver(), 30).until(
                expected_conditions.presence_of_element_located((self.locator_type, self.locator)))
        except TimeoutError:
            logging.error("Element is not displayed")

    def click(self):
        self.wait_for_display()
        element = Driver.get_driver(). \
            find_element(self.locator_type, self.locator)
        self.wait_for_display()
        element.click()
