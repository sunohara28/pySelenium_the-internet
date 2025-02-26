import time
from PageObjects.HomePage_Locators import HomePageLocators
from PageObjects.disappearing_elements_locators import DisappearningElements_locators
from Test.IntDriver import IntDriver


class TestMain(IntDriver):
    class TestMain(IntDriver):
        def test_homepage(self):
            HomePage_elements = HomePageLocators(self.driver)

            HomePage_elements.click_example(*HomePageLocators.var_disappearing_elements_locator)


        def test_dissappearing_menu(self):
            DisappearningElements = DisappearningElements_locators(self.driver)
            DisappearningElements.wait_content()

            DisappearningElements.click_menu(*DisappearningElements.var_home_locator)
            DisappearningElements.go_back()
            DisappearningElements.wait_content()

            DisappearningElements.click_menu(*DisappearningElements.var_about_locator)
            DisappearningElements.go_back()
            DisappearningElements.wait_content()

            DisappearningElements.click_menu(*DisappearningElements.var_contactus_locator)
            DisappearningElements.go_back()
            DisappearningElements.wait_content()

            DisappearningElements.click_menu(*DisappearningElements.var_gallery_locator)
            DisappearningElements.go_back()
            DisappearningElements.wait_content()

            DisappearningElements.click_menu(*DisappearningElements.var_portfolio_locator)
            DisappearningElements.go_back()
            DisappearningElements.wait_content()