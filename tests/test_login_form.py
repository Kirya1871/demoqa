from pages.form_page import FormPage
import time
def test_login_form(browser):
    log_form = FormPage(browser)
    log_form.visit()

    assert not log_form.modal_dialog.exist()
    time.sleep(2)
    log_form.first_name.send_keys('tester')
    log_form.last_name.send_keys('testerovich')
    log_form.user_email.send_keys('test@ttt.tt')
    log_form.gender_radio_1.click()
    log_form.user_number.send_keys('987987987987')
    time.sleep(2)
    log_form.btn_submit.click()
    time.sleep(2)

