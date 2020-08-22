from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.python.org")
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "id-search-field"))
    )
    element.click()
finally:
    driver.quit()
