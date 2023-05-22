import pytest
from pages.demoqa import DemoQa
from pages.radio_button import RadioButton


@pytest.mark.skip
def test_decor(browser):
    test_decor = DemoQa(browser)
    test_decor.visit()
    assert test_decor.h5.check_count_elements(6)

    for element in test_decor.h5.check_count_elements():
        assert element.text != ''

# @pytest.mark.skipif(True, reason = 'просто пропуск')
def test_radio_button(browser):
    test_radio_button = RadioButton(browser)
    if not test_radio_button.code_status():
        pytest.skip(reason=f"Страница {test_radio_button.base_url} недоступно")
    test_radio_button.visit()
    test_radio_button.yes.click_force()
    assert test_radio_button.text.get_text() == 'You have selected Yes'
    test_radio_button.impressive.click_force()
    assert test_radio_button.text.get_text() == 'You have selected Impressive'
    assert 'disabled' in test_radio_button.no.get_dom_attribute('class')

