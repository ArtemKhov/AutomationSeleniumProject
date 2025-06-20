import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.components.filters import FiltersComponent


class CatalogPage(Base):
    """Взаимодействие с элементами на странице жанров книг"""

    def __init__(self, driver):
        super().__init__(driver)
        self.filters = FiltersComponent(driver)


    # Locators
    genre_light_reading = "(//a[@class='GenresPage-module__y6ZFYq__genresPage__genreItem__title'])[1]"
    genre_word = "//span[@class='PageHeader-module__k0W69G__title__text']"
    first_book = "(//div[@class='Art-module__3wrtfG__content Art-module__3wrtfG__content_full'])[1]"
    adult_confirm_button = "//div[contains(text(), 'Да, мне есть 18')]"
    cart_added_button = "//button[@data-testid='book__addToCartButton']"
    cart_menu_button = "//div[@id='tab-basket']"
    popup_info_close_button = "//div[@data-testid='modal__close--button']"


    # Getters
    def get_genre_light_reading(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.genre_light_reading)))

    def get_genre_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.genre_word)))

    def get_first_book(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(('xpath', self.first_book)))

    def get_adult_confirm_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.adult_confirm_button)))

    def get_cart_added_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.cart_added_button)))

    def get_cart_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.cart_menu_button)))

    def get_popup_info_close_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.popup_info_close_button)))


    # Actions
    def click_genre_light_reading(self):
        self.get_genre_light_reading().click()
        print('Click genre light reading')

    def click_first_book(self):
        self.get_first_book().click()
        print('Click first book')

    def click_adult_confirm_button(self):
        self.get_adult_confirm_button().click()
        print('Click adult confirm button')

    def click_cart_added_button(self):
        self.get_cart_added_button().click()
        print('Add book to cart')

    def click_cart_menu_button(self):
        self.get_cart_menu_button().click()
        print('Click cart menu button')

    def click_popup_info_close_button(self):
        self.get_popup_info_close_button().click()
        print('Close popup info')


    # Methods
    def select_light_reading_book(self):
        """Выбор книги из жанра: 'Легкое чтение' и добавление её в корзину"""

        self.get_current_url()
        self.click_genre_light_reading()
        self.assert_word(self.get_genre_word(), 'легкое чтение')
        self.filters.click_filter_only_for_subscription()
        self.filters.click_filter_only_for_abonement()
        self.filters.click_filter_textbook()
        self.filters.click_filter_language_ru()
        self.filters.click_filter_high_score_only()
        self.filters.click_filter_new_books()

        # доп. время ожидания в 1 секунду после применения фильтров
        time.sleep(1)
        self.click_first_book()

        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        else:
            raise Exception("Нет второй вкладки для переключения!")

        try:
            self.click_cart_added_button()
        except ElementClickInterceptedException:
            print(f'Попалась книга с контентом 18+')
            self.click_adult_confirm_button()
            self.click_cart_added_button()

        try:
            self.click_popup_info_close_button()
        except Exception as e:
            print(f'Попап не появился: {e}')

        self.click_cart_menu_button()
        self.assert_url('https://www.litres.ru/my-books/cart/')




