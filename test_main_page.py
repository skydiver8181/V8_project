from selenium.webdriver.common.by import By


def test_check_main_page(driver):
    main_page = driver.find_element(By.LINK_TEXT, 'Главная')
    main_page.click()

    phone_number = driver.find_element(By.CSS_SELECTOR, '[class="header-phone"]')
    phone_number_check = phone_number.text

    email = driver.find_element(By.CSS_SELECTOR, '[class="header-mail"]')
    email_check = email.text

    assert phone_number_check == '8 (342) 206-06-57'
    assert email_check == 'info@v8ru.ru'

