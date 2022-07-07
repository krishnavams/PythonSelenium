from selenium.webdriver.common.by import By


class SignInPage:
    def __init__(self, driver):
        self.driver = driver

    def login_name(self):
        return self.driver.find_element(By.ID, "userName")

    def password(self):
        return self.driver.find_element(By.ID, "passWord")

    def sign_in(self):
        return self.driver.find_element(By.XPATH, "//input[@title='Sign In']")

    def logo(self):
        return self.driver.find_element(By.XPATH, "//img[@title='Zoho CRM']")


