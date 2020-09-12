import unittest
from selenium import webdriver
from loginPage import LoginPage
from account import Account

class loginTests(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.get('https://the-internet.herokuapp.com/login')

  def tearDown(self):
    self.driver.close()

  def test_login_successfully(self):
    login_page = LoginPage(self.driver)
    login_page.login('tomsmith', 'SuperSecretPassword!')
    self.assertTrue(login_page.login_message_displayed())
    self.assertIn("You logged into a secure area!", login_page.get_message())

  def test_login_blank_password(self):
    login_page = LoginPage(self.driver)
    login_page.login('tomsmith', '')
    self.assertTrue(login_page.login_message_displayed())
    self.assertIn("Your password is invalid!", login_page.get_message())

  def test_login_blank_username(self):
    login_page = LoginPage(self.driver)
    login_page.login('', 'SuperSecretPassword!')
    self.assertTrue(login_page.login_message_displayed())
    self.assertIn("Your username is invalid!", login_page.get_message())

  def test_login_with_object(self):
    account = Account('tomsmith', 'SuperSecretPassword!')
    login_page = LoginPage(self.driver)
    login_page.login_object(account)
    self.assertTrue(login_page.login_message_displayed())
    self.assertIn("You logged into a secure area!", login_page.get_message())
 
  if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(loginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
