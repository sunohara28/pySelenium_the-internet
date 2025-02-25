from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


class AddRemove:

    var_add_locator = (By.XPATH,"//button[@onclick='addElement()']")
    var_del_locator = (By.XPATH,"//button[@onclick='deleteElement()']")

    def __init__(self,driver):
        self.driver = driver

    def wait_add_locator(self):
        return WebDriverWait(self.driver, 2).until(element_to_be_clickable((AddRemove.var_add_locator)))

    def wait_del_locator(self):
        return WebDriverWait(self.driver, 2).until(element_to_be_clickable((AddRemove.var_del_locator)))

    def Add_locator(self):
        return self.driver.find_element(*AddRemove.var_add_locator)

    def del_locators(self):
        return self.driver.find_elements(*AddRemove.var_del_locator)


