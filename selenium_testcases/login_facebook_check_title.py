from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Firefox
browser = webdriver.Chrome()
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("YOUR EMAILID")
password.send_keys("YOUR PASSWORD")
# Step 4) Click Login
submit.click()
wait = WebDriverWait( browser, 5 )
page_title = browser.title
assert page_title == "Facebook"

browser.close()


'''
Explanation of the code:

Code line 1-2: Import selenium packages
Code line 4: Initialize Firefox by creating an object
Code line 6: Get login page (Facebook)
Code line 8-10: Fetch username, password input boxes and submit button.
Code line 11-12: Enter data into username and password input boxes
Code line 14: Click on the "Submit" button
Code line 15: Create wait object with a timeout of 5 sec.
Code line 16: Capturing the title from "browser" Object.
Code Line 17: Testing the captured title string with "Facebook"
'''

'''
Summary:

Selenium is an open-source web-based automation tool.
Python language is used with Selenium for testing. It has far less verbose and easy to use than any other programming language
The Python APIs empower you to connect with the browser through Selenium
Selenium can send the standard Python commands to different browsers, despite variation in their browser's design.
'''