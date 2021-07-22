from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.login
class TestUserAddToBasketFromProductPage:
    # Данная фикстура перед каждым тестом в данном классе заходит на страницу входа (Login) и регистрирует нового
    # пользователя, а также после регистрации проверяет залогинен ли пользователь
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(str(time.time()) + "@mail.ru", "1qazXSW@!")
        page.should_be_authorized_user()

    # Проверяет, может ли залогиненный пользователь добавить товар в корзину, а также после добавления в корзину
    # сравнивает название и цену товара
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_item_to_cart()
        page.solve_quiz_and_get_code()
        page.checking_the_item_in_the_cart()
        page.checking_the_price_of_goods()

    # Проверяет, есть ли сообщение об успешном добавлении товара, если сообщение есть, тест не будет пройден
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.checking_no_success_message_after_adding_product_to_basket()


# Проверяет, может ли не залогиненный пользователь добавить товар в корзину, а также после добавления в корзину
# сравнивает название и цену товара
@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer',
                         ['0', '1', '2', '3', '4', '5', '6', pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    page.checking_the_item_in_the_cart()
    page.checking_the_price_of_goods()


# Проверяет, есть ли сообщение об успешном добавлении товара, если сообщение есть, тест не будет пройден
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.checking_no_success_message_after_adding_product_to_basket()


# Добавляет товар в корзину и проверяет, есть ли сообщение об успешном добавлении товара, если сообщение есть,
# тест не будет пройден
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.checking_no_success_message_after_adding_product_to_basket()


# Добавляет товар в корзину и ждет когда исчезнет сообщение об успешном добавлении в корзину, если сообщение не
# исчезает за заданный промежуток времени, тест не будет пройден
@pytest.mark.xfail
def test_message_dissapeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.checking_message_disappeared_after_adding_product_to_basket()


# Заходит на страницу товара и проверяет, есть ли на странице ссылка на страницу входа (login)
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# Заходит на страницу товара и переходит с нее на страницу входа (login)
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


# Заходит на страницу товара, после этого переходит в корзину и проверяет, отсутствуют ли товары в корзине,
# и есть ли сообщение об отсутствие товаров
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/neuromancer_13/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_no_items_in_the_cart()
    page.should_be_an_empty_shopping_cart_notice()
