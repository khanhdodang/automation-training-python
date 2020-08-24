from pages.base_page_object import BasePage
from locators import LoginPageLocators
from TestData import TestData

class LoginPage(BasePage):
  URL = 'https://the-internet.herokuapp.com/login'

  def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver
    self.driver.get(TestData.BASE_URL)

  def login(self, username, password):
    self.enter_username(username)
    self.enter_password(password)
    self.click_login_button()

  def enter_username(self, username):
    self.enter_text(LoginPageLocators.INPUT_USERNAME, username)

  def enter_password(self, password):
    self.enter_text(LoginPageLocators.INPUT_PASSWORD, password)

  def click_login_button(self):
    self.click(LoginPageLocators.BUTTON_LOGIN)

  def is_title_matches(self):
    """Verifies that the hardcoded text "The Internet" appears in page title"""
    return "The Internet" in self.driver.title