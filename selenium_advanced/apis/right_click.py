import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class RightClick(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_right_click(self):
    driver = self.driver
    baseUrl = "http://the-internet.herokuapp.com/context_menu"
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(30)

    menu_area = driver.find_element_by_id('hot-spot')
    ActionChains(driver).context_click(menu_area).perform()

    alert = driver.switch_to_alert()
    assert alert.text == 'You selected a context menu'
    alert.dismiss()
    driver.switch_to.default_content

  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
