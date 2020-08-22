from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

element = driver.find_element_by_tag_name("input")
elements = driver.find_elements_by_tag_name("input")

driver.close()
driver.quit()
