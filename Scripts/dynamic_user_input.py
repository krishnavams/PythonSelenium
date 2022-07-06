from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.worldometers.info/coronavirus/")
# //table[@id='main_table_countries_today']
# //tr/td/a
from re import findall
countries = [i.text for i in driver.find_elements(By.XPATH, "//table[@id='main_table_countries_today'] //tr/td/a") if not "".join(findall("\d+", i.text)).isdigit()]

# population = [int("".join(findall("\d+", i.text))) for i in driver.find_elements(By.XPATH,
# "//table[@id='main_table_countries_today'] //tr/td[contains(@style,'font-weight: bold; text-align:right')]/a")]
co_po = {i:int("".join(findall("\d+", driver.find_element(By.XPATH, "//a[text()='"+i+"']/../..//td[contains(@style,'font-weight: bold; text-align:right')]/a ").text))) for i in countries if i not in ("Israel", "New Zealand", "Qatar", "China", "Diamond Princess", "MS Zaandam", "Brunei")}
# co_po = {key: value for key, value in zip(countries,population)}
# co_po = dict(zip(countries, population))
print(sorted(co_po.items(), key=lambda item:item[-1], reverse=True))
# print(sum(list(map(lambda item: item[-1], co_po.items()))))
# print((list(filter(lambda item: item[-1] > 100000000, co_po.items()))))
# print(co_po)
driver.close()