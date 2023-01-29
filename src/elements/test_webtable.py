import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_browser():
    service_obj = Service("/drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://qavbox.github.io/demo/webtable/")
    assert "webtable" in driver.title

    table = driver.find_element(By.ID, "table01")
    header = table.find_elements(By.TAG_NAME, "th")

    body = table.find_element(By.TAG_NAME, "tbody")
    rows = table.find_elements(By.TAG_NAME, "tr")
    cells = body.find_elements(By.TAG_NAME, "td")

    """"
    # Print all the cells
    for cell in cells:
        print(cell.text)
    """

    # Select a row base on a given value & delete it
    for i in range(len(rows)):
        columns = rows[i].find_elements(By.TAG_NAME, "td")
        for j in range(len(columns)):
            if columns[j].text == "TFS":
                columns[0].click()

    # Print the row counts
    print(len(rows))

    driver.quit()
