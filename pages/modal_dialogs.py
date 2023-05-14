from components.components import WebElements
from pages.base_page import BasePage

class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.mm_elements = WebElements(driver, '#item-4')
        self.main_icon = WebElements(driver, '#app > header > a > img')

