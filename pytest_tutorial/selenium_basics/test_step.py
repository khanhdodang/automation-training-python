#Using @pytest.mark.incremental decorator to stop test suite after n test failure using Selenium test automation in Python with pytest 
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys
import urllib3
import warnings
# @pytest.mark.incremental Stop Test Suite after N Test Failures in Pytest
@pytest.mark.usefixtures("driver_init")
@pytest.mark.incremental
class Test_Scenario_1:
  def test_1(self):
    self.driver.get('https://www.lambdatest.com/blog/')
    self.driver.maximize_window()

    expected_title = "LambdaTest | A Cross Browser Testing Blog"
    assert expected_title ==  self.driver.title
    time.sleep(5)

  def test_2(self):
    self.driver.get('https://www.google.com/')
    self.driver.maximize_window()
    title = "Google"
    assert title == self.driver.title

    search_text = "LambdaTest"
    search_box = self.driver.find_element_by_xpath("//input[@name='q']")
    search_box.send_keys(search_text)

    time.sleep(5)
    search_box.submit()

    time.sleep(5)
    
    # Click on the LambdaTest HomePage Link
    # This test will fail as the titles will not match
    title = "Cross Browser Testing Tool | Test Your Website on Different Browsers | LambdaTest1"
    lt_link = self.driver.find_element_by_xpath("//span[text()='LambdaTest - Browser Testing Tool On Cloud']")
    lt_link.click()

    time.sleep(10)
    assert title == self.driver.title   
    time.sleep(2)

  # As test_2 fails, test_3 will xfail i.e. skipped and all subsequent tests in the same class
  # will be marked as xfailed
  def test_3(self):
    self.driver.get('https://www.lambdatest.com/')
    self.driver.maximize_window()

    expected_title = "Cross Browser Testing Tools | Free Automated Website Testing | LambdaTest"
    assert expected_title ==  self.driver.title
    time.sleep(5)
 
@pytest.mark.usefixtures("driver_init")
@pytest.mark.incremental
class Test_Scenario_2:
  def test_4(self):
    self.driver.get('https://lambdatest.github.io/sample-todo-app/')
    self.driver.maximize_window()

    self.driver.find_element_by_name("li1").click()
    self.driver.find_element_by_name("li2").click()

    title = "Sample page - lambdatest.com"
    assert title ==  self.driver.title

    sample_text = "Happy Testing at LambdaTest"
    email_text_field =  self.driver.find_element_by_id("sampletodotext")
    email_text_field.send_keys(sample_text)
    time.sleep(5)

    self.driver.find_element_by_id("addbutton").click()
    time.sleep(5)

    assert self.driver.find_element_by_xpath("//span[.='Happy Testing at LambdaTest']").text == sample_text
