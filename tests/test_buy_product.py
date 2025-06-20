import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.main_page import MainPage


# @pytest.mark.run(order=3)
def test_buy_product_1():
    """Тест по покупке книги включает:
    авторизацию, переход в каталог с жанрами книг, выбор фильтров, выбор книги, переход в корзину, переход к покупке книги."""

    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument("--guest")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print('Start Test 1')

    # login = LoginPage(driver)
    # login.authorization()

    mp = MainPage(driver)
    mp.navigate_to_catalog()

    print('Finish Test 1')
    driver.quit()