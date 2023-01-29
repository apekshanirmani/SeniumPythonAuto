import traceback

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_browser():
    service_obj = Service("/drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()

    # driver.implicitly_wait(30)
    driver.get("https://qavbox.github.io/demo/signup/")
    assert "Registration" in driver.title

    """"
    # Assertion error handling
    try:
        name = driver.find_element(By.ID, "lblname")
        assert "Full Name1" in name.text
    except AssertionError:
        print(traceback.format_exc())

    # Element not found exception handling
    try:
        username = driver.find_element(By.ID, "username")
        username.send_keys("new value")
    except NoSuchElementException:
        print(traceback.format_exc())   
    """

    # Alert not found exception
    driver.switch_to.alert.accept()

    driver.quit()
