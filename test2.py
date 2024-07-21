from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.get('https://www.demoblaze.com/')


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login2"]'))).click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'loginusername'))).send_keys('123')
driver.find_element(By.ID, 'loginpassword').send_keys('123')
driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
time.sleep(2)

#WebDiverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Next")]'))).click()

time.sleep(2)
