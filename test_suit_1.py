
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://v8ru.ru"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
browser.add_cookie({'name': 'ABCPUser', 'value': 'ivan273681%40gmail.com-----e10adc3949ba59abbe56e057f20f883e'})
browser.get(link)

def search():
    search = browser.find_element(By.ID, "pcode")
    search.send_keys("CUK1919")

    search_button = browser.find_element(By.CSS_SELECTOR, "[class='fr-icon3-search']")
    search_button.click()

    cod_item_value = browser.find_element(By.CSS_SELECTOR, "[class='casePartCode ']")
    cod_item = cod_item_value.get_attribute("value")

    assert cod_item == "CUK1919", "Search function works incorrect"
