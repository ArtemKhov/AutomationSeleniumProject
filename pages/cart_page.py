from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CartPage(Base):
    """Взаимодействие с элементами на странице корзины"""

    def __init__(self, driver):
        super().__init__(driver)


    # Locators
    buy_button = "//div[@data-testid='button__content']"


    # Getters
    def get_buy_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.buy_button)))


    # Actions
    def click_buy_button(self):
        self.get_buy_button().click()
        print('Click buy button')


    # Methods
    def proceed_to_buy(self):
        """Подтверждение выбранных книг в корзине для покупки"""

        self.get_current_url()
        self.click_buy_button()

