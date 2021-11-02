from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

class TestMaimPage():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.driver = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print('\nfinish browser for test suite..')
        self.driver.quit()

    def test_guest_should_see_login_link(self):
        self.driver.get(link)
        self.driver.find_element_by_id('login_link')

    def test_guest_should_see_basket_link_on_page(self):
        self.driver.get(link)
        self.driver.find_element_by_css_selector('.basket-mini .btn-group > a')

class TestMainPage2():

    def setup_method(self):
        print('start webdiver in 2 page...')
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        print('quit webdriver in 2 page...')
        self.driver.quit()

    def test_guest_sould_see_login_link(self):
        self.driver.get(link)
        self.driver.find_element_by_id('login_link')

    def test_guest_sould_see_basket_link_on_page(self):
        self.driver.get(link)
        self.driver.find_element_by_css_selector('.basket-mini .btn-group > a')
