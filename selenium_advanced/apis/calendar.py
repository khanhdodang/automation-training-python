import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

class Calendar(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()

  def test1(self):
    driver = self.driver
    baseUrl = "http://www.expedia.com"
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(30)

    # Click flights tab
    driver.find_element_by_xpath("//span[@class='uitk-tab-text' and text()='Flights']").click()
    # Find departing field
    departingField = driver.find_element_by_id("d1-btn")
    # Click departing field
    departingField.click()
    # Find the date to be selected
    # Expedia website has changed the DOM after the lecture was made
    # Updated new xpath
    dateToSelect = driver.find_element(By.XPATH,
                                       "(//div[@class='uitk-new-date-picker-month'])[1]//button[@data-day='30']")
    # Click the date
    dateToSelect.click()

    time.sleep(3)

  def test2(self):
    driver = self.driver
    baseUrl = "http://www.expedia.com"
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(30)

    # Click flights tab
    driver.find_element_by_xpath("//span[@class='uitk-tab-text' and text()='Flights']").click()
    # Click departing field
    driver.find_element_by_id("d1-btn").click()
    # Expedia website has changed the DOM after the lecture was made
    # Updated new xpath
    calMonth = driver.find_element(By.XPATH, "(//div[@class='uitk-new-date-picker-month'])[1]")
    allValidDates = calMonth.find_elements(By.TAG_NAME, "button")
    time.sleep(2)

    for date in allValidDates:
      if date.text == "30":
        date.click()
      break

  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
