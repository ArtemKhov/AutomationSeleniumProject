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
    def assert_word(self, word, result: str):
        value_word = word.text
        assert value_word == result, 'Значения не совпадают'
        print('Correct value word')

    """Method: assert URL"""
    def assert_url(self, result: str):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(result))
        get_url = self.driver.current_url
        assert get_url == result, 'URL не совпадают'
        print('Correct URL')

    """Method: assert Any word in results"""
    def assert_any_word_in_results(self, locator, expected_word):
        """Проверяет, что хотя бы один элемент содержит ожидаемый текст"""
        elements = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located(('xpath', locator))
        )

        found = False
        for element in elements:
            if element.text == expected_word:
                found = True
                break

        assert found, f'Не найдено ни одного элемента с текстом "{expected_word}"'
        print(f'Correct: найден элемент с текстом "{expected_word}"')

    """Method: Screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        screenshot_name = f'screenshot {now_date}.png'
        self.driver.save_screenshot(r"E:\autoTests\AutomationSeleniumProject\screen\\" + screenshot_name)
        print('Screenshot - Done')