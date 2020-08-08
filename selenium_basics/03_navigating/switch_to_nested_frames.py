from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/nested_frames")
time.sleep(3)

driver.switch_to_default_content()
driver.switch_to.frame(driver.find_element_by_name("frame-top"))
driver.switch_to.frame(driver.find_element_by_name("frame-left"))
driver.switch_to.parent_frame()
driver.switch_to.frame(driver.find_element_by_name("frame-middle"))
driver.switch_to.parent_frame()
driver.switch_to.frame(driver.find_element_by_name("frame-right"))
driver.switch_to.default_content()

driver.switch_to_frame(driver.find_element_by_name("frame-bottom"))
driver.switch_to.parent_frame()

driver.close()
