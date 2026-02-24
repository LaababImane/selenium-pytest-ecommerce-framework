import time
import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.config_reader import get_config

config = get_config()
VALID_USER = config["valid_user"]
PRODUCT_NAME = "Samsung galaxy s6"

@allure.feature("Cart Functionality")
@allure.title("Product can be added to cart and displayed correctly")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_product_to_cart(driver):
    with allure.step("Login"):
        # Login first
        home = HomePage(driver)
        home.open()
        home.go_to_login()
        login = LoginPage(driver)
        login.login(VALID_USER["email"], VALID_USER["password"])

    with allure.step(f"Click on product '{PRODUCT_NAME}'"):    
        # Select product and add to cart
        home.click_product_by_name(PRODUCT_NAME)

    with allure.step("Add product to cart"):
        #Add to cart
        product= ProductPage(driver)
        name = product.get_product_name()
        product.add_to_cart()
    
    with allure.step("Verify product appears is in cart"):
        # Verify product is in cart
        cart = CartPage(driver)
        cart.open()
        time.sleep(2)  # wait for cart to update

        items = cart.get_item_names()
        print(f"\nCart items: {items}")  # helpful for debugging
        assert any(PRODUCT_NAME in item for item in items), f"{PRODUCT_NAME} should be in the cart, but got: {items}"


@allure.feature("Cart Functionality")
@allure.title("Cart displays total price correctly")
@allure.severity(allure.severity_level.NORMAL)
def test_cart_total_calculation(driver):

    with allure.step("Login and add product to cart"):
        home = HomePage(driver)
        home.open()
        home.go_to_login()
        login = LoginPage(driver)
        login.login(VALID_USER["email"], VALID_USER["password"])
        home.click_product_by_name(PRODUCT_NAME)
        product = ProductPage(driver)
        product.add_to_cart()

    with allure.step(" Verify total is displayed in cart"):
        cart = CartPage(driver)
        cart.open()
        time.sleep(2)  # wait for cart to update
        total = cart.get_total_price()
        assert total is not None and total != "", "Total price should be displayed"

@allure.feature("Cart Functionality")
@allure.title("Item can be deleted from cart")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_item_from_cart(driver):
    with allure.step("Login and add product to cart"):
        home = HomePage(driver)
        home.open()
        home.go_to_login()
        login = LoginPage(driver)
        login.login(VALID_USER["email"], VALID_USER["password"])

        home.click_product_by_name(PRODUCT_NAME)
        product = ProductPage(driver)
        product.add_to_cart()

    with allure.step("Delete item from cart and verify it's removed"):
        cart = CartPage(driver)
        cart.open()
        time.sleep(2)  # wait for cart to update

        items_before = len(cart.get_cart_items())

        cart.delete_first_item()
    time.sleep(2)  # wait for deletion to process

    with allure.step("Verify item is deleted from cart"):
        items_after = len(cart.get_cart_items())
        assert items_after < items_before, "Item should be deleted from the cart"

@allure.feature("Cart Functionality")
@allure.title("User can complete checkout process")
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout_process(driver):

    with allure.step("Login, add product"):
        home = HomePage(driver)
        home.open()
        home.go_to_login()
        login = LoginPage(driver)
        login.login(VALID_USER["email"], VALID_USER["password"])

        home.click_product_by_name(PRODUCT_NAME)
        product = ProductPage(driver)
        product.add_to_cart()
    with allure.step("Place order"):
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
    with allure.step("Verify order confirmation is displayed"):
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