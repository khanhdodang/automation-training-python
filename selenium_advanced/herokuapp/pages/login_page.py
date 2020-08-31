from Pages.base_page_object import BasePage
from Locators.locators import LoginPageLocators
from TestData.TestData import TestData
from Objects.Account import Account
import logging

class LoginPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.navigate_to(TestData.BASE_URL)
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

  def login(self, username, password):
    self.enter_username(username)
    self.enter_password(password)
    self.click_login_button()

  def login(self, Accounts):
    self.enter_username(Accounts.username)
    self.enter_password(Accounts.password)
    self.click_login_button()

  def enter_username(self, username):
    message = "Enter the username '{}'"
    logging.info(message.format(username))

    self.enter_text(LoginPageLocators.INPUT_USERNAME, username)

  def enter_password(self, password):
    message = "Enter the password '{}'"
    logging.info(message.format(password))

    self.enter_text(LoginPageLocators.INPUT_PASSWORD, password)

  def click_login_button(self):
    logging.info("Click Login button")

    self.click(LoginPageLocators.BUTTON_LOGIN)

  def is_title_matches(self):
    logging.info("Check the title match or not")
    """Verifies that the hardcoded text "The Internet" appears in page title"""
    return "The Internet" in self.get_title()
