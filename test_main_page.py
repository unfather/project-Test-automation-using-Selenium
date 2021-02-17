from pages.main_page import MainPage
from pages.login_page import LoginPage

link =  "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):

    page = MainPage(browser, link)
    page.open()                    
    login_page = page.go_to_login_page() # метод возвращает класс LoginPage
    login_page.should_be_login_page()


    