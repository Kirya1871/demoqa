import time

from pages.webtables import WebTables

def test_web_tables(browser):
    test_wb = WebTables(browser)
    test_wb.visit()

    assert not test_wb.nowrowsfound.exist()

    while test_wb.btn_delete_row.exist():
        test_wb.btn_delete_row.click()
        time.sleep(5)




