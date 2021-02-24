from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):


    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()
        #self.solve_quiz_and_get_code()


    def equivalence_of_the_name_of_the_added_product(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_added_product = self.browser.find_element(*ProductPageLocators.NAME_ADDED_PRODUCT).text
        assert name_added_product == name_product, \
            "The name of the added product and the added product are different"  
    


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ADD_TO_CART), \
            "Success message is presented, but should not be"


    def should_not_be_not_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_ADD_TO_CART),\
             "Success message is not disappeared"

     

        
        