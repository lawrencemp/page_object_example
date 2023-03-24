from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert self.browser.current_url.__contains__("basket"), 'URL not contains word "basket"'

    def go_to_basket(self):
        self.open()

    def should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE) * \
            self.is_not_element_present(*BasketPageLocators.PRODUCTS_SUMMARY_FORM), \
        "Basket is not empty but should be"

    def should_have_products(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCTS_SUMMARY_FORM) * \
            self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
        "Basket is empty but should have products"