import configparser


def get_parser():
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    return parser


def platform_name():
    return get_parser().get("APPIUM_SETTINGS", "platform_name")


def platform_version():
    return get_parser().get("APPIUM_SETTINGS", "platform_version")


def app():
    return get_parser().get("APPIUM_SETTINGS", "app")


def device_name():
    return get_parser().get("APPIUM_SETTINGS", "device_name")


def server_url():
    return get_parser().get("APPIUM_SETTINGS", "server_url")
