from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage


def test_delete_book_from_cart():
    """Тест по удалению книги из корзины:
    переход в каталог с жанрами книг, выбор книги, переход в корзину, удаление выбранной книги из корзины.
    """

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(
        options=options, service=ChromeService(ChromeDriverManager().install())
    )

    print("Start Test: Delete book from Cart")

    mp = MainPage(driver)
    mp.navigate_to_catalog()

    ct = CatalogPage(driver)
    ct.select_history_book()

    cp = CartPage(driver)
    cp.delete_book()

    print("Finish Test: Delete book from Cart")
    driver.quit()
