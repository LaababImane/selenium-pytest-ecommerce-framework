from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, "#tbodyid > tr")
    TOTAL_PRICE = (By.ID, "totalp")
    PLACE_ORDER_BTN = (By.XPATH, "//button[text()='Place Order']")
    DELETE_BTN = (By.XPATH, "//a[text()='Delete']")

    # Place order modal fields
    ORDER_NAME = (By.ID, "name")
    ORDER_COUNTRY = (By.ID, "country")
    ORDER_CITY = (By.ID, "city")
    ORDER_CARD = (By.ID, "card")
    ORDER_MONTH = (By.ID, "month")
    ORDER_YEAR = (By.ID, "year")
    PURCHASE_BTN = (By.XPATH, "//button[text()='Purchase']")
    CONFIRM_MESSAGE = (By.CSS_SELECTOR, ".sweet-alert")
    CINFIRM_OK_BTN = (By.XPATH, "//button[text()='OK']")

    def open(self):
        self.driver.get(f"{self.BASE_URL}/cart.html")
        time.sleep(2)  # wait for cart to load

    def get_cart_items(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.CART_ITEMS))
            return self.driver.find_elements(*self.CART_ITEMS)
        except:
            return []
    
    def get_item_names(self):
        items = self.get_cart_items()
        names = []
        for item in items:
            try:
                cols = item.find_elements(By.TAG_NAME, "td")
                if len(cols) > 1:
                    names.append(cols[1].text.strip())
            except:
                continue
        return names
    
    def get_total_price(self):
        try:
            time.sleep(2)  # wait for price to update
            self.wait.until(EC.visibility_of_element_located(self.TOTAL_PRICE))
            return self.get_element_text(self.TOTAL_PRICE)
        except:
            return ""
    
    def delete_first_item(self):
        items = self.get_cart_items()
        if items:
            try:
                delete_btn = items[0].find_element(*self.DELETE_BTN)
                self.driver.execute_script("arguments[0].click()", delete_btn)
                time.sleep(2)  # wait for deletion to process
            except:
                pass

    def place_order(self, name, country, city, card, month, year):
        self.click(self.PLACE_ORDER_BTN)
        self.wait.until(EC.visibility_of_element_located(self.ORDER_NAME))
        self.type(self.ORDER_NAME, name)
        self.type(self.ORDER_COUNTRY, country)
        self.type(self.ORDER_CITY, city)
        self.type(self.ORDER_CARD, card)
        self.type(self.ORDER_MONTH, month)
        self.type(self.ORDER_YEAR, year)
        self.click(self.PURCHASE_BTN)

    def is_order_confirmed(self):
        try:
            confirm = self.find(self.CONFIRM_MESSAGE)
            return confirm.is_displayed()
        except:
            return False
    
    def confirm_order(self):
        self.click(self.CINFIRM_OK_BTN)




    