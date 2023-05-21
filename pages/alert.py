from pages.base_page import BasePage
from components.components import WebElements
class Alert(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)
        self.alertButton = WebElements (driver,'#alertButton')
        self.confirmButton = WebElements(driver,'#confirmButton')
        self.confirmResult = WebElements(driver, '#confirmResult')
        self.promtButtom = WebElements(driver, '#promtButton')
        self.promptResult = WebElements(driver, '#promptResult')
        self.button_alert = WebElements(driver, '#timerAlertButton')




