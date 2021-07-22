from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Данный метод проверяет, есть ли в корзине добавленные товары
    def should_be_no_items_in_the_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), "There is an item in the cart"

    # Данный метод проверяет, есть ли сообщение об отсутствии товаров в корзине
    def should_be_an_empty_shopping_cart_notice(self):
        assert self.is_element_present(*BasketPageLocators.INF_EMPTY_CART), "There are items in the cart"
