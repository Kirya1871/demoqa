from pages.elements_page import ElementsPage
import time
def test_visible_btn_sidebar(browser):
    obj_page = ElementsPage(browser)
    obj_page.visit()
    #obj_page.sidebar_first.click() #вызов метода клик
    time.sleep(3)
    #assert obj_page.btn_sidebar_first_textbox.exist()
    assert obj_page.btn_sidebar_first_textbox.visible()

def test_not_visible_btn_sidebar(browser): # назв функции,связана с конфгтест
    obj_page = ElementsPage(browser) #созд объекта стран
    obj_page.visit()  #вызов метода входа на страницу
    assert obj_page.btn_sidebar_first_checkbox.visible() #проверка,что элемент виден.Он у нас прописан в классе ElementsPage
    obj_page.btn_sidebar_first.click() #вызов метода клик для кнопки btn_sidebar_first
    time.sleep(2)
    assert not obj_page.btn_sidebar_first_checkbox.visible() #отриц проверка
