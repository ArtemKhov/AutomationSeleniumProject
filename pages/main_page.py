from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):
    """Взаимодействие с элементами на главной странице товаров"""

    BASE_URL = "https://www.litres.ru/"

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    catalog_button = "//button[@data-testid='header-catalog-button']"
    all_genres_button = "//div[@data-testid='popup__allGenre--button']"
    main_word = "//h1[@id='pageTitle']"
    search_field = "//input[@data-testid='search__input']"
    search_button = "//button[@data-testid='search__button']"
    search_result_word = "//h1[@id='pageTitle']"
    all_books_titles_locator = "//a[@data-testid='art__title']"

    # Getters
    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.catalog_button))
        )

    def get_all_genres_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.all_genres_button))
        )

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.main_word))
        )

    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.search_field))
        )

    def get_search_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.search_button))
        )

    def get_search_result_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.search_result_word))
        )

    def get_all_books_titles_locator(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.all_books_titles_locator))
        )

    # Actions
    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click catalog button")

    def click_all_genres_button(self):
        self.get_all_genres_button().click()
        print("Click all genres button")

    def input_search_field(self, search_book):
        self.get_search_field().send_keys(search_book)
        print("Input search field")

    def click_search_button(self):
        self.get_search_button().click()
        print("Click search button")

    # Methods
    def navigate_to_catalog(self):
        """Переход в каталог с жанрами книг"""

        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_catalog_button()
        self.click_all_genres_button()
        self.assert_word(self.get_main_word(), "Жанры")

    def search_book(self, book_name):
        """Поиск популярной книги"""

        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_search_field(book_name)
        self.click_search_button()
        self.assert_word(self.get_search_result_word(), "Результаты поиска «Ведьмак»")
        self.assert_any_word_in_results(self.all_books_titles_locator, "Ведьмак")
        self.get_screenshot()
