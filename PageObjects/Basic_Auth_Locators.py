from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


class Basic_Auth_Locators:

    username = "admin"
    password = "admin"
    Login_URL = "https://" + username + ":" + password + "@the-internet.herokuapp.com/basic_auth"

    loggedin_text_locator = (By.XPATH,"//p[contains(text(),'Congratulations! You must have the proper credentials.')]")

    def __init__(self,driver):
        self.driver = driver

    def login_url(self):
        return self.driver.get(Basic_Auth_Locators.Login_URL)

    def wait_loggedin_text(self):
        return WebDriverWait(self.driver, 2).until(element_to_be_clickable((Basic_Auth_Locators.loggedin_text_locator)))

    def loggedin_text(self):
        return self.driver.find_element(*Basic_Auth_Locators.loggedin_text_locator).text


