from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def check_about_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ELEMENTS_IN_BASKET), \
            "Basket is not empty"

    def text_about_empty_basket_is_present(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_ABOUT_EMPTY), \
            "Text about empty basket not found"