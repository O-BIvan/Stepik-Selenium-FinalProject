import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox (default: chrome)")
    parser.addoption('--language', action='store', default='*',
                     help="Choose preferred content language: en, ru, fr, de, es, etc")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == 'chrome':
        print("\n Start 'chrome' browser...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print("\n Start 'firefox' browser...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\n Quit browser..")
    browser.quit()
