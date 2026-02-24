import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):

    # Nav buttons
    LOGIN_NAV = (By.ID, "login2")
    SIGNUP_NAV = (By.ID, "signin2")
    LOGOUT_NAV = (By.ID, "logout2")
    NAV_USERNAME = (By.ID, "nameofuser")
    CART_NAV = (By.ID, "cartur")
    LOGIN_MODAL = (By.ID, "logInModal")

    # Search/categories
    PHONES_CAT = (By.XPATH, "//a[text()='Phones']")
    LAPTOPS_CAT = (By.XPATH, "//a[text()='Laptops']")
    MONITORS_CAT = (By.XPATH, "//a[text()='Monitors']")

    PRODUCTS = (By.CLASS_NAME, "card-title")

    def open(self):
        self.driver.get(self.BASE_URL)

    def go_to_login(self):
        self.click(self.LOGIN_NAV)

        self.wait.until(EC.visibility_of_element_located(self.LOGIN_MODAL))
    
    def go_to_signup(self):
        self.click(self.SIGNUP_NAV)

    def go_to_cart(self):
        self.click(self.CART_NAV)

    def is_logged_in(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.NAV_USERNAME))
            text = self.get_element_text(self.NAV_USERNAME)
            return "Welcome" in text
        except: 
            return False
        
    def select_category(self, category):
        categories = {
            "phones": self.PHONES_CAT,  
            "laptops": self.LAPTOPS_CAT,
            "monitors": self.MONITORS_CAT
        }
        self.click(categories[category.lower()])

    def click_first_product(self):
        self.click(self.PRODUCTS)

    def click_product_by_name(self, name):
        time.sleep(5)  # wait for products to load
        product = (By.XPATH, f"//a[text()='{name}']")
        element = self.wait.until(EC.presence_of_element_located(product))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)