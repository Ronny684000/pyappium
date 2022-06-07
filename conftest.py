import pytest

from driver.driver import Driver


@pytest.fixture(autouse=True)
def set_up():
    yield
    Driver.get_driver().close()

