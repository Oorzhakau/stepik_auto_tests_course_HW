from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_on_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()

    def valid_product_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_basket = self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME_ADD_IN_BASKET)[0]
        assert product_name.text == product_name_in_basket.text, \
            f"Error. Name Product in basket - {product_name_in_basket.text}. Name Product in Describe - {product_name.text}"

    def valid_price_in_basket(self):
        product_price_in_main = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MAIN)
        product_price_in_basket = self.browser.find_elements(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)[-1]
        assert product_price_in_main.text == product_price_in_basket.text, \
            f"Error. Price in basket - {product_price_in_basket.text}. Price in main - {product_price_in_main.text}"

    def should_be_promo_url(self):
        url = self.browser.current_url
        url_find_promo = False
        for i in range(10):
            if url.find("?promo=offer"+str(i)) != -1:
                url_find_promo = True
        assert url_find_promo, "Url doesn't have part about \"promo\""

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeare_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be disappeare"