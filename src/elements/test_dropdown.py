from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_browser():
    service_obj = Service("/drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://qavbox.github.io/demo/signup/")
    assert "OrangeHRM" in driver.title
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()

    select = Select(driver.find_element(By.XPATH, ""))
    # Option 1
    # select.select_by_visible_text("Admin")

    # Option 2
    # select.select_by_value("female")

    # Option 3
    # select.select_by_index(2)

    # get all dropdown values and print the value text
    opts = select.options
    for opt in opts:
        print(opt.text)

    assert "Admin" in select.first_selected_option.text
    driver.quit()
