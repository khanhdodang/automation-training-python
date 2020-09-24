import os
import sys

sys.path.append(".")
import unittest
from HTMLTestRunner import *
from unittestpackage.test_class1 import TestClass1
from unittestpackage.test_class2 import TestClass2

# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# get the directory path to output report file
dir = os.getcwd()

# Create a test suite combining TestClass1 and TestClass2
smokeTests = unittest.TestSuite([tc1, tc2])

# open the report file
outfile = open(dir + "/Report.html", "w", encoding='utf-8')

# configure HTMLTestRunner options
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Acceptance Tests')

# run the suite using HTMLTestRunner
runner.run(smokeTests)
outfile.close()