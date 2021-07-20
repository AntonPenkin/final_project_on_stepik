from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_cart(self):
        cart = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        cart.click()

    def checking_the_item_in_the_cart(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == self.browser.find_element(*ProductPageLocators.BOOK_NAME_SUCCESS).text, "The title of the book is different"

    def checking_the_price_of_goods(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text == self.browser.find_element(*ProductPageLocators.BOOK_PRICE_INFO).text, "The price of the book is different"
