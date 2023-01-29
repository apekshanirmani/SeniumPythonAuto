import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_browser():
    service_obj = Service("/drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://qavbox.github.io/demo/dragndrop/")
    assert "DragnDrop" in driver.title

    action = ActionChains(driver)
    source1 = driver.find_element(By.ID, "draggable")
    target1 = driver.find_element(By.ID, "droppable")

    # Option 1
    # action.drag_and_drop(source=source1, target=target1).perform()

    # Option 2
    # action.click_and_hold(source1).pause(2).move_to_element(target1).perform()

    # Option 3
    # action.drag_and_drop_by_offset(source=source1, xoffset=100, yoffset=100).perform()

    # Option 4
    # action.click_and_hold(source1).pause(2).move_to_element_with_offset(target1, 100, 200).perform()

    time.sleep(2)
    assert "Dropped!" in target1.text

    driver.quit()
