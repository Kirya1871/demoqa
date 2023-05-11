import pytest
from selenium import webdriver

@pytest.fixture(scope= "session")
def browser(): #название функции
    driver = webdriver.Chrome() #создание виртуальный браузер
    driver.set_window_size(1000, 1000)
    yield driver
    driver.quit()
