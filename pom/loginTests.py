import unittest
from selenium import webdriver
from loginPage import LoginPage


class loginTests(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.get('https://the-internet.herokuapp.com/login')

  def tearDown(self):
    self.driver.close()

  def test_login_incorrect_username(self):
    login_page = LoginPage(self.driver)
    login_page.login('tomsmith1', 'SuperSecretPassword!')
    assert login_page.login_message_displayed()

  def test_login_blank_password(self):
    login_page = LoginPage(self.driver)
    login_page.login('tomsmith', '')
    assert login_page.login_message_displayed()

  def test_login_blank_username(self):
    login_page = LoginPage(self.driver)
    login_page.login('', 'SuperSecretPassword!')
    assert login_page.login_message_displayed()

  if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(loginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
