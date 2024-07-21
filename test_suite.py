import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils import user_signup, user_login, browse_products, add_product_to_cart, checkout, user_logout

class EcommerceTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        chrome_driver_path = 'C://Users//admin//Documents//chromedriver//chromedriver.exe'
        service = Service(executable_path=chrome_driver_path)
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_user_signup(self):
        user_signup(self.driver, 'valid_username', 'valid_password')

    def test_user_login_positive(self):
        user_login(self.driver, 'valid_username', 'valid_password')

    def test_user_login_negative(self):
        user_login(self.driver, 'invalid_username', 'invalid_password')

    def test_browse_products(self):
        self.assertTrue(browse_products(self.driver))

    def test_add_product_to_cart(self):
        add_product_to_cart(self.driver)

    def test_checkout_positive(self):
        add_product_to_cart(self.driver)
        checkout(self.driver)

    def test_checkout_negative(self):
        checkout(self.driver)

    def test_user_logout(self):
        user_logout(self.driver)

if __name__ == "__main__":
    unittest.main()
