from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # CSS селектор ссылки на страницу авторизацию
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")  # CSS селектор ссылки на страницу корзины
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")  # CSS селектор иконки авторизированного пользователя


class BasketPageLocators:
    ITEM_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")  # CSS селектор элемента который добавлен в корзину
    INF_EMPTY_CART = (By.CSS_SELECTOR, "#content_inner > p:nth-child(1)")  # CSS селектор сообщения (Ваша корзину пуста)


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  # CSS селектор формы авторизации
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  # CSS селектор формы регистрации
    USER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")  # CSS селектор поля Email на форме регистрации
    USER_PASS = (By.CSS_SELECTOR, "#id_registration-password1")  # CSS селектор поля Password на форме регистрации
    USER_PASS_CONF = (By.CSS_SELECTOR, "#id_registration-password2")  # CSS селектор поля Confirm на форме регистрации
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button:nth-child(7)")  # CSS селектор кнопки Register


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")  # CSS селектор кнопки "Добавить в
    # корзину"
    PRODUCT_NAME_SUCCESS = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")  # CSS селектор названия
    # книги которую добавили в корзину
    PRODUCT_PRICE_INFO = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > "
                                           "p:nth-child(1) > strong")  # CSS селектор цены книги которую добавили
    # корзину
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")  # CSS селектор названия книги
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color:nth-child(2)")  # CSS селектор цены книги
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1)")  # CSS селектор сообщения об успешном добавлении
    # книги в корзину
