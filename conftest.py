import pytest
from selenium import webdriver

@pytest.fixture(scope= "session")# декоратор
def browser(): #название функции
    driver = webdriver.Chrome() #создание виртуальный браузер
    driver.set_window_size(1500, 900)
    yield driver
    driver.quit()


