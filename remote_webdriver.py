from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities={'browserName': 'htmlunit',
                         'version': '2',
                        'javascriptEnabled': True})

'''
Download selenium standalone server at https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-server-standalone/2.53.0

'''
