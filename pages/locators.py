from selenium.webdriver.common.by import By


class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    #REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    pass

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    BUTTON_TO_BASKET = (By.CSS_SELECTOR, ".page_inner .btn-default:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") 
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form .btn")      


class BasketPageLocators():
    #form with books, when empty it is not there
    FORM_BASKET_BOOKS = (By.CSS_SELECTOR, "#basket_formset")
    # the message that the basket is empty
    LABEL_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner :first-child") 
    
 
class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket") 
    SUCCESS_MESSAGE_ADD_TO_CART = (By.CSS_SELECTOR, "#messages .alert-noicon:nth-child(1)")
    NAME_PRODUCT = (By.CSS_SELECTOR, "#content_inner h1")
    NAME_ADDED_PRODUCT = (By.CSS_SELECTOR, "#messages .alert-noicon:nth-child(1) strong")