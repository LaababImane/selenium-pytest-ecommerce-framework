import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, ".name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price-container")
    ADD_TO_CART = (By.XPATH, "//a[text()='Add to cart']")

    def wait_for_page_load(self):
        time.sleep(3)  # wait for product details to load
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME), "Product name should be visible")  

    def get_product_name(self):
        return self.get_element_text(self.PRODUCT_NAME)
    
    def get_product_price(self):
        return self.get_element_text(self.PRODUCT_PRICE)
    
    def add_to_cart(self):
        self.wait_for_page_load()
        element = self.wait.until(EC.presence_of_element_located(self.ADD_TO_CART), "Add to Cart button should be present")
        self.driver.execute_script("arguments[0].click();", element)
        # Demoblaze shows a browser alert after adding to cart
        self.wait.until(EC.alert_is_present(), "Expected alert after adding to cart")
        alert = self.driver.switch_to.alert
        alert.accept()

    

    