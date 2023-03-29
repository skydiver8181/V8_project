import time
from selenium import webdriver
from selenium.webdriver.common.by import By

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

finally:
    time.sleep(3)
    browser.quit()

