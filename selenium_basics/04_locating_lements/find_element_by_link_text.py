from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://google.com")
driver.maximize_window()
time.sleep(3)
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("Techbeamers")
inputElement.submit()
time.sleep(3)
elem = driver.find_element_by_link_text("Python Tutorial")
elem = driver.find_elements_by_link_text("Python Tutorial")

driver.close()
