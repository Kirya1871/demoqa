
from pages.accordian import Accordian
import time
def test_visible_accordian(browser):
    obj_page = Accordian(browser) #созд объекта стран
    obj_page.visit() #вызов метода входа на страницу
    assert obj_page.accordian.visible() #проверка на видимость элемента
    obj_page.f_accordian.click() #вызов метода клик для созданного элемента
    time.sleep(2)
    assert not obj_page.accordian.visible() #проверка отсутствия видимости первого элемента

def test_visible_accordian_default(browser):
    t_default = Accordian(browser)
    t_default.visit()
    time.sleep(2)
    assert not t_default.fdefault.visible()
    assert not t_default.gdefault.visible()
    assert not t_default.hdefault.visible()