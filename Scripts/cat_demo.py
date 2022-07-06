from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://demowebshop.tricentis.com/")
Categories = driver.find_elements(By.XPATH, "//strong[text()='Categories']/../..//ul/li/a")
try:
    for i in Categories:
        i.click()
        product_item = driver.find_elements(By.XPATH, "//div[@class='product-item']//h2/a")
        for l in product_item:
            print(l.text)
except Exception as e:
    print(e)