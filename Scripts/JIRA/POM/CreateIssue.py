from selenium.webdriver.common.by import By


class create_issue:
    def __init__(self, driver):
        self.driver = driver

    def get_Issue_type(self):
        return self.driver.find_element(By.XPATH, "//label[text()='Issue type']/..//div")

    def get_bug(self):
        return self.driver.find_element(By.XPATH, "//div[text()='Bug']/..")

    def get_summary(self):
        return self.driver.find_element(By.XPATH, "//label[text()='Summary']/..//input")

    def get_label(self):
        return self.driver.find_element(By.XPATH, "//label[text()='Labels']/..//div[text()='Select label']/../..")

    def get_sprint(self):
            return self.driver.find_element(By.XPATH, "//label[text()='Sprint']/..//div[text()='Select sprint']/../..")
