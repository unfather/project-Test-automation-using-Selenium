import pytest
from pages.product_page import ProductPage

link =  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
arry_link = [f'{link}{i}' for i in range(10) if i != 7]
arry_link += [pytest.param(f'{link}7', marks=pytest.mark.xfail)]

@pytest.mark.parametrize('link', arry_link)
def test_guest_can_add_product_to_basket(browser, link):
    
    page = ProductPage(browser, link)
    page.open()
    page.possible_to_add_product_to_basket()

