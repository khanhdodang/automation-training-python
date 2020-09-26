import sys
sys.path.append(".")
import pytest
from Pages.login_page import LoginPage
from Pages.result_page import ResultPage
from TestData.TestData import TestData
from Objects.account import Account

@pytest.mark.usefixtures("driver_init")
class Test_Login():

  def test_login_successfully1(self):
    login_page = LoginPage(self.driver)
    assert login_page.is_title_matches()
    login_page.login(TestData.USERNAME, TestData.PASSWORD)
    result_page = ResultPage(self.driver)

    print(result_page.get_message())
    assert "You logged into a secure area!" in result_page.get_message()

  def test_login_successfully2(self):
    login_page = LoginPage(self.driver)
    assert login_page.is_title_matches()

    account = Account(TestData.USERNAME, TestData.PASSWORD)
    login_page.login_object(account)
    result_page = ResultPage(self.driver)

    print(result_page.get_message())
    assert "You logged into a secure area!" in result_page.get_message()

  def test_login_with_invalid_username(self):
    login_page = LoginPage(self.driver)
    login_page.login(TestData.FAKE_USERNAME, TestData.PASSWORD)
    result_page = ResultPage(self.driver)

    print(result_page.get_message())
    assert "Your username is invalid!" in result_page.get_message()

  def test_login_with_invalid_password(self):
    login_page = LoginPage(self.driver)
    login_page.login(TestData.USERNAME, TestData.FAKE_PASSWORD)
    result_page = ResultPage(self.driver)

    print(result_page.get_message())
    assert "Your password is invalid!" in result_page.get_message()

  @pytest.mark.skip(reason="I want to skip this test")
  def test_login_with_invalid_username_password(self):
    login_page = LoginPage(self.driver)
    login_page.login(TestData.FAKE_USERNAME, TestData.FAKE_PASSWORD)
    result_page = ResultPage(self.driver)

    print(result_page.get_message())
    assert "Your password is invalid!" in result_page.get_message()
