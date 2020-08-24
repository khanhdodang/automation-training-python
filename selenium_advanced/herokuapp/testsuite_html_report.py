import unittest
import HTMLTestRunner #pip install html-testRunner
import os
from testcase import HerokuAppLogin

# get the directory path to output report file
dir = os.getcwd()

# get all tests from Login class
login = unittest.TestLoader().loadTestsFromTestCase(HerokuAppLogin)

# create a test suite
test_suite = unittest.TestSuite([login])

# open the report file
outfile = open(dir + "/SeleniumPythonTestSummary.html", "w", encoding='utf-8')

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='Acceptance Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)
outfile.close()
