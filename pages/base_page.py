from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    BASE_URL = "https://demoblaze.com"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        try:
            element.click()
        except:
             self.driver.execute_script("arguments[0].click();", element)
    
    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def current_url(self):
        return self.driver.current_url
    
    def get_element_text(self, locator):
        element = self.find(locator)
        return element.text
    