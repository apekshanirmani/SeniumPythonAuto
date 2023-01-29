from src.pom import properties
from src.pom.tests.base_test import BaseTest


class TestLogin(BaseTest):

    def test_valid_login(self):
        self.loginPage.login(properties.username, properties.password)

    def test_locked_user_login(self):
        self.loginPage.login(properties.locked_username, properties.password)
        assert "Epic sadface: Sorry, this user has been locked out" in self.loginPage.get_locked_user_error()