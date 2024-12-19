
from POM import LoginPage

from selenium import webdriver

def test_login_page():
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.print_page_info()
