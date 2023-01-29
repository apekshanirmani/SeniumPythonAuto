import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_browser():
    service_obj = Service("/drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()

    # driver.implicitly_wait(30)
    driver.get("https://qavbox.github.io/demo/signup/")
    assert "Registration" in driver.title

    click(driver, (By.ID, "username"))
    driver.refresh()
    send_keys(driver,(By.ID, "username"), "apeksha")
    time.sleep(5)
    driver.quit()


def click(driver, locator):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).click()


def send_keys(driver, locator, value):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).send_keys(value)
