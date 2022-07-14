from selenium import webdriver


# from webdriver_manager.chrome import ChromeDriverManager


def test_case_no_1():
    driver = webdriver.Chrome(r"C:\Users\VAMSI\Desktop\Selenium\data\chromedriver.exe")
    from Scripts.Zoho_CRM.data.TestData import password as pw, username as ur, url as ul
    global ul, ur, pw
    driver.get(ul)
    driver.maximize_window()
    driver.implicitly_wait(5)
    from Scripts.Zoho_CRM.WebElement_Repos.Sign_in_page import SignInPage
    signpage = SignInPage(driver)
    assert signpage.logo().is_displayed() == True
    assert signpage.logo().is_enabled() == True
    assert signpage.login_name().is_displayed() == True
    assert signpage.login_name().is_enabled() == True
    assert signpage.password().is_displayed() == True
    assert signpage.password().is_enabled() == True
    signpage.login_name().send_keys(ur)  # valid username
    signpage.password().send_keys(pw)  # valid password
    signpage.sign_in().click()
    assert driver.title in "Zoho CRM - Home Page"
    driver.close()


def test_case_no_2():
    driver = webdriver.Chrome(r"C:\Users\VAMSI\Desktop\Selenium\data\chromedriver.exe")
    from Scripts.Zoho_CRM.data.TestData import password as pw, username as ur, url as ul
    global ul, ur, pw
    driver.get(ul)
    driver.maximize_window()
    driver.implicitly_wait(5)
    from Scripts.Zoho_CRM.WebElement_Repos.Sign_in_page import SignInPage
    signpage = SignInPage(driver)
    assert signpage.logo().is_displayed() == True
    assert signpage.logo().is_enabled() == True
    assert signpage.login_name().is_displayed() == True
    assert signpage.login_name().is_enabled() == True
    assert signpage.password().is_displayed() == True
    assert signpage.password().is_enabled() == True
    signpage.login_name().send_keys(ur + "123")  # invalid username
    signpage.password().send_keys(pw)  # valid password
    signpage.sign_in().click()
    assert driver.title in "Zoho CRM - Home Page"
    driver.close()


def test_case_no_3():
    driver = webdriver.Chrome(r"C:\Users\VAMSI\Desktop\Selenium\data\chromedriver.exe")
    from Scripts.Zoho_CRM.data.TestData import password as pw, username as ur, url as ul
    global ul, ur, pw
    driver.get(ul)
    driver.maximize_window()
    driver.implicitly_wait(5)
    from Scripts.Zoho_CRM.WebElement_Repos.Sign_in_page import SignInPage
    signpage = SignInPage(driver)
    assert signpage.logo().is_displayed() == True
    assert signpage.logo().is_enabled() == True
    assert signpage.login_name().is_displayed() == True
    assert signpage.login_name().is_enabled() == True
    assert signpage.password().is_displayed() == True
    assert signpage.password().is_enabled() == True
    signpage.login_name().send_keys(ur)  # valid username
    signpage.password().send_keys(pw + "25")  # invalid password
    signpage.sign_in().click()
    assert driver.title in "Zoho CRM - Home Page"
    driver.close()


try:
    test_case_no_1()

except:
    print("test case 1 failed")
try:
    test_case_no_2()
except:
    print("test case 2 passed")
try:
    test_case_no_3()
except:
    print("test case 3 passed")
