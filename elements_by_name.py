from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://google.com")
driver.maximize_window()
time.sleep(3)
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("Selenium")
inputElement.submit()
time.sleep(3)

driver.close()

'''
It is a standard practice to define unique ids for web elements in an HTML code.
However, there may be cases when these unique identifiers are not present.
Instead, the names are there; then we can also use them to select a web element.

Here is the code snippet that demonstrates the use of <find_element_by_name> method.
Below code opens Google in the browser and performs a text search.

If the HTML code has more than one web element with “@name” attribute, then this method will select the first web element from the list.
If no match occurs, a NoSuchElementException gets raised.
'''
