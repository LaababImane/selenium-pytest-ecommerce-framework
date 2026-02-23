from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def verify():
    brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    options = Options()
    options.binary_location = brave_path
    options.add_argument("--start-maximized")

    # Let Selenium Manager handle the driver automatically
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com")
    print(f"Page title: {driver.title}")
    driver.quit()

if __name__ == "__main__":
    verify()