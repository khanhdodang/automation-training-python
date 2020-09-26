import pytest
from selenium import webdriver
import urllib3
import warnings
 
def pytest_runtest_makereport(item, call):
  if "incremental" in item.keywords:
    if call.excinfo is not None:
      parent = item.parent
      parent._previousfailed = item
 
def pytest_runtest_setup(item):
  previousfailed = getattr(item.parent, "_previousfailed", None)
  if previousfailed is not None:
    pytest.xfail("previous test failed (%s)" % previousfailed.name)
        
@pytest.fixture(scope="class")
def driver_init(request):
  driver = webdriver.Chrome()
  request.cls.driver = driver
  yield
  driver.close()
  # driver.quit()