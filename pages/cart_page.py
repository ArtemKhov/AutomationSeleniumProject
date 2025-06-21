from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.catalog_page import CatalogPage


class CartPage(Base):
    """Взаимодействие с элементами на странице корзины"""

    def __init__(self, driver):
        super().__init__(driver)


    # Locators
    buy_button = "//div[@data-testid='button__content']"
    delete_book_button = "//button[@data-testid='cart__listDeleteButton']"
    delete_word = "//h3[@class='Modal-module__ckz0XG__content__title']"
    confirm_delete_button = "//button[@class='Button-module__QumUZq__button Button-module__QumUZq__button_medium Button-module__QumUZq__button_primary Modal-module__ckz0XG__button']"
    empty_cart_word = "//h2[@class='EmptyState-module__Rus85q__empty__title']"


    # Getters
    def get_buy_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.buy_button)))

    def get_delete_book_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.delete_book_button)))

    def get_delete_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.delete_word)))

    def get_confirm_delete_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.confirm_delete_button)))

    def get_empty_cart_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.empty_cart_word)))


    # Actions
    def click_buy_button(self):
        self.get_buy_button().click()
        print('Click buy button')

    def click_delete_book_button(self):
        self.get_delete_book_button().click()
        print('Click delete button')

    def click_confirm_delete_button(self):
        self.get_confirm_delete_button().click()
        print('Click confirm delete button')


    # Methods
    def proceed_to_buy(self):
        """Подтверждение выбранных книг в корзине для покупки"""

        self.get_current_url()
        self.assert_url('https://www.litres.ru/my-books/cart/')
        self.click_buy_button()
        self.get_screenshot()

    def delete_book(self):
        """Удаление книги из корзины"""

        self.get_current_url()
        self.assert_url('https://www.litres.ru/my-books/cart/')
        self.click_delete_book_button()
        self.assert_word(self.get_delete_word(), 'Удаление книги')
        self.click_confirm_delete_button()
        self.assert_word(self.get_empty_cart_word(), 'Корзина пуста')
        self.get_screenshot()



