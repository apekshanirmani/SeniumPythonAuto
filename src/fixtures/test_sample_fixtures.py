
from selenium.webdriver.common.by import By
from src.fixtures.base_test import BaseTest


class TestFixtureSample(BaseTest):

    def test_login(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

    def test_get_count(self, get_driver):
        driver = self.driver
        driver.find_element(By.ID, "password")
