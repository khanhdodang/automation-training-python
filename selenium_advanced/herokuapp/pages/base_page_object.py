from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

  # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).click()
    
    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text_equal(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

     # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text_contains(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text in element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        return element.send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self,by_locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

