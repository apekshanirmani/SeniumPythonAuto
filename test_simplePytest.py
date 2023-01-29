from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class DriverSetup:
    driver = None


def test_browser():
    service_obj = Service("/drivers/chromedriver.exe")
    DriverSetup.driver = webdriver.Chrome(service=service_obj)
    DriverSetup.driver.maximize_window()
    DriverSetup.driver.implicitly_wait(30)


def test_test1():
    DriverSetup.driver.get("https://sitdladmin.hnb.lk/")
    assert "HNB2" in DriverSetup.driver.title
    print(DriverSetup.driver.title)
    # driver.find_element(By.ID, " ").click()
    DriverSetup.driver.save_screenshot("/screenshots/test.png")
    DriverSetup.driver.quit()
