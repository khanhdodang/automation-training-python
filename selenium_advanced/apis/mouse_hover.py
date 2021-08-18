import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class MouseHovering(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_hover(self):
    driver = self.driver
    baseUrl = "https://courses.letskodeit.com/practice"
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(3)

    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(2)
    element = driver.find_element(By.ID, "mousehover")
    itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"
    try:
      actions = ActionChains(driver)
      actions.move_to_element(element).perform()
      time.sleep(2)
      topLink = driver.find_element(By.XPATH, itemToClickLocator)
      actions.move_to_element(topLink).click().perform()
    except:
      print("Mouse Hover failed on element")

  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
