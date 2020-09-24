import unittest
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Slider(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_slider(self):
    driver = self.driver
    baseUrl = "https://jqueryui.com/slider/"
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(3)

    driver.switch_to.frame(0)

    element = driver.find_element(By.XPATH, "//div[@id='slider']//span")
    time.sleep(2)
    try:
      actions = ActionChains(driver)
      actions.drag_and_drop_by_offset(element, 100, 0).perform()
      print("Sliding passed.")
      time.sleep(2)
    except:
      print("Sliding failed.")

  def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
  unittest.main()
