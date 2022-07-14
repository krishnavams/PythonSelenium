from selenium.webdriver.common.by import By


class projects_jira:
    def __init__(self, driver):
        self.driver = driver

    def get_create(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Create']/..")
