import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
    print('\nstart driver from fixture...')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit driver from fixture...')
    browser.quit()

class TestMaimPage():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_id('login_link')

    def test_guest_should_see_basket_link_on_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('.basket-mini .btn-group > a')

class TestMainPage2():

    def test_guest_sould_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_id('login_link')

    def test_guest_sould_see_basket_link_on_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('.basket-mini .btn-group > a')
