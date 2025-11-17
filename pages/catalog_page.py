import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.components.filters import FiltersComponent


class CatalogPage(Base):
    """Взаимодействие с элементами на странице каталога"""

    def __init__(self, driver):
        super().__init__(driver)
        self.filters = FiltersComponent(driver)

    # Locators
    genre_light_reading = (
        "(//a[@class='_2ce937fc'])[1]"
    )
    genre_history = (
        "(//a[@class='_2ce937fc'])[3]"
    )
    genre_business_book = (
        "(//a[@class='_2ce937fc'])[4]"
    )
    genre_word_light_reading = "//a[@class='_2ce937fc' and contains(text(), 'Легкое чтение')]"
    genre_word_history = "//a[@class='_2ce937fc' and contains(text(), 'История')]"
    genre_word_business = "//a[@class='_2ce937fc' and contains(text(), 'Бизнес-книги')]"
    bestsellers_history_book = "(//h2[@class='d113beca e3b5eee6'])[1]"
    top_20_business_book = "(//h2[@class='d113beca e3b5eee6'])[1]"
    first_book = "(//a[@class='d14d2f6b'])[1]"
    adult_confirm_button = "//div[contains(text(), 'Да, мне есть 18')]"
    cart_added_button = "//button[@data-testid='book__addToCartButton']"
    cart_menu_button = "//div[@id='tab-basket']"
    popup_info_close_button = "//div[@data-testid='modal__close--button']"

    # Getters
    def get_genre_light_reading(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.genre_light_reading))
        )

    def get_genre_history(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.genre_history))
        )

    def get_genre_business_book(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.genre_business_book))
        )

    def get_genre_word_light_reading(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.genre_word_light_reading))
        )

    def get_genre_word_history(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.genre_word_history))
        )

    def get_genre_word_business(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.genre_word_business))
        )

    def get_bestsellers_history_book(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(("xpath", self.bestsellers_history_book))
        )

    def get_top_20_business_book(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(("xpath", self.top_20_business_book))
        )

    def get_first_book(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.first_book))
        )

    def get_adult_confirm_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.adult_confirm_button))
        )

    def get_cart_added_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.cart_added_button))
        )

    def get_cart_menu_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.cart_menu_button))
        )

    def get_popup_info_close_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(("xpath", self.popup_info_close_button))
        )

    # Actions
    def click_genre_light_reading(self):
        self.get_genre_light_reading().click()
        print("Click genre light reading")

    def click_genre_history(self):
        self.get_genre_history().click()
        print("Click genre history")

    def click_genre_business_book(self):
        self.get_genre_business_book().click()
        print("Click genre business book")

    def click_bestsellers_history_book(self):
        self.get_bestsellers_history_book().click()
        print("Click bestsellers history book")

    def click_top_20_business_book(self):
        self.get_top_20_business_book().click()
        print("Click top 20 business book")

    def click_first_book(self):
        """Открытие страницы с книгой по ссылке"""

        element = self.get_first_book()
        url = element.get_attribute("href")
        if url:
            self.driver.execute_script(f"window.open('{url}', '_blank');")
            print("Opened book URL in a new tab")
        else:
            raise Exception("Element is not a link or has no href")

    def click_adult_confirm_button(self):
        self.get_adult_confirm_button().click()
        print("Click adult confirm button")

    def click_cart_added_button(self):
        self.get_cart_added_button().click()
        print("Add book to cart")

    def click_cart_menu_button(self):
        self.get_cart_menu_button().click()
        print("Click cart menu button")

    def click_popup_info_close_button(self):
        self.get_popup_info_close_button().click()
        print("Close popup info")

    # Methods
    def select_light_reading_book(self):
        """Выбор книги из жанра: 'Легкое чтение' и добавление её в корзину"""

        self.get_current_url()
        self.click_genre_light_reading()
        self.assert_word(self.get_genre_word_light_reading(), "Легкое чтение")

        # выбор фильтров
        try:
            self.filters.click_filter_only_for_subscription()
            self.filters.click_filter_only_for_abonement()
            self.filters.click_filter_textbook()
            self.filters.click_filter_language_ru()
            self.filters.click_filter_high_score_only()
        except TimeoutError:
            print("Фильтры недоступны")

        # доп. время ожидания в 2 секунду после применения фильтров
        time.sleep(2)
        self.click_first_book()

        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        else:
            raise Exception("Нет второй вкладки для переключения!")

        try:
            self.click_cart_added_button()
        except ElementClickInterceptedException:
            print(f"Попалась книга с контентом 18+")
            self.click_adult_confirm_button()
            self.click_cart_added_button()

        try:
            self.click_popup_info_close_button()
        except Exception as e:
            print(f"Попап не появился: {e}")

        self.click_cart_menu_button()
        self.assert_url("https://www.litres.ru/my-books/cart/")

    def select_history_book(self):
        """Выбор книги из жанра: 'История - бестселлеры и новинки' и добавление её в корзину"""

        self.get_current_url()
        self.click_genre_history()
        self.assert_word(self.get_genre_word_history(), "История")
        self.click_bestsellers_history_book()
        self.get_current_url()

        # выбор фильтров
        try:
            self.filters.click_filter_only_for_subscription()
            self.filters.click_filter_audiobook()
        except TimeoutError:
            print("Фильтры недоступны")

        # доп. время ожидания в 2 секунду после применения фильтров
        time.sleep(2)
        self.click_first_book()

        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        else:
            raise Exception("Нет второй вкладки для переключения!")

        try:
            self.click_cart_added_button()
        except ElementClickInterceptedException:
            print(f"Попалась книга с контентом 18+")
            self.click_adult_confirm_button()
            self.click_cart_added_button()

        try:
            self.click_popup_info_close_button()
        except Exception as e:
            print(f"Попап не появился: {e}")

        self.click_cart_menu_button()
        self.assert_url("https://www.litres.ru/my-books/cart/")

    def select_business_book(self):
        """Выбор книги из жанра: 'Бизнес-книги - топ-20' и добавление её в корзину"""

        self.get_current_url()
        self.click_genre_business_book()
        self.assert_word(self.get_genre_word_business(), "Бизнес-книги")
        self.click_top_20_business_book()
        self.get_current_url()

        # выбор фильтров
        try:
            self.filters.click_filter_only_for_abonement()
            self.filters.click_filter_high_score_only()
        except TimeoutError:
            print("Фильтры недоступны")

        # доп. время ожидания в 2 секунды после применения фильтров
        time.sleep(2)
        self.click_first_book()

        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        else:
            raise Exception("Нет второй вкладки для переключения!")

        try:
            self.click_cart_added_button()
        except ElementClickInterceptedException:
            print(f"Попалась книга с контентом 18+")
            self.click_adult_confirm_button()
            self.click_cart_added_button()

        try:
            self.click_popup_info_close_button()
        except Exception as e:
            print(f"Попап не появился: {e}")

        self.click_cart_menu_button()
        self.assert_url("https://www.litres.ru/my-books/cart/")
