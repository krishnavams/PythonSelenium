from timeit import timeit
code = """
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://demowebshop.tricentis.com/")
elements = driver.find_elements(By.XPATH, "//a")
import requests
for ele in elements:
    try:
        response = requests.head(ele.get_attribute("href"))
        if response.status_code > 400:
            print(ele.get_attribute("href"))

    except:
        pass
driver.close()"""
print(timeit(code, ))