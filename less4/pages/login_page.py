from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        field_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        field_email.send_keys(email)

        password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password1.send_keys(password)

        password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2.send_keys(password)

        btn = self.browser.find_element(*LoginPageLocators.BTN_TO_REGISTRATE)
        btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        if url.find("login") == -1:
            url_find_login = False
        else:
            url_find_login = True
        assert url_find_login, "Url doesn't have part \"login\""

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME) and \
            self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL) and \
            self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1) and \
            self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Registration form is not presented"