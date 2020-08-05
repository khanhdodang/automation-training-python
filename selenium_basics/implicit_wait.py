from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(100)

driver.get("http://google.com")
driver.maximize_window()

print("Implicit Wait Example")

inputElement = driver.find_element_by_id("lst-ib")
inputElement.send_keys("Techbeamers")
inputElement.submit()

driver.close()
