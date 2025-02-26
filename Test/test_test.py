import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.Add_Remove_Locators import AddRemove

def test_eeh():

    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com")
    driver.maximize_window()
    driver.implicitly_wait(10)

    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Disappearing Elements").click()

    driver.find_element(By.LINK_TEXT,"Home").click()
    time.sleep(1)
    driver.back()

    driver.find_element(By.LINK_TEXT, "About").click()
    time.sleep(1)
    driver.back()

    driver.find_element(By.LINK_TEXT, "Contact Us").click()
    time.sleep(1)
    driver.back()

    driver.find_element(By.LINK_TEXT, "Portfolio").click()
    time.sleep(1)
    driver.back()


    time.sleep(2)