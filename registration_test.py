import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "https://v8ru.ru"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    button_reg = browser.find_element(By.CSS_SELECTOR, "[class='logRegLink']")
    button_reg.click()

    field_first_name = browser.find_element(By.ID, "fname")
    field_first_name.send_keys("Иван")

    field_phone_number = browser.find_element(By.CSS_SELECTOR, "[placeholder='+7 (900) 000-00-00']")
    field_phone_number.send_keys("  (900) 000-00-00")

    field_email = browser.find_element(By.ID, "email")
    field_email.send_keys("ivan_1998@gmail.com")

    field_password = browser.find_element(By.CSS_SELECTOR, "[name='password']")
    field_password.send_keys("12345678!Ab")

    field_password_confirm = browser.find_element(By.CSS_SELECTOR, "[name='password_confirm']")
    field_password_confirm.send_keys("12345678!Ab")


finally:
    time.sleep(8)
    browser.quit()

