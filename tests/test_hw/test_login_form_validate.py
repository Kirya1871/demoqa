import time

from pages.form_page import FormPage

def test_login_form_validate(browser):
    lf_validate = FormPage(browser)
    lf_validate.visit()
    assert lf_validate.first_name.get_dom_attribute('placeholder') == 'First Name'
    time.sleep(2)
    assert lf_validate.last_name.get_dom_attribute('placeholder') == 'Last Name'
    time.sleep(2)
    assert lf_validate.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    time.sleep(2)


#^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$
