from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class ChallengingDom:

    var_table_locator = (By.XPATH,"//table")
    var_column_head_locator = (By.XPATH, "//table/thead/tr/th")
    var_row_locator = (By.XPATH,"//tbody/tr")

    def __init__(self,driver):
        self.driver = driver

    def wait_table(self):
        return WebDriverWait(self.driver,2).until(presence_of_element_located((ChallengingDom.var_table_locator)))

    def column_len(self):
        return len(self.driver.find_elements(*ChallengingDom.var_column_head_locator))

    def row_len(self):
        return len(self.driver.find_elements(*ChallengingDom.var_row_locator))

    def column_header(self,c_index):
        column_header = self.driver.find_element(By.XPATH,f"//table/thead/tr/th[{c_index}]").text
        return column_header

    def row_data(self,r_index,c_index):
        row_data = self.driver.find_element(By.XPATH,f"//tbody/tr[{r_index}]/td[{c_index}]").text
        return row_data



