import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_browser():
    service_obj = Service("/drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()

    driver.get("https://qavbox.github.io/demo/delay/")

    # implicit wait - wait until element is present. if element is
    # already present but text is not present this is not work
    # driver.implicitly_wait(60)
    assert "Delay" in driver.title

    driver.find_element(By.XPATH, "//input[@name='commit1']").click()
    # print(driver.find_element(By.ID, "delay").text)

    WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element(By.XPATH("//h2[@id='delay']")), "I appeared "
                                                                                                     "after 5 sec")
    print(driver.find_element(By.XPATH, "//h2[@id='delay']").text)

    driver.quit()
