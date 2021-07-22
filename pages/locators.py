from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    ITEM_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    INF_EMPTY_CART = (By.CSS_SELECTOR, "#content_inner > p:nth-child(1)")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    USER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    USER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    USER_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button:nth-child(7)")


class ProductPageLocators:
    CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_SUCCESS = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_PRICE_INFO = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > "
                                           "p:nth-child(1) > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color:nth-child(2)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1)")
