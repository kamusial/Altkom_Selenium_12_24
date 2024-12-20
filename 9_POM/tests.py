from POM import LoginPage
from selenium import webdriver
from time import sleep
from a2_selenium import make_screenshot
import pytest
import sys

test_data = [
    ('standard_user', 'secret_saucea', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')
]

@pytest.mark.skipif(len('piesek') == 5, reason='not implemented')
@pytest.mark.parametrize('username, password, url', test_data)
def test_login_page(username, password, url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-gpu')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    page = LoginPage(driver)
    page.open()
    page.print_page_info()
    page.enter_username(username)
    page.enter_password(password)
    page.click_login()
    sleep(3)
    page.print_page_info()
    try:
        assert page.get_current_url() == url, make_screenshot(driver)
    except AssertionError:
        print('Asercja nie przeszla')
        raise
    else:
        print('Asercja przeszła')
    finally:
        print('Koniec')
        page.close()

if sys.platform.startswith("win"):
    @pytest.mark.skip("skipping linux-only tests")
    def test_default():
        assert 3 == 4

@pytest.mark.xfail(reason='not implemented')
def test_default2():
    assert 4 == 5
