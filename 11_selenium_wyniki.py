from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")  # Pełny ekran
# options.add_argument("--headless")         # Tryb bez GUI
# options.add_argument("--disable-notifications")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--window-size=1920,1080")
# options.add_argument("--lang=pl-PL")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")

def google_search(query, output_file='files\\strona.txt'):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get('https://www.google.com/')
    driver.find_element(By.ID, 'L2AGLb').click()

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search")))
#
    results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
    print(results)

    data = []
    for result in results:
        try:
            title = result.find_element(By.XPATH, ".//h3").text
            link = result.get_attribute('href')
            data.append({'title': title, 'link':link})
        except Exception as e:
            print(e)
            continue

    print(data)
    with open(output_file, mode='a') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'link'])
        writer.writeheader()
        writer.writerows(data)

    driver.close()
    driver.quit()

if __name__ == '__main__':
    query = input('Czego szukamy? ')
    google_search(query)