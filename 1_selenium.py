from selenium import webdriver
import time
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
# time.sleep(10)
button_accept = driver.find_element('id', 'L2AGLb')

# print(button_accept)
# print(button_accept.text)
# print(button_accept.is_displayed())
button_accept.click()
time.sleep(2)
search_field = driver.find_element('name', 'q')
search_field.send_keys('Czy AI przejmie świat?')
time.sleep(2)
# search_button = driver.find_element('name', 'btnK')
# search_button.click()
# time.sleep(2)
search_field.send_keys(Keys.ENTER)
time.sleep(2)
driver.quit()