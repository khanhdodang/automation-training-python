import unittest

from selenium import webdriver

class WindowSize(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_window_size(self):
    driver = self.driver
    driver.maximize_window()
    driver.get("https://letskodeit.teachable.com/pages/practice")
    driver.implicitly_wait(3)

    height = driver.execute_script("return window.innerHeight;")
    width = driver.execute_script("return window.innerWidth;")
    print("Height: " + str(height))
    print("Width: " + str(width))

  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
