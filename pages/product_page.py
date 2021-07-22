from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # Данный метод добавляет товар в корзину
    def add_item_to_cart(self):
        cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        cart.click()

    # Данный метод сравнивает название добавленной книги с названием книги на текущей страницей
    def checking_the_item_in_the_cart(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_SUCCESS).text, "The title of the book is different"

    # Данный метод сравнивает цену добавленной книги с ценой книги на текущей страницей
    def checking_the_price_of_goods(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_INFO).text, "The price of the book is different"

    # Данный метод проверяет отсутствие сообщения об успешном добавлении
    def checking_no_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but " \
                                                                                  "should not be "

    # Данный метод проверяет исчезает ли сообщение об успешном добавлении или нет
    def checking_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"
