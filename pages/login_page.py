from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    # Locators
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")


    def fill_login_form(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)

    def submit(self):
        self.click(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        self.fill_login_form(username, password)
        self.submit()