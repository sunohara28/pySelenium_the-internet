import time

from Test.IntDriver import IntDriver
from PageObjects.HomePage_Locators import HomePageLocators

class TestMain(IntDriver):
    def test_abtest(self):
        HomePage_elements = HomePageLocators(self.driver)

        HomePage_elements.abtest_locator().click()
        time.sleep(1)
