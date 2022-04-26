from selenium.webdriver import Keys
from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):

    def should_be_search_link(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_FIELD_LINK), "поле поиска отсутствует"

    def input_search_field(self):
        input_tensor = self.browser.find_element(*MainPageLocators.SEARCH_FIELD_LINK)
        input_tensor.send_keys("Тензор")

    def should_be_suggest(self):
        assert self.is_element_present(*MainPageLocators.SUGGEST_LINK), "suggest отсутствует"

    def go_search(self):
        search_enter = self.browser.find_element(*MainPageLocators.SEARCH_FIELD_LINK)
        search_enter.send_keys(Keys.ENTER)

    def check_links(self):
        five_element = self.browser.find_elements(*MainPageLocators.FIVE_LINKS)
        flag = True
        for i in range(5):
            if 'tensor.ru' not in five_element[i].get_attribute('href').lower():
                flag = False
        assert flag, f'ссылка на Тензор отсутствует в первых пяти найденных страницах'

    def should_be_images_link(self):
        assert self.is_element_present(*MainPageLocators.IMAGES_LINK), "Ссылка 'Картинки' отсутствует на странице"

    def go_image(self):
        image_button = self.browser.find_element(*MainPageLocators.IMAGES_LINK)
        image_button.click()