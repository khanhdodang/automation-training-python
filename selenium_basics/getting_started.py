from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

element = driver.find_element_by_id("username")
element.clear()
element.send_keys("tomsmith")

element = driver.find_element_by_id("password")
element.clear()
element.send_keys("SuperSecretPassword!")

element = driver.find_element_by_xpath("//button[@type='submit']")
element.click()

element = driver.find_element_by_id("flash")
message = element.text

assert "You logged into a secure area!" in message
driver.close()
driver.quit()
