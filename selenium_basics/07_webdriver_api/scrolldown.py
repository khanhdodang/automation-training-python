# import webdriver
from selenium import webdriver
# import time
import time

# create webdriver object
driver = webdriver.Chrome()
driver.maximize_window()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(3)

driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

time.sleep(3)

driver.close()
