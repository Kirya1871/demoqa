from pages.demoqa import DemoQa
import time


def test_size(browser):
    demo_size = DemoQa(browser)
    demo_size.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)

