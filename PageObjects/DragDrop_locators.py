from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class DragDrop_Locators:

    var_content_locator = (By.ID,"content")
    var_columnA_locator = (By.ID,"column-a")
    var_columnB_locator = (By.ID, "column-b")

    def __init__(self,driver):
        self.driver = driver

    def wait_content(self):
        return WebDriverWait(self.driver,2).until(presence_of_element_located((DragDrop_Locators.var_content_locator)))

    def drag_drop(self,dra,g,dro,p):
        return ActionChains(self.driver).drag_and_drop(self.driver.find_element(dra,g),self.driver.find_element(dro,p)).perform()

    def drag_text(self,dr,ag):
        return self.driver.find_element(dr,ag).text

    def drop_text(self,dr,op):
        return self.driver.find_element(dr,op).text

