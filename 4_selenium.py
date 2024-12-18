from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from time import sleep
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def make_screenshot(driver):
    teraz = datetime.datetime.now()
    file_name = teraz.strftime('screens\\screenshot_%Y%m%d_%H%M%S.png')
    driver.get_screenshot_as_file(file_name)

def wait_for_id(element_id):
    timeout = 5
    timeout_message = f'Element {element_id} nie pojawił się w czasie {timeout}s'
    lokalizator = (By.ID, element_id)
    znaleziono = EC.visibility_of_element_located(lokalizator)
    oczekiwator = WebDriverWait(driver, timeout).until(znaleziono, timeout_message)


driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')
print(f'nazwa strony: {driver.title}')
sleep(1)

try:
    username_field = driver.find_element('id', 'user-name')
    password_field = driver.find_element(By.NAME, 'password')

except NoSuchElementException:
    make_screenshot(driver)
    driver.quit()
    print('Nie znaleziono')
    raise

username_field.clear()
username_field.send_keys('standard_user')
password_field.clear()
password_field.send_keys('secret_sauce')

try:
    login_button = wait_for_id('login_buttone')
except TimeoutException:
    print('Nie znaleziono')
    raise
else:
    print('Znaleziono')
finally:
    make_screenshot(driver)
    driver.quit()