from time import sleep
from collections import defaultdict
from re import findall

from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
opt = webdriver.ChromeOptions()
opt.headless
driver = webdriver.Chrome(executable_path=r"C:\Users\VAMSI\Downloads\chromedriver_win32 (2)\chromedriver.exe", chrome_options=opt)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.bseindia.com/index.html")
act = ActionChains(driver)
# act.click(driver.find_element(By.XPATH, "//td[@class='tdcolumn rightalign']/a"))
driver.get(driver.find_element(By.XPATH, "//td[@class='tdcolumn rightalign']/a").get_attribute("href"))
Names = [item.text for item in driver.find_elements(By.XPATH, "//td[text()='Market Cap/Broad- Real Time']/../../..//a")]
prices = defaultdict(list)
for name in Names:
    prices[name] += [float("".join(findall(r"[\d/.]", i.text))) for i in driver.find_elements(By.XPATH, f"//a[text()='{name}']/../../td[contains(@class,'text-right')]")]

print(prices)
# sleep(5)
print(driver.title)
driver.close()