
from pages.accordian import Accordian
import time
def test_visible_accordian(browser):
    obj_page = Accordian(browser)
    obj_page.visit()
    assert obj_page.accordian.visible()
    obj_page.f_accordian.click()
    time.sleep(2)
    assert not obj_page.f_accordian.visible()