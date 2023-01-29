import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from src.fixtures import properties


def pytest_addoption(parser):
    # get browser from command line
    # parser.addoption("--browser", action="store", default="chrome")

    # get browser from property file
    parser.addoption("--browser", action="store", default=properties.browser)

    # setup env
    parser.addoption("--env", action="store", default=properties.env)


@pytest.fixture
def get_browser(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture
def get_driver(request, get_browser):
    _driver = None
    print("Enter browser: " + get_browser)

    if get_browser == "chrome":
        service_obj = Service("/drivers/chromedriver.exe")
        _driver = webdriver.Chrome(service=service_obj)

    elif get_browser == "firefox":
        pass

    env = request.config.getoption("--env")
    _driver.get("https://www." + env + ".saucedemo.com/")
    _driver.maximize_window()
    _driver.implicitly_wait(30)
    request.cls.driver = _driver
    yield request.cls.driver
    request.cls.driver.quit()
