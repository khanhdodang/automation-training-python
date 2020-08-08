from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://google.com")
driver.maximize_window()
time.sleep(3)

driver.get("https://the-internet.herokuapp.com/")

driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)

driver.close()
