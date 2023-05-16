import time

from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa

def test_modal_elements(browser):
    m_ele = ModalDialogs(browser)
    m_ele.visit()
    assert m_ele.mm_elements.check_count_elements(count=5)

def test_navigation_modal(browser):
    navig_modal = ModalDialogs(browser)
    demoqa = DemoQa(browser)

    navig_modal.visit()
    navig_modal.refresh()
    time.sleep(2)
    navig_modal.main_icon.click()
    time.sleep(2)
    navig_modal.back()
    time.sleep(2)
    browser.set_window_size(900, 400)
    time.sleep(2)
    navig_modal.forward()
    time.sleep(2)
    assert demoqa.equal_url() #проверка урл на глав странице
    assert demoqa.get_title() == demoqa.pageData['title'] #проверка title на главной странице
    browser.set_window_size(1000, 1000) #возвращаем размеры экрана по умолчанию 1000х1000(прописаны в conftest.py)

