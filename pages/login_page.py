from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.__contains__("login"), 'URL not contains word "login"'

    def should_be_login_form(self):
        elements_is_present = self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FORM) \
                              * self.is_element_present(*LoginPageLocators.LOGIN_PASS_FORM) \
                              * self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT_BUTTON)
        assert elements_is_present, "Not all elements of login form are present"

    def should_be_register_form(self):
        elements_is_present = self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_FORM) \
                              * self.is_element_present(*LoginPageLocators.REGISTER_PASS1_FORM) \
                              * self.is_element_present(*LoginPageLocators.REGISTER_PASS2_FORM) \
                              * self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_FORM) \
                              * self.is_element_present(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        assert elements_is_present, "Not all elements of register form are present"

    def register_new_user(self, email, password):
        self.get_element(*LoginPageLocators.REGISTER_EMAIL_FORM).send_keys(email)
        self.get_element(*LoginPageLocators.REGISTER_PASS1_FORM).send_keys(password)
        self.get_element(*LoginPageLocators.REGISTER_PASS2_FORM).send_keys(password)
        self.get_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON).click()

