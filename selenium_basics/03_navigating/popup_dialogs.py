from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(3)

element = driver.find_element_by_xpath("//button[text()='Click for JS Alert']")
element.click()

alert = driver.switch_to_alert()
alert.accept()

element = driver.find_element_by_xpath("//button[text()='Click for JS Confirm']")
element.click()

alert = driver.switch_to_alert()
alert.dismiss()

element = driver.find_element_by_xpath("//button[text()='Click for JS Prompt']")
element.click()

alert = driver.switch_to_alert()
alert.dismiss()

driver.close()
