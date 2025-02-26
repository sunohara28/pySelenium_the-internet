from Test.IntDriver import IntDriver
from PageObjects.HomePage_Locators import HomePageLocators
from PageObjects.Add_Remove_Locators import AddRemove

class TestMain(IntDriver):

    def test_add_page(self):
        HomePage_elements = HomePageLocators(self.driver)
        HomePage_elements.click_example(*HomePageLocators.var_add_remove_elements_locator)


    def test_add(self):

        add_num = 5

        AddRemove_element = AddRemove(self.driver)
        AddRemove_element.wait_add_locator()

        for x in range(add_num):
            AddRemove_element.Add_locator().click()
            AddRemove_element.wait_del_locator()

        assert len(AddRemove_element.del_locators()) == 5

    def test_del(self):
        AddRemove_element = AddRemove(self.driver)

        for x in AddRemove_element.del_locators():
            x.find_element(*AddRemove_element.var_del_locator).click()

        assert len(AddRemove_element.del_locators()) == 0









