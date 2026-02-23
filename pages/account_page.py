from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountPage(BasePage):

    # Locators
    PAGE_HEADING = (By.CSS_SELECTOR, "h2")

    def is_loaded(self):
        return self.get_element_text(self.PAGE_HEADING) == "My Account"
    
    def get_heading(self):
        return self.get_element_text(self.PAGE_HEADING)
