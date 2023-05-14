from pages.modal_dialogs import ModalDialogs

def test_modal_elements(browser):
    m_ele = ModalDialogs(browser)
    m_ele.visit()
    assert m_ele.mm_elements.check_count_elements(count=5)

def test_navigation_modal(browser):
    navig_modal = ModalDialogs(browser)
    navig_modal.visit()
    navig_modal.refresh()
    navig_modal.main_icon.click()
    navig_modal.back()
    browser.set_window_size(900, 400)
    navig_modal.forward()
    # assert navig_modal.equal_url()
    # assert browser.title == navig_modal.pageData["title"]