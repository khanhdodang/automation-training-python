import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.result_page import ResultPage
from base_test import Test_Base
from TestData import TestData

class HerokuAppLogin(Test_Base):
    """A sample test class to show how page object works"""
    def setUp(self):
        super().setUp(TestData.BROWSER)

    def tearDown(self):
         super().tearDown()

    def test_login_successfully(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.is_title_matches())
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        result_page = ResultPage(self.driver)

        print(result_page.get_message())
        self.assertIn("You logged into a secure area!", result_page.get_message())

    def test_login_with_invalid_username(self):
        login_page = LoginPage(self.driver)
        login_page.login(TestData.FAKE_USERNAME, TestData.PASSWORD)
        result_page = ResultPage(self.driver)
        
        print(result_page.get_message())
        self.assertIn("Your username is invalid!", result_page.get_message())

    def test_login_with_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.login(TestData.USERNAME, TestData.FAKE_PASSWORD)
        result_page = ResultPage(self.driver)
        
        print(result_page.get_message())
        self.assertIn("Your password is invalid!", result_page.get_message())
    
    @unittest.SkipTest
    def test_login_with_invalid_username_password(self):
        login_page = LoginPage(self.driver)
        login_page.login(TestData.FAKE_USERNAME, TestData.FAKE_PASSWORD)
        result_page = ResultPage(self.driver)
        
        print(result_page.get_message())
        self.assertIn("Your password is invalid!", result_page.get_message())

if __name__ == "__main__":
    unittest.main()
