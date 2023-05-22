from pages.base_page import BasePage
from components.components import WebElements

class ProgressBar(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar'
        super().__init__(driver, self.base_url)
        self.button_start = WebElements(driver, '#startStopButton')
        self.poloska = WebElements(driver, '#progressBar')





