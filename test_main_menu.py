import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_main_page(driver):
    main_page = driver.find_element(By.LINK_TEXT, 'Главная')
    main_page.click()

    phone_number = driver.find_element(By.CSS_SELECTOR, '[class="header-phone"]')
    phone_number_check = phone_number.text

    email = driver.find_element(By.CSS_SELECTOR, '[class="header-mail"]')
    email_check = email.text

    assert phone_number_check == '8 (342) 206-06-57'
    assert email_check == 'info@v8ru.ru'

def test_my_orders(driver):
    my_orders = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#my-menu > li.menuItem.personal_cabinet > a')))
    my_orders.click()

    header = driver.find_element(By.CSS_SELECTOR, '.contentHeader')
    header_check = header.text
    assert header_check == 'Личный кабинет'

def test_cart(driver):
    cart_page = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="my-menu"]/li[3]/a')))
    cart_page.click()

    check_text = driver.find_element(By.CSS_SELECTOR, 'h1.cartTitle')
    check_cart = check_text.text
    assert check_cart == 'Ваша корзина'


