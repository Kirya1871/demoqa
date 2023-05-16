from pages.text_box import TextBox


def test_text_box_submit(browser):
    ttbox = TextBox(browser)
    ttbox.visit()
    assert ttbox.submit.check_css('color, rgb(255, 255, 255)')
    assert ttbox.submit.check_css('backgroundColor, rgb(0, 123, 255)')
    assert ttbox.submit.check_css('borderColor', 'rgb(0, 123, 255)')