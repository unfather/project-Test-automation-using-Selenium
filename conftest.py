import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    #select browser
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")
    #select browser language                 
    parser.addoption('--language', action='store', default="en",
                 help="Choose language: ru, en, esp and many others")                 


@pytest.fixture(scope="function")
def browser(request):
    print("\n\nThe machines have risen from the ashes of a nuclear conflagration")
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption('language') 
    browser = None
    if browser_name == "chrome":
        print("\nStart chrome: Cyborgs don't feel pain. I feel")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(20)
    elif browser_name == "firefox":
        print("\nStart firefox: Come with me if you want to live")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(20)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\n\nHasta la vista, baby\nquit browser..")

   

    browser.quit()
