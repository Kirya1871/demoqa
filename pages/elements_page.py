from pages.base_page import BasePage
from components.components import WebElements

class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)
        self.elements = WebElements(driver, '#app > div > div > div.pattern-backgound.playgound-header') # создание нового элемента в классе страницы
        self.icon = WebElements(driver, '#app > header > a > img')# создание нового элемента
        self.btn_sidebar_first = WebElements(driver,'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElements(driver, 'div:nth-child(1) > div ul > #item-0 > span')
        self.btn_sidebar_first_checkbox = WebElements(driver, 'div:nth-child(1) > div > ul > #item-1 > span') # создание нового элемента(нужно для проверки в тест-кейсах)
        self.btns_first_menu = WebElements(driver, "div:nth-child(1) > div > ul > li")



     #   self.accordian = WebElements(driver,'#app > div > div > div.pattern-backgound.playgound-header')
    # def equal_url(self):
    #     if self.get_url() == self.base_url:
    #         return True
    #     return False
