from pages.base_page_object import BasePage
from locators import ResultPageLocators

class ResultPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)

  def get_message(self):
    element = self.driver.find_element(*ResultPageLocators.LABEL_MESSAGE)
    return element.text