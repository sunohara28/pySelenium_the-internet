import time

import pytest

from PageObjects.HomePage_Locators import HomePageLocators
from PageObjects.checkbox_locators import Checkbox
from Test.IntDriver import IntDriver


class TestMain(IntDriver):
    class TestMain(IntDriver):
        def test_homepage(self):
            HomePage_elements = HomePageLocators(self.driver)

            HomePage_elements.click_example(*HomePageLocators.var_checkboxes_locator)


        def test_Checkbox_checked(self):
            Checkbox_elements = Checkbox(self.driver)
            Checkbox_elements.wait_form()

            index = 0
            for x in range(Checkbox_elements.checkboxes_locator_len()):
                index = index + 1
                print(Checkbox_elements.checkbox_locator(index).is_selected())
                if  Checkbox_elements.checkbox_locator(index).is_selected() == False:
                    Checkbox_elements.checkbox_locator(index).click()
                time.sleep(1)

            ass_index = 0
            for x in range(Checkbox_elements.checkboxes_locator_len()):
                ass_index = ass_index + 1
                assert Checkbox_elements.checkbox_locator(ass_index).is_selected() == True


        def test_Checkbox_unchecked(self):
            Checkbox_elements = Checkbox(self.driver)

            index = 0
            for x in range(Checkbox_elements.checkboxes_locator_len()):
                index = index + 1
                print(Checkbox_elements.checkbox_locator(index).is_selected())
                if Checkbox_elements.checkbox_locator(index).is_selected() == True:
                    Checkbox_elements.checkbox_locator(index).click()
                time.sleep(1)

            ass_index = 0
            for x in range(Checkbox_elements.checkboxes_locator_len()):
                ass_index = ass_index + 1
                assert Checkbox_elements.checkbox_locator(ass_index).is_selected() == False




