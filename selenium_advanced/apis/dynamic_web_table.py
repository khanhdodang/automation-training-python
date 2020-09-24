import unittest

from selenium import webdriver

class DynamicWebTable(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_dynamic_table(self):
    driver = self.driver
    baseUrl = "http://qavalidation.com/demo/"
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(30)

    columns = len(self.driver.find_elements_by_xpath(".//*[@id='table01']/tbody/tr[1]/td"))
    rows = len(self.driver.find_elements_by_xpath(".//*[@id='table01']/tbody/tr"))
    print("rows - ", rows)  # rows -  3
    print("columns - ", columns)  # columns -  4

    for row in range(1, rows):
      for col in range(2, columns):
        values = self.driver.find_element_by_xpath(
          ".//*[@id='table01']/tbody/tr[" + str(row) + "]/td[" + str(col) + "]").text
        print(" Dynamic web table index {0} ,{1} value is {2} ".format(row, col, values))

  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
