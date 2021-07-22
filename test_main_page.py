from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page_login = LoginPage(browser, browser.current_url)
    page_login.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_no_items_in_the_cart()
    page.should_be_an_empty_shopping_cart_notice()
