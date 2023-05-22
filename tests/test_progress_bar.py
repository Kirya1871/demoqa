import time

from pages.progress_bar import ProgressBar

def test_progress_bar(browser):
    test_progress_bar = ProgressBar(browser)
    test_progress_bar.visit()
    time.sleep(2)
    test_progress_bar.button_start.click()
    # time.sleep(6)
    # test_progress_bar.stop_button.click_force()

    while True:
        if test_progress_bar.poloska.get_dom_attribute('aria-value') == '51':
            test_progress_bar.button_start.click()
        break
    time.sleep(3)


