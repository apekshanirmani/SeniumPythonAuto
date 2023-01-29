from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://sitdladmin.hnb.lk/")
assert "HNB" in driver.title
print(driver.title)
#driver.find_element(By.ID, " ").click()
driver.save_screenshot("/screenshots/test.png")
driver.quit()


