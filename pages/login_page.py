from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Данный метод проверяет, действительно ли текущая страница, это страница авторизации
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "This is not a login page"

    # Данный метод проверяет, есть ли на странице форма авторизации
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form missing"

    # Данный метод проверяет, есть ли на странице форма регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form missing"

    # Данный метод ищет поля Email, Password, Confirm Password и передает в них значения
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.USER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.USER_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.USER_PASS_CONF).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
