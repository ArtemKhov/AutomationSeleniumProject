from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class FiltersComponent(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    filter_only_for_subscription = "//div[@aria-labelledby='labelFor-only_litres_subscription_arts']"
    filter_only_for_abonement = "//div[@aria-labelledby='labelFor-only_abonement_arts']"
    filter_high_score_only = "//div[@aria-labelledby='labelFor-only_high_rated']"
    filter_textbook = "//input[@id='art_types-text_book']"
    filter_audiobook = "//input[@id='art_types-audiobook']"
    filter_podcast = "//input[@id='art_types-podcast']"
    filter_webtoon = "//input[@id='art_types-webtoon']"
    filter_language_ru = "//input[@id='languages-ru']"
    filter_language_en = "//input[@id='languages-en']"


    # Getters
    def get_filter_only_for_subscription(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.filter_only_for_subscription)))

    def get_filter_only_for_abonement(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.filter_only_for_abonement)))

    def get_filter_high_score_only(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.filter_high_score_only)))

    def get_filter_textbook(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.filter_textbook)))

    def get_filter_audiobook(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.filter_audiobook)))

    def get_filter_podcast(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.filter_podcast)))

    def get_filter_webtoon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.filter_webtoon)))

    def get_filter_language_ru(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.filter_language_ru)))

    def get_filter_language_en(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', self.filter_language_en)))


    # Actions
    def click_filter_only_for_subscription(self):
        self.get_filter_only_for_subscription().click()
        print('Click filter only for subscription')

    def click_filter_only_for_abonement(self):
        self.get_filter_only_for_abonement().click()
        print('Click filter only for abonement')

    def click_filter_high_score_only(self):
        self.get_filter_high_score_only().click()
        print('Click filter high score only')

    def click_filter_textbook(self):
        element = self.get_filter_textbook()
        self.driver.execute_script("arguments[0].click();", element)
        print('Click filter textbook checkbox')

    def click_filter_audiobook(self):
        element = self.get_filter_audiobook()
        self.driver.execute_script("arguments[0].click();", element)
        print('Click filter audiobook checkbox')

    def click_filter_podcast(self):
        element = self.get_filter_podcast()
        self.driver.execute_script("arguments[0].click();", element)
        print('Click filter podcast checkbox')

    def click_filter_webtoon(self):
        element = self.get_filter_webtoon()
        self.driver.execute_script("arguments[0].click();", element)
        print('Click filter webtoon checkbox')

    def click_filter_language_ru(self):
        element = self.get_filter_language_ru()
        self.driver.execute_script("arguments[0].click();", element)
        print('Click filter language "Russian" checkbox')

    def click_filter_language_en(self):
        element = self.get_filter_language_en()
        self.driver.execute_script("arguments[0].click();", element)
        print('Click filter language "English" checkbox')
