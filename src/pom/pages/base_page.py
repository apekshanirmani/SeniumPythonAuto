from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def click(self, locator):
        self.wait.until(EC.presence_of_element_located(locator)).click()

    def send_keys(self, locator, value):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(value)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).get_attribute("innerText")

    def wait_for(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def get_count(self, locator):
        return len(self.wait.until(EC.presence_of_all_elements_located(locator)))

    def get_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def select_dropdown_option(self, locator, option):
        select = Select(self.get_element(locator))
        select.select_by_visible_text(option)
