from selenium.webdriver.common.by import By
import time

# This is the base page which defines attributes and methods that all other pages will share
class BasePage(object):
  def __init__(self, driver):
    self.driver = driver
    self.driver.implicitly_wait(5)
    self.timeout = 30
    self.driver.maximize_window()


# This class represents the login page which defines attributes and methods associated with the login page
class LoginPage(BasePage):
  username = (By.ID, 'username')
  password = (By.ID, 'password')
  submitButton = (By.XPATH, '//button/i[contains(text(),"Login")]')
  loginMessage = (By.ID, 'flash')

  def set_username(self, username):
    emailElement = self.driver.find_element(*LoginPage.username)
    emailElement.send_keys(username)

  def set_password(self, password):
    pwordElement = self.driver.find_element(*LoginPage.password)
    pwordElement.send_keys(password)

  def click_submit(self):
    submitBttn = self.driver.find_element(*LoginPage.submitButton)
    submitBttn.click()

  def login_message_displayed(self):
    notifcationElement = self.driver.find_element(*LoginPage.loginMessage)
    return notifcationElement.is_displayed()

  def login(self, username, password):
    self.set_username(username)
    self.set_password(password)
    self.click_submit()
    time.sleep(5)  # sleep for 5 seconds so you can see the results

  def login_object(self, account):
    self.set_username(account.username)
    self.set_password(account.password)
    self.click_submit()
