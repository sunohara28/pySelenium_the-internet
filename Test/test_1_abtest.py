import time

from Test.IntDriver import IntDriver
from PageObjects.HomePage_Locators import HomePageLocators

class TestMain(IntDriver):
    def test_abtest(self):
        HomePage_elements = HomePageLocators(self.driver)

        HomePage_elements.click_example(*HomePageLocators.var_abtest_locator)

        time.sleep(1)
