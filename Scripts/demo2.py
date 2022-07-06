from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/login")
l = [i for i in driver.find_elements_by_xpath("//div/ul/li/a") if i.text.strip() and i.text != "(0)"]
print("*"*150)
for i in l:
    if i.text.lower() in "Apparel & Shoes".lower():
        i.click()
        break
giftcards = driver.find_elements(By.XPATH, "//h2/a")
for i in giftcards:
    print(i.text)
sleep(3)
driver.close()
