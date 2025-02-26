
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class DisappearningElements_locators:


    var_content_locator = (By.ID, "content")
    var_home_locator = (By.LINK_TEXT,"Home")
    var_about_locator = (By.LINK_TEXT, "About")
    var_contactus_locator = (By.LINK_TEXT, "Contact Us")
    var_portfolio_locator = (By.LINK_TEXT, "Portfolio")
    var_gallery_locator = (By.LINK_TEXT, "Gallery")


    def __init__(self,driver):
        self.driver = driver

    def wait_content(self):
        return WebDriverWait(self.driver,2).until(presence_of_element_located((DisappearningElements_locators.var_content_locator)))

    def go_back(self):
        return self.driver.back()

    def click_menu(self,a,b):
        return self.driver.find_element(a,b).click()
