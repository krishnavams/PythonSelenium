from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# d = webdriver.Chrome(ChromeDriverManager().install())
# d.get(r"C:\Users\VAMSI\Desktop\Selenium\Notes\DemoWeb\iframe.html")
# d.implicitly_wait(10)
# d.maximize_window()

# # act = ActionChains(d)
# d.switch_to.frame(d.find_element(By.NAME, "frame1"))
# d.find_element(By.LINK_TEXT, "Register").click()
# d.switch_to.default_content()
# d.switch_to.frame("frame2")
# d.find_element(By.ID, "search_form").send_keys("abcd")
# d.close()

# d.find_element(By.LINK_TEXT, "Register").send_keys(Keys.RETURN)

d = webdriver.Chrome(ChromeDriverManager().install())
d.get(r"http://127.0.0.1:5500/Notes/DemoWeb/drag.html")
d.implicitly_wait(10)
d.maximize_window()
act = ActionChains(d)
act.drag_and_drop(d.find_element(By.CLASS_NAME, "imgBox"), d.find_element(By.XPATH, "//div[4]")).perform()
# d.switch_to.alert.accept()


