import requests
from selenium.webdriver import Chrome

driver = Chrome(r"C:\Users\VAMSI\Desktop\Selenium\data\chromedriver.exe")
driver.get("https://www.google.com")
print([i.get_attribute("href") for i in driver.find_elements_by_xpath("//a") if
       200 < requests.head(i.get_attribute("href")).status_code < 400])
driver.close()
