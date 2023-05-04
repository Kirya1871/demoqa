from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    test_check_text() = ElementsPage(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()

