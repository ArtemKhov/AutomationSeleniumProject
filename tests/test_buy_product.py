import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage


# @pytest.mark.run(order=3)
def test_buy_book_from_light_reading_genre():
    """Тест по покупке книги включает:
    авторизацию, переход в каталог с жанрами книг, выбор книги по установленным фильтрам, переход в корзину, переход к покупке книги."""

    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument("--guest")
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print('Start Test: Buy book from light reading genre')

    # login = LoginPage(driver)
    # login.authorization()

    mp = MainPage(driver)
    mp.navigate_to_catalog()

    ct = CatalogPage(driver)
    ct.select_light_reading_book()

    cp = CartPage(driver)
    cp.proceed_to_buy()

    # p = PaymentPage(driver)
    # p.complete_payment()


    print('Finish Test: Buy book from light reading genre')
    driver.quit()