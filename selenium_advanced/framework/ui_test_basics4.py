import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://www.google.com/')
assert "Google" in driver.title

elem = driver.find_element_by_name('q')
elem.send_keys('Selenium')
elem.send_keys(Keys.RETURN)
assert 'No results found.' not in driver.page_source
driver.close()
