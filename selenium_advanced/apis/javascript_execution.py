import time
import unittest

from selenium import webdriver

class JavaScriptExecution(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_javascript(self):
    driver = self.driver
    # driver.get("https://letskodeit.teachable.com/pages/practice")
    driver.execute_script("window.location = 'https://letskodeit.teachable.com/pages/practice';")
    driver.implicitly_wait(3)
    time.sleep(6)

    # element = driver.find_element(By.ID, "name")
    element = driver.execute_script("return document.getElementById('name');")
    element.send_keys("Test")

  def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
  unittest.main()
