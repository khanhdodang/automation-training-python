from pages.base_page_object import BasePage
from locators import ResultPageLocators
import logging

class ResultPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

  def get_message(self):
    element = self.driver.find_element(*ResultPageLocators.LABEL_MESSAGE)

    message = "Get the message result '{}'"
    logging.info(message.format(element.text))
    return element.text
