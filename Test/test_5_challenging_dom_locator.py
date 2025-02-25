import pytest

from Test.IntDriver import IntDriver
from PageObjects.HomePage_Locators import HomePageLocators
from PageObjects.challenging_dom_locators import ChallengingDom

class TestMain(IntDriver):
    def test_homepage(self):
        HomePage_elements = HomePageLocators(self.driver)

        HomePage_elements.challenging_dom_locator().click()

    def test_chall_dom(self):
        ChallengingDom_elements = ChallengingDom(self.driver)
        ChallengingDom_elements.wait_table()

        temp_dict = {}
        data_dict = []

        r_index = 0
        for a in range(10):
            c_index = 0
            r_index = r_index + 1
            for c in range(7):
                c_index = c_index + 1
                temp_dict[ChallengingDom_elements.column_header(c_index)] = ChallengingDom_elements.row_data(c_index,r_index)
            data_dict.append(temp_dict.copy())

        print(data_dict)

