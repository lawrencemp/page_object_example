from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException


class ProductPage(BasePage):
    def check_adding_to_basket(self):
        self.check_access_elements()
        self.add_book_to_basket()
        assert self.check_alerts_after_adding, "Title or price is not the same"

    def add_book_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def check_access_elements(self):
        condition = self.is_element_present(*ProductPageLocators.BOOK_TITLE) \
                    * self.is_element_present(*ProductPageLocators.BOOK_PRICE) \
                    * self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        assert condition, f"Not all elements are available {self.is_element_present(*ProductPageLocators.BOOK_TITLE)}, " \
                          f"{self.is_element_present(*ProductPageLocators.BOOK_PRICE)}," \
                          f" {self.is_element_present(*ProductPageLocators.BOOK_PRICE)}"

    def check_alerts_after_adding(self):
        try:
            msg = ""
            book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
            if book_title != self.browser.find_element(*ProductPageLocators.BOOK_ADDED_TITLE_ALERT).text:
                msg += "Titles"
            book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
            if book_price != self.browser.find_element(*ProductPageLocators.BOOK_ADDED_PRICE_ALERT).text:
                if msg == "":
                    msg += "Prices"
                else:
                    msg += " and Prices"
            if msg != "":
                msg += " are not equal"
                raise Exception(msg)
            return True
        except NoSuchElementException():
            return False
        except Exception:
            print(msg)
            return False



