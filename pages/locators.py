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


class ProductPageLocators():
    BOOK_TITLE = (By.XPATH, '//div[contains(@class,"product_main")]/h1')
    BOOK_PRICE = (By.XPATH, '//p[@class="price_color"]')
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//form[@id="add_to_basket_form"]/button')
    BOOK_ADDED_TITLE_ALERT = (By.XPATH, '//div[@id="messages"]//strong')
    BOOK_ADDED_PRICE_ALERT = (By.XPATH, '//div[@id="messages"]//p/strong')


