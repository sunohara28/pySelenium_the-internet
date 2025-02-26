from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class Checkbox:

    var_form_locator = (By.ID,"checkboxes")
    var_checkbox_locator = (By.XPATH, "//input[@type='checkbox']")

    def __init__(self,driver):
        self.driver = driver

    def wait_form(self):
        WebDriverWait(self.driver,2).until(presence_of_element_located((Checkbox.var_form_locator)))

    def form_locator(self):
        return self.driver.find_element(*Checkbox.var_form_locator)

    def checkboxes_locator(self):
        return self.driver.find_elements(*Checkbox.var_checkbox_locator)

    def checkboxes_locator_len(self):
        return len(Checkbox.checkboxes_locator(self))

    def checkbox_locator(self,index):
        return self.driver.find_element(By.XPATH, f"//input[@type='checkbox'][{index}]")