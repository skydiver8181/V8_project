from selenium import webdriver
from selenium.webdriver.common.by import By

def add_to_cart():
    try:
        link = "https://v8ru.ru"
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(link)
        browser.add_cookie({'name': 'ABCPUser', 'value': 'ivan273681%40gmail.com-----e10adc3949ba59abbe56e057f20f883e'})
        browser.get(link)

        search = browser.find_element(By.ID, "pcode")
        search.send_keys("CUK2939")

        search_button = browser.find_element(By.CSS_SELECTOR, "[class='fr-icon3-search']")
        search_button.click()

        add_to_cart = browser.find_element(By.CSS_SELECTOR, "[class='j-confirm-button fr-btn fr-btn-success articleButtonsBigRedButton']")
        add_to_cart.click()

        button_cart = browser.find_element(By.CSS_SELECTOR, "[class='cartTitle']")
        button_cart.click()

        quantity_value = browser.find_element(By.CSS_SELECTOR, "[class='j-quantity-input quantityInput']")
        quantity = quantity_value.get_attribute("value")

        assert quantity != 0, "The item didn't add to the cart"


    finally:
        browser.quit()

def test_add_to_cart():
    add_to_cart()


