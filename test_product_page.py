from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    product_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, product_link, 10)
    product_page.open()
    product_page.check_adding_to_basket()

