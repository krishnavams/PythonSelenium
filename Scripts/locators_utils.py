from selenium.webdriver.common.by import By


class _locators:
    def __init__(self, driver):
        self.driver = driver

    def xpath_(self, path):
        return self.driver.find_element(By.XPATH, path)

    def link_text_(self, path):
        return self.driver.find_element(By.LINK_TEXT, path)

    def id_(self, path):
        return self.driver.find_element(By.ID, path)

    def class_name(self, path):
        return self.driver.find_element(By.CLASS_NAME, path)

    def css_selector_(self, path):
        return self.driver.find_element(By.CSS_SELECTOR, path)

    def name_(self, path):
        return self.driver.find_element(By.NAME, path)

    def tag_name(self, path):
        return self.driver.find_element(By.TAG_NAME, path)

    def partial_link_text(self, path):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, path)
