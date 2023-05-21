from pages.webtables import WebTables

def test_sort(browser):
    test_sort = WebTables(browser)
    test_sort.visit()
