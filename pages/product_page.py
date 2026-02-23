from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, ".name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price-container")
    ADD_TO_CART = (By.XPATH, "//button[text()='Add to cart']")

    def get_product_name(self):
        return self.get_element_text(self.PRODUCT_NAME)
    
    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

    