import time

BOOK = "Coders at Work"
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_of_finding_add_button_to_cart(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_element_by_class_name('btn-add-to-basket').text
    assert len(button) != 0, "The button is lost"
    if button == "Ajouter au panier":
        print('\nThe selected language logic for launching the browser: French')
   
def test_add_to_cart(browser):
    browser.get(link)
    browser.find_element_by_class_name('btn-add-to-basket').click()
    add_messenge = browser.find_element_by_css_selector('#messages :nth-child(1) .alertinner strong').text
    assert add_messenge == BOOK, f"{BOOK} has NOT been added to your cart ! "
    browser.find_element_by_css_selector('.btn-group a.btn-default').click()
    time.sleep(2)
    check_cart = browser.find_element_by_css_selector('.col-sm-4 h3 a').text
    assert check_cart == BOOK, f"The book {BOOK} was not found in the shopping cart !"

