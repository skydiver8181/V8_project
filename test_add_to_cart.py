from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_cart(driver):
    search = driver.find_element(By.ID, "pcode")
    search.send_keys("CUK2939")

    search_button = driver.find_element(By.CSS_SELECTOR, "[class='fr-icon3-search']")
    search_button.click()

    add_item_to_cart = driver.find_element(By.CSS_SELECTOR, "[class='j-confirm-button fr-btn fr-btn-success articleButtonsBigRedButton']")
    add_item_to_cart.click()

    if EC.text_to_be_present_in_element(By.ID, "Такой товар уже есть в корзине в количестве 1 штук. Добавить?"):
        check_condition = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ui-dialog-buttonset :nth-child(2)")))
        check_condition.click()

    button_cart = driver.find_element(By.CSS_SELECTOR, "[class='cartTitle']")
    button_cart.click()

    quantity_value = driver.find_element(By.CSS_SELECTOR, "[class='j-quantity-input quantityInput']")
    quantity = quantity_value.get_attribute("value")

    assert quantity != 0, "The item didn't add to the cart"

    clear_cart = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='fr-btn cartClearButton']")))
    clear_cart.click()

    confirm = driver.switch_to.alert
    confirm.accept()





