import re
import unittest

from selenium import webdriver

class RegularExpression(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_regular_expression(self):
    driver = self.driver
    baseUrl = "http://www.airindia.in/contact-details.htm"
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(30)

    doc = driver.page_source
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)
    list_new = []

    print('List emails from page_source\n')
    for email in emails:
      list_new.append(str(email))
      print(email)

    emails = [email.text for email in driver.find_elements_by_class_name('linkText') if "@" in email.text]
    list_new = []

    print('\nList emails from linkText\n')
    for email in emails:
      list_new.append(str(email))
      print(email)

  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
