from pages.alert import Alert

def test_check_alert(browser):
    test_check_alert = Alert(browser)
    test_check_alert.visit()

    test_check_alert.button_alert.click_force()
