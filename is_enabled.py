# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element_by_link_text("Courses")

# print value
print(element.is_enabled())

driver.close()
