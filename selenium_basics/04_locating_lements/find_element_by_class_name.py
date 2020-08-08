from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

elements = driver.find_element_by_class_name("example")
elements = driver.find_elements_by_class_name("example")

driver.close()
driver.quit()
