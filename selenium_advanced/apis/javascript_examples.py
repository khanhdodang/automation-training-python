import unittest
import time

from selenium import webdriver

class JavaScripts(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_javascripts(self):
    driver = self.driver
    driver.execute_script("window.location = 'https://www.makemytrip.com'")
    driver.maximize_window()
    time.sleep(2)
    # Refreshing the page using javaScript
    print("Refreshing the page")
    driver.execute_script("history.go(0)")
    time.sleep(2)
    # Page title using javaScript
    print("Page title is :" + driver.execute_script("return document.title;"))

    search = driver.execute_script("return document.getElementsByClassName('widgetSearchBtn');")
    for s in search:
      print("Search button class :" + s.get_attribute("class"))

    time.sleep(2)
    # gettext method using javaScript
    print(driver.execute_script("return arguments[0].innerHTML", search))
    print(driver.execute_script("return arguments[0].textContent", search))

    print("Scrolling down to coordinates (300,2000)")
    driver.execute_script("window.scrollBy(300,2000)")
    time.sleep(2)

    print("Scrolling down to a element")
    ele = driver.find_element_by_xpath("//*[contains(text(),'About Us')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", ele)
    print("Scrolled successfully to :" + ele.text)
    time.sleep(2)
    # Highlighted elements using javaScript
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", ele,
                          "background:yellow; color: Red; border: 4px dotted solid yellow;")
    print("Highlighted elements :" + ele.text)
    time.sleep(2)

  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
