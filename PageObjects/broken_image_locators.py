from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

class broken_image:

    var_img_src = (By.XPATH,"//div/img")

    def __init__(self,driver):
        self.driver = driver

    def wait_img(self):
        return WebDriverWait(self.driver,2).until(presence_of_element_located((broken_image.var_img_src)))

    def img_src_locators(self):
        return self.driver.find_elements(*broken_image.var_img_src)

    def broken_img_locators(self):
        return self.driver.find_elements(By.XPATH, "//h1[contains(text(),'Not Found')]")

    def img_src_list(self):
        img_list = []
        for x in self.driver.find_elements(*broken_image.var_img_src):
            img_list.append(x.get_attribute("src"))
        return img_list

    def img_url(self,img_src):
        return self.driver.get(img_src)





