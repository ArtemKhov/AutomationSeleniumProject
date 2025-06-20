import os
from dotenv import load_dotenv

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


load_dotenv()


class LoginPage(Base):
    """Авторизация пользователя на сайте"""

    BASE_URL = 'https://www.litres.ru/'

    def __init__(self, driver):
        super().__init__(driver)


    # Locators
    login_button = "//div[@id='tab-login']"
    login_name = "//input[@id='auth__input--enterEmailOrLogin']"
    continue_button = "//button[@data-testid='auth__button--continue']"
    password = "//input[@data-testid='auth__input--enterPassword']"
    enter_button = "//button[@data-testid='auth__button--enter']"
    popup_close_button = "//div[@class='ModalStep-module__O5EZhW__closeButton']"
    profile_button = "//a[@data-testid='header__profile-button']"


    # Getters
    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.login_button)))

    def get_login_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.login_name)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.continue_button)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.password)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.enter_button)))

    def get_popup_close_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.popup_close_button)))

    def get_profile_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.profile_button)))


    # Actions
    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')

    def input_login_name(self, login_name):
        self.get_login_name().send_keys(login_name)
        print('Input login name')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('Click continue button')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input password')

    def click_enter_button(self):
        self.get_enter_button().click()
        print('Click enter button')

    def click_popup_close_button(self):
        self.get_popup_close_button().click()
        print('Click popup close button')

    def click_profile_button(self):
        self.get_profile_button().click()
        print('Click profile button')


    # Methods
    def authorization(self):
        """Успешная авторизация в системе"""

        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_login_button()
        self.input_login_name(os.getenv('LOGIN'))
        self.click_continue_button()
        self.input_password(os.getenv('PASSWORD'))
        self.click_enter_button()

        try:
            self.click_popup_close_button()
        except Exception as e:
            print(f'Попап не появился: {e}')

        self.click_profile_button()
        self.assert_url('https://www.litres.ru/me/profile/')

