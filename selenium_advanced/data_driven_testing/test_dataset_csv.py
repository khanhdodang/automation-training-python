import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

class PythonOrgSearch(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Firefox()

  def test_search_in_python_org(self):
    with open('test_data.csv') as csvDataFile:
      csvReader = csv.reader(csvDataFile)
      for row in csvReader:
        self.search(row)

  def search(self, keyword):
    driver = self.driver
    driver.get('http://www.python.org')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))

    self.assertIn('Python', driver.title)
    element = driver.find_element_by_name('q')
    element.send_keys(keyword)
    element.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    time.sleep(5)  # sleep for 5 seconds so you can see the results

  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
