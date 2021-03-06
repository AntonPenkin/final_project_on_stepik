from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # Данный метод принимает аргумент в виде ссылки и открывает её
    def open(self):
        self.browser.get(self.url)

    # Данный метод находит ссылку на страницу авторизации и переходит на неё
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    # Данный метод находит ссылку на страницу с добавленными в корзину товарами и переходит на неё
    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    # Данный метод проверяет, есть ли на текущей странице ссылка на страницу авторизации (login)
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # Данный метод проверяет, есть ли на текущей странице переданный элемент
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Данный метод проверяет, отсутствие на странице переданный элемента
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # Данный метод проверяет, исчез ли переданный элемент со страницы
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # Данный метод решает задачу, которая появляется при добавлении товара
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # Данный метод проверяет, авторизирован пользователь или нет
    def should_be_authorized_user(self):
        assert self.is_element_present(
            *BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"
