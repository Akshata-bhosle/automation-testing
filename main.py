from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
from utils import user_signup, user_login, browse_products, add_product_to_cart, checkout, user_logout

def get_chrome_driver():
    options = Options()
    # Uncomment the line below to run in headless mode
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Path to ChromeDriver
    chrome_driver_path = 'C://Users//admin//Documents//chromedriver//chromedriver.exe'
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome( options=options)
    return driver

def run_tests():
    driver = get_chrome_driver()
    try:
        # User SignUp Positive Scenario
        user_signup(driver, 'valid_username', 'valid_password')

        # User Login Positive Scenario
        user_login(driver, 'valid_username', 'valid_password')
        print('Products displayed:', browse_products(driver))

        # Adding products to the shopping cart
        add_product_to_cart(driver)

        # Checkout Positive Scenario
        checkout(driver)

        # User Logout Positive Scenario
        user_logout(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    run_tests()
