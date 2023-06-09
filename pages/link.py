from pages.base_page import BasePage
from components.components import WebElements


class Link(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/links'
        super().__init__(driver, self.base_url)
        self.button_link_home = WebElements(driver, '#simpleLink')
