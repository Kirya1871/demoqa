from pages.elements_page import ElementsPage

def test_find_elements(browser):
    demo_qa_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.btns_first_menu.check_count_elements(count=9)
