from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class ContextMenu_locators:


    var_content_locator = (By.XPATH, "//div[@class='example']")
    var_hotspot_locator = (By.ID,"hot-spot")

    def __init__(self,driver):
        self.driver = driver

    def wait_content_locator(self):
        return WebDriverWait(self.driver,2).until(presence_of_element_located((ContextMenu_locators.var_content_locator)))

    def hot_spot_locator(self):
        return self.driver.find_element(*ContextMenu_locators.var_hotspot_locator)

    def right_click_element(self,element):
        return ActionChains(self.driver).move_to_element(element).context_click().perform()

    def switchto_active_element(self):
        return self.driver.switch_to.active_element

    def window_alert_locator(self):
        return self.driver.switch_to().Alert()

    def click_anywhere(self):
        return ActionChains(self.driver).click().perform()

    def current_window(self):
        return self.driver.current_window_handle

    def switchto_default_window(self):
        return self.driver.switch_to.default_content()



