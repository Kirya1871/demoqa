from pages.link import Link
from pages.demoqa import DemoQa
def test_window_tab(browser):
    test_window_tab = Link(browser)
    demo_qa = DemoQa(browser)
    test_window_tab.visit()
    test_window_tab.button_link_home.click()
    assert demo_qa

