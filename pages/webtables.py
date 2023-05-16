
from pages.base_page import BasePage
from components.components import WebElements

class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.wb = WebElements(driver, '#item-3 > span')
        self.nowrowsfound = WebElements(driver, "div.rt-noData")
        self.btn_delete_row = WebElements(driver,'#delete-record-1 > svg')
        self.button_add = WebElements(driver, '#addNewRecordButton')
        self.mod_dial = WebElements(driver, '#registration-form-modal')
        self.first_name = WebElements(driver,'#firstName')
        self.last_name = WebElements(driver, '#lastName')
        self.user_email = WebElements(driver, '#userEmail')
        self.age = WebElements(driver,'#age')
        self.salary = WebElements(driver, '#salary')
        self.department =WebElements(driver, '#department')
        self.btn_submit = WebElements(driver, '#submit')
        self.edit_rec = WebElements(driver, '#edit-record-4 > svg')
        self.button_delete =WebElements(driver, '#delete-record-4 > svg')
