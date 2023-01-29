from selenium.webdriver.common.by import By

from src.pom.pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    product_text = (By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']")
    inventory_item = (By.CSS_SELECTOR, ".inventory_item")
    total_item_count =(By.XPATH, "//span[@class='shopping_cart_badge']")
    remove_first_item = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) .btn_inventory")
    remove_second_item = (By.CSS_SELECTOR, ".inventory_item:nth-child(2) .btn_inventory")
    sort_selector = (By.CSS_SELECTOR, ".product_sort_container")
    first_product_name = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_name")
    first_product_price = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price")

    def wait_for_element(self):
        self.wait_for(self.product_text)

    def get_item_count(self):
        return self.get_count(self.inventory_item)

    def add_all_items_to_cart(self):
        for i in range(1, self.get_item_count()+1):
            self.click((By.CSS_SELECTOR, ".inventory_item:nth-child("+str(i)+") .btn_inventory"))

    def get_total_count(self):
        return self.get_text(self.total_item_count)

    def remove_items_from_cart(self):
        self.click(self.remove_first_item)
        self.click(self.remove_second_item)

    def sorting_the_items(self, option):
        self.select_dropdown_option(self.sort_selector, option)

    def get_first_item_name(self):
        return self.get_text(self.first_product_name)

    def get_first_item_price(self):
        return self.get_text(self.first_product_price)
