from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators, BasketPageLocators

class BasketPage(BasePage):

    
    def should_not_be_button_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BUTTON_TO_BASKET), \
            "Success message is presented, but should not be"
    

    def should_not_products_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.FORM_BASKET_BOOKS), \
            "Message about adding to the basket, the basket is not empty"


    def should_find_text_basket_is_empty(self):
        assert not(self.is_not_element_present(*BasketPageLocators.LABEL_BASKET_EMPTY)), \
            "There is no text indicating that the basket is empty"
         