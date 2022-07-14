from time import sleep

import Scripts.JIRA.POM.loginPage


def logger():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    from Scripts.JIRA.GENARIC.BasicData import URL, password, username
    driver.get(URL)
    from Scripts.JIRA.POM.loginPage import LoginPage
    driver.implicitly_wait(10)
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.get_username().send_keys(username)
    sleep(2)
    login_page.get_continue().click()
    sleep(2)
    login_page.get_password().send_keys(password)
    sleep(2)
    login_page.get_login().click()
    sleep(2)
    print("passed")



logger()
