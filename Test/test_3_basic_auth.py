import time

from Test.IntDriver import IntDriver
from PageObjects.HomePage_Locators import HomePageLocators
from PageObjects.Basic_Auth_Locators import Basic_Auth_Locators

class TestMain(IntDriver):

    def test_basic_auth_page(self):
        HomePage_elements = HomePageLocators(self.driver)

        HomePage_elements.basic_auth_locator().click()

        time.sleep(2)

    def test_pop_up_login(self):
        basic_auth_element = Basic_Auth_Locators(self.driver)

        basic_auth_element.login_url()
        basic_auth_element.wait_loggedin_text()
        assert basic_auth_element.loggedin_text() == "Congratulations! You must have the proper credentials."


