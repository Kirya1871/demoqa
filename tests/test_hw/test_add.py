import time

from pages.webtables import WebTables

def test_add(browser):
    test_add = WebTables(browser)
    test_add.visit()
    test_add.button_add.click()
    time.sleep(4)

    # assert test_add.mod_dial.exist()

    test_add.first_name.send_keys('Ter')
    test_add.last_name.send_keys('Loo')
    test_add.user_email.send_keys('ter@loo.com')
    test_add.age.send_keys('100')
    test_add.salary.send_keys('1111111')
    test_add.department.send_keys('itmo')
    test_add.btn_submit.click_force()
    time.sleep(4)
    test_add.edit_rec.click()
    test_add.first_name.send_keys('Teret')
    test_add.btn_submit.click_force()
    time.sleep(2)
    test_add.button_delete.click_force()
    time.sleep(5)
