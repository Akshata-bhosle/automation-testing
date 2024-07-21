from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def user_signup(driver, username, password):
    driver.get('https://www.demoblaze.com/')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'signin2'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'sign-username'))).send_keys(username)
    driver.find_element(By.ID, 'sign-password').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()
    time.sleep(2)
def user_login(driver, username, password):
    driver.get('https://www.demoblaze.com/')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login2'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'loginusername'))).send_keys(username)
    driver.find_element(By.ID, 'loginpassword').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
    time.sleep(2)
def browse_products(driver):
    driver.get('https://www.demoblaze.com/')
    products = driver.find_elements(By.CLASS_NAME, 'card')
    return len(products) > 0
def add_product_to_cart(driver):
    driver.get('https://www.demoblaze.com/')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Next")]'))).click()
    last_product = driver.find_elements(By.CLASS_NAME, 'card')[-1]
    last_product.find_element(By.CLASS_NAME, 'btn-success').click()
    time.sleep(2)
def checkout(driver):
    driver.get('https://www.demoblaze.com/cart.html')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Place Order")]'))).click()
    time.sleep(2)
def user_logout(driver):
    driver.get('https://www.demoblaze.com/')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'logout2'))).click()
    time.sleep(2)
