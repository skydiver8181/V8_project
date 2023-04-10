from selenium import webdriver
from selenium.webdriver.common.by import By

def login():
    try:
        link = "https://v8ru.ru/"
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(link)

        login = browser.find_element(By.ID, "logInModal")
        login.click()

        enter_login = browser.find_element(By.ID, "login_modal")
        enter_login.send_keys("ivan273681@gmail.com")

        enter_password = browser.find_element(By.ID, "pass_modal")
        enter_password.send_keys("123456")

        button_enter = browser.find_element(By.ID, "go_modal")
        button_enter.click()

        user_name_value = browser.find_element(By.CSS_SELECTOR, "[class='clientName']")
        user_name = user_name_value.get_attribute("value")

        assert user_name != "Вход", "Login function works incorrect"


    finally:
        browser.quit()

def test_login():
    login()

