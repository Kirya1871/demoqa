from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class WebElements:
    def __init__(self, driver, locator=''): #принимаю от элементпэйдж
        self.driver = driver
        self.locator = locator


    def click(self):
        self.find_element().click()
    def find_element(self): #ищет по переданному драйверу и локатору
        return self.driver.find_element(By.CSS_SELECTOR,self.locator) #обращение и поиск
    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):#
        return str(self.find_element().text) #поиск элемента берем текст от найденного элемента и пеереводим в строку
    def visible(self):
        return self.find_element().is_displayed()# поиск и возврат элемента, виден или нет

    def check_count_elements(self, count:int) -> bool: #
        if len(self.find_elements()) == count: #ищет элементы по не уникальным локаторам
            return True
        return False
    def send_keys(self, text: str):
        self.find_element().send_keys(text)



