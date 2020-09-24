import time
import unittest

from selenium import webdriver

class AutoComplete(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_auto_complete(self):
    driver = self.driver
    baseUrl = "http://www.southwest.com"
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(30)

    # Send Partial Data
    cityField = driver.find_element_by_id("LandingAirBookingSearchForm_originationAirportCode")
    cityField.send_keys("New York")
    time.sleep(3)
    # Find the item and click
    itemToSelect = driver.find_element_by_xpath("//button[contains(@aria-label,'New York (LaGuardia), NY - LGA')]")
    itemToSelect.click()

  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
