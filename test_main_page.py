from pages.basket_page import BasketPage
from pages.base_page import BasePage
from pages.locators import BasePageLocators
from pages.login_page import LoginPage
import pytest, time

link =  "http://selenium1py.pythonanywhere.com/"

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):

    page = BasketPage(browser, link)
    page.open()                    
    page.go_to_basket_page()
    page.should_not_products_in_the_basket()
    page.should_find_text_basket_is_empty()

@pytest.mark.login_guest
class TestLoginFromMainPage():
        
    def test_guest_can_go_to_login_page(self,browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_page()

    def test_guest_should_see_login_link(self,browser):
        
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()

