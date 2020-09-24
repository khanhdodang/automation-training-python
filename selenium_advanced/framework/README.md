# Python automation testing basics
##UI testing with Python and Selenium Webdriver
Understanding the basics with data driven UI testing with Python, [Selenium](https://pypi.python.org/pypi/selenium) &amp; [nose](https://nose.readthedocs.org/en/latest/) / [unittest](https://docs.python.org/2/library/unittest.html).

Note: '[nose](https://nose.readthedocs.org/en/latest/)' is used only for standalone execution. As I use PyCharm with '[pydev](https://www.jetbrains.com/pycharm/help/remote-debugging.html)' support for debugging and '[unittest](https://docs.python.org/2/library/unittest.html)' module for running the tests, I am actually not using it.

For DDT (Data driven testing) you have to install '[ddt](https://ddt.readthedocs.org/en/latest/index.html)', '[xlrd](http://www.python-excel.org/)' or use *csv*

## Automated tests framework - unittest
A test case is created by subclassing `unittest.TestCase`. The individual tests are defined with methods whose names start with the letters `test`. This naming convention informs the test runner about which methods represent tests. (see *ui_test_basics.py*)
The `setUp()` and `tearDown()` methods allow you to define instructions that will be executed before and after each test method (used in *ui_test_basics5.py*).

## Other Automated tests
Files *ui_test_basics2.py*, *ui_test_basics3.py* and *ui_test_basics4.py* are basic .py scripts demonstrating the ability to build the automated test framework with Selenium Webdriver and Python. All except *ui_test_basics4.py* (Safari) and *ui_test_basics5* (Chrome) are using Firefox browser.
As Selenium Webdriver is native written for use with Firefox, so for other browser support there is need to install additional drivers (as described below).


##Using Chrome
Before you run a python file *ui_test_basics5.py* it is good to read 'Chromedriver - Getting Started (https://sites.google.com/a/chromium.org/chromedriver/getting-started)' to find out how to configure the script to get chromedriver executable to work (best choice for MAC OS X is to download it to /usr/bin) and setup the PATH so you don't get any kind of error).

##Page object pattern script
In *PO_template_script* directory you can find a template script using page object pattern.

    test_case_script.py
     +-- page.py
      +-- element.py
      +-- locators.py

This approach is well-known as Page Objects Model (POM) as well. For further information and explanation how and why, please read carefully: [Page Objects in Python](https://pragprog.com/magazines/2010-08/page-objects-in-python)

### *Screenshot* functionality
In *ui_test_basics5.py* you will find the usage of "take screenshot on error" in the `test_2_search_by_name` test case. Another solution used in `tearDown()` method:

    import sys, unittest
    from datetime import datetime

    class TestCase(unittest.TestCase):

        def setUp(self):
            some_code

        def test_case(self):
            test case comes here

        def tearDown(self):
            if sys.exc_info()[0]:  # Returns the info of exception being handled
                fail_url = self.driver.current_url
                print fail_url
                now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
                self.driver.get_screenshot_as_file('/path/to/file/%s.png' % now) # my tests work in parallel, so I need uniqe file names
                fail_screenshot_url = 'http://debugtool/screenshots/%s.png' % now
                print fail_screenshot_url
            self.driver.quit()

### HTML report
HTMLTestRunner is an extension to the Python standard library's unittest module. It generates easy to use HTML test reports.
See *test_HTMLTestRunner.py* for test and demo of *HTMLTestRunner.py*
More about HTMLTestRunner: [http://tungwaiyip.info/software/HTMLTestRunner.html](http://tungwaiyip.info/software/HTMLTestRunner.html)

### Data driven testing
Example of *xlrd* impementation - *DDT/xlrd_example.py*

