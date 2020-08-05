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
elem.click()
time.sleep(3)

driver.close()

'''
We use this method for selecting hyperlinks from a web page.
If multiple elements have the same link text, then this method selects the first element with a match.
It works only on links (hyperlinks), that is why we call it <Link Text locator>.

Here is the code snippet that demonstrates the use of <find_element_by_link_text> method.
Below code opens Google in the browser and performs a text search.
After that, it opens a Hyperlink with link text as “Python Tutorial.”
'''
