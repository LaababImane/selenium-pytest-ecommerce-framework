from pages.home_page import HomePage
from selenium.webdriver.common.by import By


def test_home_page_loads(driver):
    home_page = HomePage(driver)
    home_page.open()
    
    assert "STORE" in driver.title, "Home page should have 'STORE' in the title"

def test_category_phones(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.select_category("Phones")

    assert "demoblaze" in driver.current_url

def test_navigate_to_cart(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.go_to_cart()

    assert "cart" in driver.current_url, "Should navigate to cart page"