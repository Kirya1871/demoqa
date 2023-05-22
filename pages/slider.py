from pages.base_page import BasePage
from components.components import WebElements
class Slider(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'
        super().__init__(driver, self.base_url)
        self.pole = WebElements(driver, '#sliderContainer > div.col-9 > span > input')
        self.drag = WebElements(driver,'#sliderContainer > div.col-9 > span > input')
        self.drop = WebElements(driver, '#sliderContainer > div.col-9 > span > div')

