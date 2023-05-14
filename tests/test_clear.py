import time

from pages.text_box import TextBox

def test_clear(browser):
    t_clear = TextBox(browser)
    t_clear.visit()
    t_clear.full_name.send_keys('trdgdgrt')
    time.sleep(2)
    t_clear.full_name.clear()
    time.sleep(2)
    assert t_clear.full_name.get_text()==''



