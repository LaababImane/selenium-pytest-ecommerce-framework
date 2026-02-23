from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.config_reader import get_config

config = get_config()
VALID_USER = config["valid_user"]
INVALID_USER = config["invalid_user"]



def test_login_valid(driver):
    home = HomePage(driver)
    home.open()
    home.go_to_login()

    login = LoginPage(driver)
    login.login(VALID_USER["email"], VALID_USER["password"])

    assert home.is_logged_in(), "User should be logged in"
    

def test_login_invalid(driver):
    home = HomePage(driver)
    home.open()
    home.go_to_login()

    login = LoginPage(driver)
    login.login(INVALID_USER["email"], INVALID_USER["password"])

    WebDriverWait(driver, 10).until(EC.alert_is_present(), "Expected alert for invalid login")
    # Demoblaze shows a browser alert for wrong credentials
    alert = driver.switch_to.alert
    assert alert is not None
    alert.accept()


def test_login_empty_fields(driver) :
    home = HomePage(driver)
    home.open()
    home.go_to_login()

    login = LoginPage(driver)
    login.login("", "")

    WebDriverWait(driver, 10).until(EC.alert_is_present(), "Expected alert for empty fields")
    alert = driver.switch_to.alert
    assert alert is not None
    alert.accept()

# def test_debug_modal(driver):
#     home = HomePage(driver)
#     home.open()
#     home.go_to_login()

#     import time
#     time.sleep(3)  # wait for modal to open

#     # Print all visible element IDs on the page
#     elements = driver.find_elements("xpath", "//*[@id]")
#     for el in elements:
#         print(f"ID: {el.get_attribute('id')} | Visible: {el.is_displayed()}")