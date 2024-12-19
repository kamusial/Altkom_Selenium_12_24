from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/")
time.sleep(2)

menu = driver.find_element('id', 'navbtn_tutorials')
# menu.click()
# time.sleep(2)
# # HTMLtutorial = driver.find_element(By.XPATH,'//*[@id="tutorials_html_css_links_list"]/div[1]/a[2]')
HTMLtutorial = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/nav[1]/div[1]/div/div[2]/div[1]/div[1]/a[2]')
# HTMLtutorial.click()
time.sleep(2)
(webdriver.ActionChains(driver).move_to_element(menu).
 click().move_to_element(HTMLtutorial).click().perform())
driver.find_element(By.ID, 'accept-choices').click()
HTML_forms_attributes = driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[41]')
HTML_forms_attributes.click()
tryityourself = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/a')
tryityourself.click()
time.sleep(2)

# nowa karta
currentWindowName = driver.current_window_handle     # aktualna karta
windowNames = driver.window_handles
print(currentWindowName)
print(windowNames)

for window in windowNames:
    if window != currentWindowName:
        driver.switch_to.window(window)

driver.switch_to.frame(driver.find_element(By.ID,'iframeResult'))
firstName = driver.find_element(By.ID, 'fname')
time.sleep(2)
if firstName.is_enabled():
    firstName.clear()
    firstName.send_keys('Kamil')
else:
    print('Nie da się wpisać')
time.sleep(5)

driver.close()
driver.quit()