from POM import LoginPage
from selenium import webdriver
from time import sleep
from a2_selenium import make_screenshot
import pytest

test_data = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')
]

@pytest.mark.parametrize('username, password'),
        [('standard_user','https://www.saucedemo.com/inventory.html'),
         'locked_out_user',
         'problem_user', 'performance_glitch_user'])
def test_login_page(username):
    driver = webdriver.Firefox()
    page = LoginPage(driver)
    page.open()
    page.print_page_info()
    page.enter_username(username)
    page.enter_password('secret_sauce')
    page.click_login()
    sleep(3)
    page.print_page_info()
    try:
        assert page.get_current_url() == page.after_login_url
    except AssertionError:
        print('Asercja nie przeszla')
        raise
    else:
        print('Asercja przeszła')
    finally:
        print('Koniec')
        make_screenshot(driver)
        page.close()