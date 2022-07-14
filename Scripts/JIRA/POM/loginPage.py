from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_username(self):
        return self.driver.find_element(By.ID, "username")

    def get_password(self):
        return self.driver.find_element(By.ID, "password")

    def get_continue(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Continue']/../..")

    def get_login(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Log in']/../..")

