from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

password = "qwertyuiop00"
driver = webdriver.Chrome(r"C:\Users\VAMSI\Desktop\Selenium\data\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
from locators_utils import _locators

lo = _locators(driver)
driver.get("http://demowebshop.tricentis.com/login")
lo.link_text_("Register").click()
lo.id_("gender-male").click()
lo.id_("FirstName").send_keys("ram")
lo.id_("LastName").send_keys("ram")
email = lo.id_("Email")
# driver.find_element(By.LINK_TEXT, "Register").click()
# driver.find_element(By.ID, "gender-male").click()
# driver.find_element(By.ID, "FirstName").send_keys("ram")
# driver.find_element(By.ID, "LastName").send_keys("ram")
# email = driver.find_element(By.ID, "Email")
email.send_keys("abcd@gmail.com")
lo.id_("Password").send_keys(password)
lo.id_("ConfirmPassword").send_keys(password)
lo.id_("register-button").click()
# driver.find_element(By.ID, "Password").send_keys(password)
# driver.find_element(By.ID, "ConfirmPassword").send_keys(password)
# driver.find_element(By.ID, "register-button").click()
sleep(2)
# for _ in range(6):
#     try:
#         if driver.find_element(By.LINK_TEXT,"The specified email already exists").is_displayed():
#             email.clear()
#             from random import random
#
#             email.send_keys(f"abcd{int(random() * 100)}@gmail.com")
#     except:
#         break
#
# if driver.find_element(By.XPATH, "//input[@value='Continue']").is_displayed():
#     print("Registration done")
# else:
#     print("Registration not done")
driver.close()
