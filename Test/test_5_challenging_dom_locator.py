import pytest

from Test.IntDriver import IntDriver
from PageObjects.HomePage_Locators import HomePageLocators
from PageObjects.challenging_dom_locators import ChallengingDom

class TestMain(IntDriver):
    def test_homepage(self):
        HomePage_elements = HomePageLocators(self.driver)

        HomePage_elements.click_example(*HomePageLocators.var_challenging_dom_locator)


    def test_chall_dom(self):
        ChallengingDom_elements = ChallengingDom(self.driver)
        ChallengingDom_elements.wait_table()

        temp_dict = {}
        data_dict = []

        r_index = 0
        for a in range(ChallengingDom_elements.row_len()):
            c_index = 0
            r_index = r_index + 1
            for c in range(ChallengingDom_elements.column_len()):
                c_index = c_index + 1
                temp_dict[ChallengingDom_elements.column_header(c_index)] = ChallengingDom_elements.row_data(r_index,c_index)
            data_dict.append(temp_dict.copy())

        print(data_dict)

