from selenium.webdriver.common.by import By


class StartPage:

    def __init__(self, driver):
        self.driver = driver

    def get_jira_software(self):
        return self.driver.find_element(By.LINK_TEXT, "Jira Software")

