import pytest

link = "https://v8ru.ru"

@pytest.fixture(scope='function')
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)
    driver.add_cookie({'name': 'ABCPUser', 'value': 'ivan273681%40gmail.com-----e10adc3949ba59abbe56e057f20f883e'})
    driver.get(link)
    yield driver
    driver.quit()





# @pytest.fixture(scope='session')
# def driver():
#     from selenium import webdriver
#     from webdriver_manager.chrome import ChromeDriverManager
#     from selenium.webdriver.chrome.service import Service
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     yield driver
#     driver.quit()