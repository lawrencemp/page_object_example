from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException


class ProductPage(BasePage):
    def check_adding_to_basket(self):
        self.check_access_elements()
        self.add_book_to_basket()
        self.solve_quiz_and_get_code()
        assert self.check_alerts_after_adding(), "Title or price is not the same"

    def add_book_to_basket(self):
        self.get_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def check_access_elements(self):
        condition = self.is_element_present(*ProductPageLocators.BOOK_TITLE) \
                    * self.is_element_present(*ProductPageLocators.BOOK_PRICE) \
                    * self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        assert condition, "Not all elements are available "

    def check_alerts_after_adding(self):
        try:
            msg = ""
            book_title = self.get_element(*ProductPageLocators.BOOK_TITLE).text
            if book_title != self.get_element(*ProductPageLocators.BOOK_ADDED_TITLE_ALERT).text:
                msg += "Titles"
            book_price = self.get_element(*ProductPageLocators.BOOK_PRICE).text
            if book_price != self.get_element(*ProductPageLocators.BOOK_ADDED_PRICE_ALERT).text:
                if msg == "":
                    msg += "Prices"
                else:
                    msg += " and Prices"
            if msg != "":
                msg += " are not equal"
                raise Exception(msg)
            return True
        except NoSuchElementException:
            return False
        except Exception:
            return False

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_ADDED_TITLE_ALERT), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_ADDED_TITLE_ALERT, timeout=10), \
            "Success message is presented, but should disappear"
