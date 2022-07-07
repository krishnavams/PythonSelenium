from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.get("http://127.0.0.1:5500/Notes/DemoWeb/demo.html")
for i in Select(driver.find_element(By.XPATH, "//select")).options:
    if i.text.lower() in "audi":
        i.click()

Select(driver.find_element(By.XPATH, "//select")).select_by_index(1)
Select(driver.find_element(By.XPATH, "//select")).select_by_value("aud")
Select(driver.find_element(By.XPATH, "//select")).select_by_visible_text("Audi")

sleep(2)
driver.close()

