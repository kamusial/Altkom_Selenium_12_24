from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
import datetime

def make_screenshot(driver):
    teraz = datetime.datetime.now()
    file_name = teraz.strftime('screenshot_%Y%m%d_%H%M%S.png')
    driver.get_screenshot_as_file(file_name)

driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')
sleep(10)
try:
    username_field = driver.find_element('id', 'user-name')
    password_field = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/input')

except NoSuchElementException:
    make_screenshot(driver)
    driver.quit()
    print('Nie znaleziono')
    raise

username_field.clear()
username_field.send_keys('standard_user')
password_field.clear()
password_field.send_keys('secret_sauce')
login_button.click()
sleep(3)

make_screenshot(driver)
driver.quit()