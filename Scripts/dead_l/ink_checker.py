from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime


def outer(func):
    def inner():
        start = datetime.now()
        func()
        end = datetime.now()
        return end - start
    return inner


@outer
def link_tester():
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
    driver.close()

    print(link_tester())

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://demowebshop.tricentis.com/")
elements = driver.find_elements(By.XPATH, "//a")
import requests
for ele in elements:
    try:
        response = requests.head(ele.get_attribute("href"))
        if response.status_code > 200:
            print(ele.get_attribute("href"))

    except:
        pass
driver.close()