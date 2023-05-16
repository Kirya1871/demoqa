from components.components import WebElements
from pages.base_page import BasePage


class TextBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElements(driver, '#userName')
        self.user_email = WebElements(driver, '#userEmail')
        self.currentAddress = WebElements(driver, '#currentAddress')
        self.submit = WebElements(driver,'#submit')

