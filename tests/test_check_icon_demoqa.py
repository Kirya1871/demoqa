
#from selenium.webdriver.common.by import By

from pages.demoqa import DemoQa
def test_icon_exist(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.icon.exist()



#     browser.get("http://demoqa.com")
# # поиск элемента
#     icon = browser.find_element(By.CSS_SELECTOR, 'header > a')
#     if icon is None:
#         print('Элемент не найден')
#     else:
#         print('Элемент найден')
