from pages.slider import Slider
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def test_slider(browser):
    # test_slider = Slider(browser)
    # action_chains = ActionChains(browser)
    # test_slider.visit()
    #
    # action_chains.drag_and_drop(
    #     test_slider.drag.find_element(),
    #     test_slider.drop.find_element()
    # ).perform()
    # action_chains.drag_and_drop_by_offset(test_slider.drag.find_element(),
    #                                       0, 25
    #                                       ).perform()

    test_slider = Slider(browser)
    test_slider.visit()

    assert test_slider.pole.exist()
    assert test_slider.drop.exist()

    while test_slider.drop.get_dom_atttribute('value') == '50':
        test_slider.pole.send_keys(Keys.ARROW_RIGHT)

    assert test_slider.drop.get_dom_atttribute('value') == '50'
