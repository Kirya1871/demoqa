
from pages.text_box import TextBox
def test_placeholder(browser):
    place_h = TextBox(browser)
    place_h.visit()
    assert place_h.full_name.get_dom_attribute('placeholder') == 'Full Name'
