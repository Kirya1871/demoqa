from pages.base_page import BasePage
from components.components import WebElements

class RadioButton(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)
        self.yes = WebElements(driver, '#yesRadio')
        self.impressive = WebElements(driver,'#impressiveRadio')
        self.text = WebElements(driver,'')
