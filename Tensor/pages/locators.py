from selenium.webdriver.common.by import By

class MainPageLocators():
    SEARCH_FIELD_LINK = (By.CSS_SELECTOR, ".input__control.input__input.mini-suggest__input")
    SUGGEST_LINK = (By.CSS_SELECTOR, ".mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile")
    FIVE_LINKS = (By.CSS_SELECTOR, '.Link.Link_theme_normal.OrganicTitle-Link.organic__url.link')
    IMAGES_LINK = (By.CSS_SELECTOR, ".services-new__icon.services-new__icon_images")

class ImagesPageLocators():
    CATEGORY_LINK = (By.CSS_SELECTOR, '.PopularRequestList-Item.PopularRequestList-Item_pos_0')
    FIRST_IMAGE_LINK = (By.CSS_SELECTOR, '.serp-item__preview>.serp-item__link>.serp-item__thumb.justifier__thumb')
    CIRCLE_BUTTON_NEXT = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_next')
    CIRCLE_BUTTON_PREV = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_prev')
    IMAGE = (By.CSS_SELECTOR, '.MMImage-Origin')
