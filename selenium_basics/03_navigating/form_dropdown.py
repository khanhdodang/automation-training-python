from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()
time.sleep(3)

element = driver.find_element_by_id("dropdown")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()

select = Select(driver.find_element_by_id('dropdown'))
# select.deselect_all() You may only deselect all options of a multi-select
all_selected_options = select.all_selected_options
select.select_by_index(0)
select.select_by_visible_text("Option 1")
select.select_by_value("1")


driver.close()
