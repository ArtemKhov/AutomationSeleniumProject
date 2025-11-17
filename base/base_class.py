import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Получение текущего URL"""

        get_url = self.driver.current_url
        print(f"Current URL: {get_url}")

    def assert_word(self, word, result: str):
        """Проверка совпадения значения слова"""

        value_word = word.text
        assert value_word == result, "Значения не совпадают"
        print("Correct value word")

    def assert_url(self, result: str):
        """Проверка совпадения URL"""

        WebDriverWait(self.driver, 10).until(EC.url_to_be(result))
        get_url = self.driver.current_url
        assert get_url == result, "URL не совпадают"
        print("Correct URL")

    def assert_any_word_in_results(self, locator, expected_word):
        """Проверяет, что хотя бы один элемент содержит ожидаемый текст"""

        elements = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located(("xpath", locator))
        )

        found = False
        for element in elements:
            if element.text == expected_word:
                found = True
                break

        assert found, f'Не найдено ни одного элемента с текстом "{expected_word}"'
        print(f'Correct: найден элемент с текстом "{expected_word}"')

    def get_screenshot(self):
        """Метод делает скриншот и сохраняет его по указанному пути"""

        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        screenshot_name = f"screenshot {now_date}.png"
        self.driver.save_screenshot(
            r"E:\autoTests\AutomationSeleniumProject\screen\\" + screenshot_name
        )
        print("Screenshot - Done")
