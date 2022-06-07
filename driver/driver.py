from appium import webdriver
from utils.config_reader import *


class Driver:
    __capabilities = {}
    __instance = None

    @classmethod
    def get_driver(cls):
        if cls.__instance is None:
            cls.configure_driver()
            cls.__instance = webdriver.Remote(command_executor=server_url(), desired_capabilities=cls.__capabilities)
        return cls.__instance

    @classmethod
    def close_driver(cls):
        cls.__instance.quit()
        cls.__instance = None

    @classmethod
    def configure_driver(cls):
        cls.__capabilities['app'] = app()
        cls.__capabilities['platformName'] = platform_name()
        cls.__capabilities['platformVersion'] = platform_version()
        cls.__capabilities['deviceName'] = device_name()
        cls.__capabilities['autoAcceptAlerts'] = True
