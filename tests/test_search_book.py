from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import MainPage


def test_search_book():
    """Тест, что по искомому слову находит хотя бы одну книгу"""

    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument("--guest")
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print('Start Test: Search popular book')

    mp = MainPage(driver)
    mp.search_book('Ведьмак')

    print('Finish Test: Search popular book')
    driver.quit()