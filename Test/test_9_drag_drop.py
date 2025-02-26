import time

from PageObjects.HomePage_Locators import HomePageLocators
from PageObjects.DragDrop_locators import DragDrop_Locators
from Test.IntDriver import IntDriver


class TestMain(IntDriver):
    class TestMain(IntDriver):
        def test_homepage(self):
            HomePage_elements = HomePageLocators(self.driver)

            HomePage_elements.click_example(*HomePageLocators.var_drag_and_drop_locator)

        def test_drag_drop(self):
            DragDrop_elements = DragDrop_Locators(self.driver)
            DragDrop_elements.wait_content()

            var_columnA_text = DragDrop_elements.drag_text(*DragDrop_elements.var_columnA_locator)
            var_columnB_text = DragDrop_elements.drop_text(*DragDrop_elements.var_columnB_locator)

            DragDrop_elements.drag_drop(*DragDrop_elements.var_columnA_locator,*DragDrop_elements.var_columnB_locator)

            assert DragDrop_elements.drop_text(*DragDrop_elements.var_columnB_locator) == var_columnA_text
            assert DragDrop_elements.drop_text(*DragDrop_elements.var_columnA_locator) == var_columnB_text
            time.sleep(4)

