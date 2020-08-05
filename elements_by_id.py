from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://google.com")
driver.maximize_window()
time.sleep(3)
inputElement = driver.find_element_by_id("lst-ib")
inputElement.send_keys("Selenium")
inputElement.submit()
time.sleep(3)

driver.close()

'''
We use this method when the Id attribute for the element is available.
It is in fact, the most reliable and the fastest way to locate a particular web element on an HTML page.
An Id will always be unique for any object on a web page.
So, we should prefer using Id attribute for locating the elements over other available options.

Here is the code snippet that demonstrates the use of the <find_element_by_id> method.
Below code opens Google in the browser and performs a text search.
If more than one web elements have the same value of id, attribute, this method will return the first element for which the id matches.
It will raise a NoSuchElementException if there is no match.
'''
