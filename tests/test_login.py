from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.config_reader import get_config
import allure

config = get_config()
VALID_USER = config["valid_user"]
INVALID_USER = config["invalid_user"]


@allure.suite("Login Tests")
@allure.title("Valid user can log in successfully")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_valid(driver):

    with allure.step("Open home page"):
        home = HomePage(driver)
        home.open()
    with allure.step("Navigate to login modal"):
        home.go_to_login()
    with allure.step("Enter valid credentials and submit"):
        login = LoginPage(driver)
        login.login(VALID_USER["email"], VALID_USER["password"])
    with allure.step("Verify user is logged in"):
        assert home.is_logged_in(), "User should be logged in"
    
@allure.suite("Login Tests")
@allure.title("Invalid user cannot log in")
@allure.severity(allure.severity_level.NORMAL)
def test_login_invalid(driver):

    with allure.step("Open home page and navigate to login modal"):
        home = HomePage(driver)
        home.open()
        home.go_to_login()
    
    with allure.step("Enter invalid credentials and submit"):
        login = LoginPage(driver)
        login.login(INVALID_USER["email"], INVALID_USER["password"])

    with allure.step("Verify alert is shown for invalid login"):
        WebDriverWait(driver, 10).until(EC.alert_is_present(), "Expected alert for invalid login")
        # Demoblaze shows a browser alert for wrong credentials
        alert = driver.switch_to.alert
        assert alert is not None
        alert.accept()

@allure.suite("Login Tests")
@allure.title("Login with empty fields should show alert")
@allure.severity(allure.severity_level.MINOR)
def test_login_empty_fields(driver) :

    with allure.step("Open home page and navigate to login modal"):
        home = HomePage(driver)
        home.open()
        home.go_to_login()
    
    with allure.step("Submit login form with empty fields"):
        login = LoginPage(driver)
        login.login("", "")

    with allure.step("Verify alert is shown for empty fields"):
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