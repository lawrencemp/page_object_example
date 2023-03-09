from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    EMAIL_FORM = ''
    PASS_FORM = ''
    SUBMIT_BUTTON = ''