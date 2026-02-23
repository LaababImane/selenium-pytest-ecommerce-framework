import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    
    options = Options()

    if os.environ.get("CI"):
        options.add_argument("--headless")
        options.add_argument("no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    else:
        brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        options.binary_location = brave_path
        options.add_argument("--start-maximized")

        # Anti-detection arguments
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            print(f"Saved screenshot: {screenshot_path}")
