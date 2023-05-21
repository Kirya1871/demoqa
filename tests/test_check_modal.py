import time

from pages.modal_dialogs import ModalDialogs

def test_check_modal(browser):
    t_check_modal = ModalDialogs(browser)
    t_check_modal.visit()

    t_check_modal.button_smallmodall.click_force()
    t_check_modal.close_btn_smallmodall.click_force()
    time.sleep(2)
    t_check_modal.button_largemodall.click_force()
    t_check_modal.close_btn_largemodall.click_force()


