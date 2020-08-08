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
elem = driver.find_element_by_partial_link_text("Python")
elem = driver.find_elements_by_partial_link_text("Python")

driver.close()

'''
For locating the element by using the link text method, we need to provide the complete Link text.
However, the partial link text method enables us to select a hyperlink by giving only a part of the link text.
In the above example if we use the partial link text method, then the code will become as.
This code opens the Python tutorial web page as in the above code.
'''
