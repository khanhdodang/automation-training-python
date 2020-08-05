from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "YOUR EMAILID"
password = "YOUR PASSWORD"
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
element = driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()

'''
Explanation of the code

Code line 1: From selenium module import webdriver
Code line 2: From selenium module import Keys
Code line 3: User is a variable which will be we used to store values of username.
Code line 4: Variable "password" will be used to store values of the password.
Code line 5: In this line, we are initializing "FireFox" by making an object of it.
Code line 6: The "driver.get method" will navigate to a page given by the URL. WebDriver will wait until the page has been completely loaded (that is, the "onload" occasion has let go), before returning control to your test or script.
Code line 7: In this line, we are finding the element of the textbox where the "email" has to be written.
Code line 8: Now we are sending the values to the email section
Code line 9: Same for the password
Code line 10: Sending values to the password section
Code line 11: element.send_keys(Keys.RETURN) is used to press enter after the values are inserted
Code line 12: Close
'''
