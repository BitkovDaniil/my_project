import requests
from pages.base_page import BasePage
from pages.locators import ImagesPageLocators

class ImagePage(BasePage):

    def check_url(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
        page_url = self.browser.current_url
        print(page_url)
        assert "yandex.ru/images" in page_url, "клик по кнопке Картинки не привел на url https://yandex.ru/images/"

    def first_category(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
        category = self.browser.find_element(*ImagesPageLocators.CATEGORY_LINK)
        category.click()

    def field_name_verefication(self):
        category = self.browser.find_element(*ImagesPageLocators.CATEGORY_LINK)
        category_name = category.get_attribute('data-grid-text').lower()
        page_url = str(requests.utils.unquote(self.browser.current_url)).lower()
        flag = True
        for name in category_name:
            if name not in str(page_url).lower():
                flag = False
        assert flag, 'в поисковике не текст категории'

    def first_image(self):
        first_image_link = self.browser.find_elements(*ImagesPageLocators.FIRST_IMAGE_LINK)
        first_image_link[0].click()
        assert self.is_element_present(*ImagesPageLocators.IMAGE), "Картинка из первой категории не открылась"

    def first_and_second_image(self):
        # нашли ссылку на первую картинку и сохранили ее
        first_image = self.browser.find_element(*ImagesPageLocators.IMAGE)
        first_image_url = first_image.get_attribute('src')
        # нажали на кнопку вперед
        circle_button = self.browser.find_element(*ImagesPageLocators.CIRCLE_BUTTON_NEXT)
        circle_button.click()
        # нашли вторую картинку и сохранили ее ссылку
        second_image = self.browser.find_element(*ImagesPageLocators.IMAGE)
        second_image_url = first_image.get_attribute('src')
        # сравниваем ссылки первой и второй картинки, убеждаемся что картинки изменились
        assert first_image_url != second_image_url, "ссылки на первую и вторую картинку одинаковые, открывается одна и таже картинка"
        # нажимаем кнопку назад
        circle_button = self.browser.find_element(*ImagesPageLocators.CIRCLE_BUTTON_PREV)
        circle_button.click()
        # вернулись на первую картинку, нашли ее и сохранили в отдельную переменную
        new_first_image = self.browser.find_element(*ImagesPageLocators.IMAGE)
        new_first_image_url = new_first_image.get_attribute('src')
        # сравниваем ссылки первой и возвращенной первой , убеждаемся что картинки не изменились
        assert first_image_url == new_first_image_url, "Первая картинка и возвращенная первая картинка разные"












