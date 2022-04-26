from pages.images_page import ImagePage
from pages.main_page import MainPage

def test_search_field(browser):      # Поиск в яндексе
    link = "https://yandex.ru/"      # ссылка на тестируемый ресурс
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_search_link()     # выполняем метод страницы — проверяем наличие поля поиска
    page.input_search_field()        # выполняем метод страницы — вводим текст в поле поиска
    page.should_be_suggest()         # выполняем метод страницы — проверяем открылся или нет suggest
    page.go_search()                 # нажимаем Enter
    page.check_links()               # проверяем первые 5 найденных результатов

def test_images(browser):                  # Картинки на яндексе
    link = "https://yandex.ru/"            # ссылка на тестируемый ресурс
    page = MainPage(browser, link)         # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page_image = ImagePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                            # открываем страницу
    page.should_be_images_link()           # выполняем метод страницы — проверяем ссылку "Картинки"
    page.go_image()                        # кликаем на кнопку "Картинки"
    page_image.check_url()                 # сверяем url с https://yandex.ru/images/
    page_image.first_category()            # открываем первую категорию картинок
    page_image.field_name_verefication()   # сверяем в поисковике верный текст категории
    page_image.first_image()               # переходим на первую картинку, проверяем что открылась
    page_image.first_and_second_image()    # переходим на вторую картинку и обратно, сверяем что картинки разные и вернулись к первой

