import time
from pages import product_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.config_reader import get_config

config = get_config()
VALID_USER = config["valid_user"]
PRODUCT_NAME = "Samsung galaxy s6"

def test_add_product_to_cart(driver):

    # Login first
    home = HomePage(driver)
    home.open()
    home.go_to_login()
    login = LoginPage(driver)
    login.login(VALID_USER["email"], VALID_USER["password"])

    # Select product and add to cart
    home.click_product_by_name(PRODUCT_NAME)

    #Add to cart
    product= ProductPage(driver)
    name = product.get_product_name()
    product.add_to_cart()
    
    # Verify product is in cart
    cart = CartPage(driver)
    cart.open()
    time.sleep(2)  # wait for cart to update

    items = cart.get_item_names()
    print(f"\nCart items: {items}")  # helpful for debugging
    assert any(PRODUCT_NAME in item for item in items), f"{PRODUCT_NAME} should be in the cart, but got: {items}"


def test_cart_total_calculation(driver):

    home = HomePage(driver)
    home.open()
    home.go_to_login()
    login = LoginPage(driver)
    login.login(VALID_USER["email"], VALID_USER["password"])

    home.click_product_by_name(PRODUCT_NAME)
    product = ProductPage(driver)
    product.add_to_cart()

    cart = CartPage(driver)
    cart.open()
    time.sleep(2)  # wait for cart to update
    total = cart.get_total_price()
    assert total is not None and total != "", "Total price should be displayed"


def test_delete_item_from_cart(driver):

    home = HomePage(driver)
    home.open()
    home.go_to_login()
    login = LoginPage(driver)
    login.login(VALID_USER["email"], VALID_USER["password"])

    home.click_product_by_name(PRODUCT_NAME)
    product = ProductPage(driver)
    product.add_to_cart()

    cart = CartPage(driver)
    cart.open()
    time.sleep(2)  # wait for cart to update

    items_before = len(cart.get_cart_items())

    cart.delete_first_item()
    time.sleep(2)  # wait for deletion to process

    items_after = len(cart.get_cart_items())
    assert items_after < items_before, "Item should be deleted from the cart"


def test_checkout_process(driver):

    home = HomePage(driver)
    home.open()
    home.go_to_login()
    login = LoginPage(driver)
    login.login(VALID_USER["email"], VALID_USER["password"])

    home.click_product_by_name(PRODUCT_NAME)
    product = ProductPage(driver)
    product.add_to_cart()

    cart = CartPage(driver)
    cart.open()
    time.sleep(2)  # wait for cart to update

    cart.place_order(
        name="Test User",
        country="Test Country",
        city="Test City",
        card="1234567890123456",
        month="12",
        year="2025"
    )

    time.sleep(3)  # wait for order confirmation

    assert cart.is_order_confirmed(), "Order confirmation should be displayed"
    cart.confirm_order()


# def test_debug_add_to_cart(driver):
#     from selenium.webdriver.common.by import By
#     import time

#     home = HomePage(driver)
#     home.open()
#     home.go_to_login()
#     login = LoginPage(driver)
#     login.login(VALID_USER["email"], VALID_USER["password"])

#     time.sleep(5)
#     home.click_product_by_name(PRODUCT_NAME)

#     time.sleep(3)  # wait for product page to load

#     # Print all elements with href or button elements
#     buttons = driver.find_elements(By.XPATH, "//a | //button")
#     print(f"\nFound {len(buttons)} clickable elements:")
#     for btn in buttons:
#         text = btn.text.strip()
#         if text:
#             print(f"  - '{text}' | Displayed: {btn.is_displayed()} | Tag: {btn.tag_name}")