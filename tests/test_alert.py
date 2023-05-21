import time

from pages.alert import Alert


def test_alert(browser):
    t_alert = Alert(browser)
    t_alert.visit()

    assert not t_alert.alert()

    t_alert.alertButton.click()
    time.sleep(2)
    assert t_alert.alert()
    t_alert.alert().accept() #подтверждение accept

def test_alert_text(browser):
    t_a_text = Alert(browser)
    t_a_text.visit()
    t_a_text.alertButton.click()
    time.sleep(2)
    assert t_a_text.alert().text == 'You clicked a button'
    t_a_text.alert().accept()
    assert not t_a_text.alert()

def test_confirm(browser):
    t_confirm = Alert(browser)
    t_confirm.visit()
    t_confirm.confirmButton.click()
    time.sleep(2)
    t_confirm.alert().dismiss()
    assert t_confirm.confirmResult.get_text() == 'You selected Cancel'

def test_prompt(browser):
    t_prompt = Alert(browser)
    t_prompt.visit()
    t_prompt.promtButtom.click()
    time.sleep(2)
    t_prompt.alert().send_keys('ttt')
    t_prompt.alert().accept()
    assert t_prompt.promptResult.get_text() == 'You entered ttt'
    time.sleep(2)


