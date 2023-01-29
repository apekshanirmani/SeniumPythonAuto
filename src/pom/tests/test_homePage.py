import time

import pytest

from src.pom import properties
from src.pom.tests.base_test import BaseTest
from src.pom.utility import xReader


class TestHome(BaseTest):

    @pytest.mark.skip
    def test_product_item(self):
        self.loginPage.login(properties.username, properties.password)
        self.homePage.wait_for_element()

        print(self.homePage.get_item_count())
        assert self.homePage.get_item_count() == 6

        self.homePage.add_all_items_to_cart()
        print(self.homePage.get_total_count())
        assert self.homePage.get_total_count() == '6'

        self.homePage.remove_items_from_cart()
        assert self.homePage.get_total_count() == '4'
        print(self.homePage.get_total_count())

    def test_sorting_options(self):
        self.loginPage.login(properties.username, properties.password)
        self.homePage.wait_for_element()

        xReader.load_excel("C:/SWEDEN/Nirmani/Automation/PythonProject/SeniumPythonAuto/test_data.xlsx", "sortData")
        data = xReader.get_data_as_list_tuple()
        print(data)

        for item in data:
            self.homePage.sorting_the_items(item[0])
            time.sleep(2)
            assert self.homePage.get_first_item_name() == item[1]
            assert self.homePage.get_first_item_price() == '$' + str(item[2])
            time.sleep(3)
