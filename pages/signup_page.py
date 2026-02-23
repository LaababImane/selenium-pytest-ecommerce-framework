from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignupPage(BasePage):
    USERNAME_FIELD  = (By.ID, "sign-username")
    PASSWORD_FIELD  = (By.ID, "sign-password")
    SIGNUP_BUTTON   = (By.XPATH, "//button[text()='Sign up']")

    def fill_signup_form(self, username, password):
        self.type(self.USERNAME_FIELD, username)
        self.type(self.PASSWORD_FIELD, password)

    def submit(self):
        self.click(self.SIGNUP_BUTTON)

    def signup(self, username, password):
        self.fill_signup_form(username, password)
        self.submit()