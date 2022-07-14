from selenium import webdriver
from requests import request
from time import sleep

driver = webdriver.Chrome("./chromedriver")
driver.get("file:///Users/sandeep/Desktop/demo-html/links.html")
sleep(5)

# Find all the links on the webpage and also get the url to which each link is pointing to (value of "href")
element_links = driver.find_elements_by_xpath("//a")

links = [ ]
for element in element_links:
    links.append(element.get_attribute("href"))

# for each link, get the HTTP response.
for link in links:
    print(f'sending request to the link {link}')
    response = request("GET", url=link)
    try:
        assert response.status_code == 200
    except AssertionError:
        print(f"********* The link {link} is broken *****************")
