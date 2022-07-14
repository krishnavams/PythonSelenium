from time import sleep
# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# driver = webdriver.Edge(EdgeChromiumDriverManager().install())
# driver.get(r"C:\Users\VAMSI\Desktop\Selenium\Notes\DemoWeb\loading.html")
# driver.maximize_window()
# f_text = driver.find_element(By.NAME, "fname")
# sleep(5)
# f_text.send_keys("WELCOME")
# sleep(5)
# driver.close()
#
#
# # implicitly_wait
# driver = webdriver.Edge(EdgeChromiumDriverManager().install())
# driver.get(r"C:\Users\VAMSI\Desktop\Selenium\Notes\DemoWeb\loading.html")
# driver.maximize_window()
# driver.implicitly_wait(10)
# f_text = driver.find_element(By.NAME, "fname")
# f_text.send_keys("WELCOME")
# driver.close()

# WebdriverWait
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.get(r"C:\Users\VAMSI\Desktop\Selenium\Notes\DemoWeb\loading.html")
wait = WebDriverWait(driver, 20)
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
wait.until(visibility_of_element_located(("name", "fname")))
f_text = driver.find_element(By.NAME, "fname")
f_text.send_keys("WELCOME")
sleep(5)
driver.close()
