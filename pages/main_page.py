import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):
    """Взаимодействие с элементами на главной странице товаров"""

    BASE_URL = 'https://www.litres.ru/'

    def __init__(self, driver):
        super().__init__(driver)


    # Locators
    catalog_button = "//button[@data-testid='header-catalog-button']"
    all_genres_button = "//div[@class='GenresTreePopup-module__v-7a4a__all-genres']"
    main_word = "//h1[@id='pageTitle']"


    # Getters
    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.catalog_button)))

    def get_all_genres_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.all_genres_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.main_word)))


    # Actions
    def click_catalog_button(self):
        self.get_catalog_button().click()
        print('Click catalog button')

    def click_all_genres_button(self):
        self.get_all_genres_button().click()
        print('Click all genres button')


    # Methods
    def navigate_to_catalog(self):
        """Переход в каталог с жанрами книг"""

        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_catalog_button()
        self.click_all_genres_button()
        self.assert_word(self.get_main_word(), 'Жанры')

