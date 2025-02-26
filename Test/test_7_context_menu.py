import time
from PageObjects.HomePage_Locators import HomePageLocators
from PageObjects.context_menu_locators import ContextMenu_locators
from Test.IntDriver import IntDriver


class TestMain(IntDriver):
    class TestMain(IntDriver):
        def test_homepage(self):
            HomePage_elements = HomePageLocators(self.driver)

            HomePage_elements.click_example(*HomePageLocators.var_context_menu_locator)


        def test_context_menu(self):
            ContextMenu_elements = ContextMenu_locators(self.driver)
            ContextMenu_elements.wait_content_locator()

            ContextMenu_elements.right_click_element(ContextMenu_elements.hot_spot_locator())
            time.sleep(2)

            ContextMenu_elements.switchto_active_element()
            ContextMenu_elements.window_alert_locator().Accept()

            ContextMenu_elements.current_window()
            ContextMenu_elements.click_anywhere()

            time.sleep(2)

