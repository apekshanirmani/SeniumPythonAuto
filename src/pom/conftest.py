import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from src.pom import properties
from src.pom.pages.home_page import HomePage
from src.pom.pages.login_page import LoginPage

driver = None


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


class BasePage:
    pass


@pytest.fixture
def get_driver(request, get_browser):
    global driver
    print("Enter browser: " + get_browser)

    if get_browser == "chrome":
        # service_obj = Service("/drivers/chromedriver.exe")
        service_obj = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service_obj)
        driver = webdriver.Chrome(service=service_obj)

    elif get_browser == "firefox":
        # pass
        driver = webdriver.Firefox(GeckoDriverManager().install())

    """"
    # setup an environment
    env = request.config.getoption("--env")
    _driver.get("https://www." + env + ".saucedemo.com/")  
    """

    driver.get(properties.url)
    driver.maximize_window()
    driver.implicitly_wait(30)

    # Passing driver object to base page
    # request.cls.driver = BasePage(_driver)

    # Passing driver object to login page
    request.cls.loginPage = LoginPage(driver)
    request.cls.homePage = HomePage(driver)

    yield driver
    driver.quit()
