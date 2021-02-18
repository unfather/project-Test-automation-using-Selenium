from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def possible_to_add_product_to_basket(self):
        buttin_add_link = self.browser.find_element(*MainPageLocators.BUTTON_ADD_TO_BASKET)
        buttin_add_link.click()
        self.solve_quiz_and_get_code()

        
        