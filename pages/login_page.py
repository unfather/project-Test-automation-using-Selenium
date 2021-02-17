from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        page_url = self.browser.current_url
        assert "login" in page_url, "Warning! Invalid url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*MainPageLocators.LOGIN_FORM), "Not found login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*MainPageLocators.REGISTER_FORM), "Not found register form"
