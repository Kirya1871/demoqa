import time

from pages.text_box import TextBox

def test_text_box(browser):
    tt_box = TextBox(browser)
    tt_box.visit()
    tt_box.full_name.send_keys('Fer Der')
    tt_box.currentAddress.send_keys('Derevnya Zarya')
    tt_box.submit.click_force()
    time.sleep(5)



