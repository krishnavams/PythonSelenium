from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import *

driver = webdriver.Edge(EdgeChromiumDriverManager().install())

driver.get("https://www.goibibo.com/")
driver.implicitly_wait(10)
driver.maximize_window()
year = 2023
month = "April"
day = 20

driver.find_element(By.XPATH, "//span[text()='Departure']").click()
while True:
    try:
        driver.find_element(By.XPATH, f"//div[text()='{month} {year}']/../..//p[text()='{day}']").click()
        break
    except NoSuchElementException:
        driver.find_element(By.XPATH, "//span[@aria-label='Next Month']").click()

driver.find_element(By.XPATH, "//span[text()='Done']").click()
