import unittest
from testcase import HerokuAppLogin

# get all tests from Login class
login = unittest.TestLoader().loadTestsFromTestCase(HerokuAppLogin)

# create a test suite
test_suite = unittest.TestSuite([login])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)