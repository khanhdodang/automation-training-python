from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://google.com")
driver.maximize_window()
time.sleep(3)
element = driver.find_element_by_name("q")
elements = driver.find_elements_by_name("q")

driver.close()
