import pytest, time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

link =  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
arry_link = [f'{link}/?promo=offer{i}' for i in range(1) if i != 7]
arry_link += [pytest.param(f'{link}/?promo=offer7', marks=pytest.mark.xfail)]

class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page_login = LoginPage(browser, link)
        self.page_login.open()
        password = str(time.time())
        email = password + "@fakemail.org"   
        self.page_login.register_new_user(email, password)
        self.page_login.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message() 
                               
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.equivalence_of_the_name_of_the_added_product()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


@pytest.mark.need_review
#@pytest.mark.parametrize('link', arry_link)
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()                    
    page.go_to_basket_page()
    page.should_not_products_in_the_basket()
    page.should_find_text_basket_is_empty()


@pytest.mark.need_review
#@pytest.mark.parametrize('link', arry_link)
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.equivalence_of_the_name_of_the_added_product()


@pytest.mark.parametrize('link', arry_link)
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()   
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize('link', arry_link)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_not_disappeared()

