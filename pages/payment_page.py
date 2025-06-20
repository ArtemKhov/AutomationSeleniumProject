from faker import Faker

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


fake = Faker('en_US')


class PaymentPage(Base):
    """Взаимодействие с элементами на странице оплаты"""

    def __init__(self, driver):
        super().__init__(driver)


    # Locators
    new_card = "//li[@class='PaymentMethodSelector-module__SWI10a__paymentMethod payment-method-card']"
    continue_button = "//button[@data-testid='paymentLayout__payment--button']"
    card_number = "//input[@id='cardNumber']"
    expiry_date = "//input[@id='expiryDate']"
    card_cvc = "//input[@id='cvc']"
    bank_payment_button = "//buton[@class='_14KXZFF2qamrgjaDJQf2-k _2LEfKwbPi7lA1km6XdQKz0']"
    payment_button = "//button[@data-testid='paymentLayout__payment--button']"


    # Getters
    def get_new_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.new_card)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.continue_button)))

    def get_card_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.card_number)))

    def get_expiry_date(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.expiry_date)))

    def get_card_cvc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.card_cvc)))

    def get_bank_payment_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.bank_payment_button)))

    def get_payment_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.payment_button)))


    # Actions
    def click_new_card(self):
        self.get_new_card().click()
        print('Click new card')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('Click continue button')

    def input_card_number(self, card_number):
        self.get_card_number().click()
        self.get_card_number().send_keys(card_number)
        print('Input card number')

    def input_expiry_date(self, expiry_date):
        self.get_expiry_date().click()
        self.get_expiry_date().send_keys(expiry_date)
        print('Input expiry date')

    def input_card_cvc(self, card_cvc):
        self.get_card_cvc().click()
        self.get_card_cvc().send_keys(card_cvc)
        print('Input card cvc')

    def click_bank_payment_button(self):
        self.get_bank_payment_button().click()
        print('Click bank payment button')

    def click_payment_button(self):
        self.get_payment_button().click()
        print('Click payment button')


    # Methods
    def complete_payment(self):
        """Оплата товара"""
        number = fake.credit_card_number()
        date = fake.credit_card_expire()
        cvc = fake.credit_card_security_code()

        self.get_current_url()
        self.click_new_card()
        self.click_continue_button()
        self.input_card_number(number)
        self.input_expiry_date(date)
        self.input_card_cvc(cvc)
        self.click_bank_payment_button()

