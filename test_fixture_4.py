from selenium import webdriver
import pytest


link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope='function')
def browser():
    print('\nstart webdriver')
    browser = webdriver.Chrome()
    yield browser
    print('\nfinish webdriver')
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_id('login_link')

    @pytest.mark.regression
    @pytest.mark.win10
    def test_guest_sould_see_basket_on_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('.basket-mini .btn-group > a')

    @pytest.mark.smoke
    def test_guest_should_see_login_link_2(self, browser):
        browser.get(link)
        browser.find_element_by_id('login_link')

    @pytest.mark.regression
    def test_guest_sould_see_basket_on_page_2(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('.basket-mini .btn-group > a')