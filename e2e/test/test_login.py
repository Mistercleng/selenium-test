import unittest
from selenium import webdriver
from e2e.page_object.login_page import LoginPage

class Authentication(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.driver.get("https://www.saucedemo.com/")
        # self.driver.maximize_window()
        self.accept_next_alert = True

    def test_authentication(self):
        page = LoginPage(self.driver)
        self.assertEqual('Swag Labs', page.validation_title())
        self.assertTrue(page.validation_logon_name())
        page.authentication_with_success('standard_user', 'secret_sauce')
        self.assertEqual('Products', page.validation_text_product())

    def test_authentication_with_logout(self):
        page = LoginPage(self.driver)
        self.assertEqual('Swag Labs', page.validation_title())
        self.assertTrue(page.validation_logon_name())
        page.authentication_with_success('standard_user','secret_sauce')
        self.assertEqual('Products',page.validation_text_product())
        page.logout_session()

    def test_authentication_with_wrong_password(self):
        page = LoginPage(self.driver)
        self.assertEqual('Swag Labs', page.validation_title())
        self.assertTrue(page.validation_logon_name())
        page.authentication_with_success('standard_user','123456')
        self.assertEqual('Epic sadface: Username and password do not match any user in this service',page.validation_erro_message())


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)