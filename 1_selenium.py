from selenium import webdriver
import time

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
driver.quit()