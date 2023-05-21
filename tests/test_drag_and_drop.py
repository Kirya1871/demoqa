import time

from pages.droppable import Droppable
from selenium.webdriver import ActionChains


def test_drag_and_drop(browser):
    t_d_a_d = Droppable(browser)
    action_chains = ActionChains(browser)

    t_d_a_d.visit()
    assert t_d_a_d.drop.check_css_new('backgroundColor', 'rgba(0, 0, 0, 0)')

    action_chains.drag_and_drop(
        t_d_a_d.drag.find_element(),
        t_d_a_d.drop.find_element()
    ).perform()

    time.sleep(2)

    assert t_d_a_d.drop.check_css_new('backgroundColor', 'rgba(70, 130, 180, 1)')

    time.sleep(2)
    action_chains.drag_and_drop_by_offset(t_d_a_d.drag.find_element(),
                                          -200, 0
                                          ).perform()
    time.sleep(2)
    assert t_d_a_d.drop.check_css_new('backgroundColor', 'rgba(70, 130, 180, 1)')


# def drag_and_drop_by_offset(self, source, xoffset, yoffset):


