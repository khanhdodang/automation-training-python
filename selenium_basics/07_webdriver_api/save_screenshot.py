from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.python.org/')
driver.save_screenshot('screenshot.png')
driver.quit()
