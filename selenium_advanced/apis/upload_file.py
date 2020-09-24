import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

class UploadFile(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()

  def tearDown(self):
    self.driver.quit()

  def test_upload(self):
    driver = self.driver
    driver.get('http://demo.guru99.com/test/upload/')
    driver.maximize_window()
    driver.implicitly_wait(3)
    # Enter the file path onto the file-selection input field
    uploadElement = driver.find_element(By.ID, "uploadfile_0")
    time.sleep(10)
    uploadElement.send_keys(r"/Users/khanhdo/Downloads/1600916090639.JPEG")
    time.sleep(2)
    driver.find_element(By.ID, "terms").click()
    # click the "UploadFile" button
    driver.find_element(By.NAME, "send").click()

if __name__ == "__main__":
  unittest.main()
