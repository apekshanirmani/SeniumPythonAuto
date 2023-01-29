import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_browser():
    service_obj = Service("/drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://qavbox.github.io/demo/signup/")
    assert "Registration Form" in driver.title

    action = ActionChains(driver)
    el = driver.find_element(By.ID, "username")
    action.click(el).perform()
    action.send_keys("abcjd").perform()
    time.sleep(2)

    action.send_keys_to_element(el, "newValue").perform()
    time.sleep(2)
    driver.quit()
