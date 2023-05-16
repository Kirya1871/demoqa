

from pages.herokuapp import HeroKuapp
from pages.Add_element import AddElement


def test_btn_add(browser):
    tba = HeroKuapp(browser)
    AElem = AddElement(browser)

    tba.visit()
    assert tba.add_remove_elements.visible()
    tba.add_remove_elements.click()
    assert AElem.equal_url()
    assert AElem.btn_add.get_text() == 'Add Element' #проверка текста на кнопке
    assert AElem.btn_add.get_dom_attribute('onclick') == 'addElement()'
    for i in range(4):
        AElem.btn_add.click()
    assert AElem.btns_delete.check_count_elements(4)

    for element in AElem.btns_delete.find_elements():
        assert element.text == 'Delete'

    while AElem.btns_delete.exist():
            AElem.btns_delete.click()

    assert not AElem.btns_delete.exist()





