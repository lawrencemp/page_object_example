from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')


class LoginPageLocators():
    LOGIN_EMAIL_FORM = (By.XPATH, '//input[@id="id_login-username"]')
    LOGIN_PASS_FORM = (By.XPATH, '//input[@id="id_login-password"]')
    LOGIN_SUBMIT_BUTTON = (By.XPATH, '//button[@name="login_submit"]')
    REGISTER_EMAIL_FORM = (By.XPATH, '//input[@id="id_registration-email"]')
    REGISTER_PASS1_FORM = (By.XPATH, '//input[@id="id_registration-password1"]')
    REGISTER_PASS2_FORM = (By.XPATH, '//input[@id="id_registration-password2"]')
    REGISTER_SUBMIT_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')