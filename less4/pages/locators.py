from selenium.webdriver.common.by import By

class BasePageLocators():
    BTN_GO_TO_BASKET = (By.CSS_SELECTOR, ".btn-group > .btn-default")

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    ELEMENTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    TEXT_ABOUT_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():
    BTN_TO_REGISTRATE = (By.CSS_SELECTOR, "#register_form > button")

    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_ADD_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")

    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE_IN_MAIN = (By.CSS_SELECTOR, ".product_main .price_color")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")