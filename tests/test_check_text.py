from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.text()

def test_page_elements(browser): # назв функции,связана с конфгтест
    obj_page = ElementsPage(browser) #созд объекта стран
    obj_page.visit() #вызов метода входа на страницу
    assert obj_page.elements.get_text() == 'Elements' # сравнение ФР и ОР (assert-сравнение)обращение к старнице, к новому элементу - вызов метода получ текста
#обращение к странице
    assert obj_page.icon.exist() #вызов метода exist (наличие на странице)
    assert obj_page.btn_sidebar_first.exist()
    assert obj_page.btn_sidebar_first_textbox.exist()





