import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.Add_Remove_Locators import AddRemove

def test_test():

    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, "//a[@href='/challenging_dom']").click()

    WebDriverWait(driver,2).until(presence_of_element_located((By.XPATH,"//table")))

    data_dict=[]
    temp_dict={}

    column_head = driver.find_elements(By.XPATH,"//table/thead/tr/th")
    column_head_len = len(column_head)

    rows = driver.find_elements(By.XPATH,"//tbody/tr")
    rows_len = len(rows)

    rows_data = driver.find_elements(By.XPATH,"//tbody/tr/td")
    rows_data_len = len(rows_data)

    w = 0
    for z in range(rows_len):
        q = 0
        w = w + 1
        for x in range(column_head_len):
            q = q + 1
            temp_dict[driver.find_element(By.XPATH,f"//table/thead/tr/th[{q}]").text] = driver.find_element(By.XPATH,f"//tbody/tr[{w}]/td[{q}]").text
        data_dict.append(temp_dict.copy())


    print(column_head_len)
    print(rows_len)
    print(rows_data_len)

    print(data_dict)



    time.sleep(2)

