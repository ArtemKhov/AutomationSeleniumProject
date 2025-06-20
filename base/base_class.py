import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:

    def __init__(self, driver):
        self.driver = driver


    """Method: Get current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current URL: {get_url}')

    """Method: assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result, 'Значения не совпадают'
        print('Correct value word')


    """Method: assert URL"""
    def assert_url(self, result):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(result))
        get_url = self.driver.current_url
        assert get_url == result, 'URL не совпадают'
        print('Correct URL')


    """Method: Screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        screenshot_name = f'screenshot {now_date}.png'
        self.driver.save_screenshot(r"E:\autoTests\AutomationSeleniumProject\screen\\" + screenshot_name)
        print('Screenshot - Done')