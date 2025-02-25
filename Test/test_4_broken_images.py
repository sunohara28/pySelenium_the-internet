from Test.IntDriver import IntDriver
from PageObjects.broken_image_locators import broken_image
from PageObjects.HomePage_Locators import HomePageLocators


class TestMain(IntDriver):


    def test_broken_image_page(self):
        HomePage_elements = HomePageLocators(self.driver)
        HomePage_elements.broken_image_locator().click()

    def test_img_check(self):
        broken_image_element = broken_image(self.driver)

        broken_image_element.wait_img()

        img_list = broken_image_element.img_src_list()

        for x in range(len(img_list)):
            broken_image_element.img_url(img_list[x])
            if len(broken_image_element.broken_img_locators()) > 0:
                print(img_list[x] + " image is borken")

            elif len(broken_image_element.broken_img_locators()) == 0:
                print(img_list[x] + " image is worken")


