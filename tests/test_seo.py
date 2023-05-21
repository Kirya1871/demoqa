import time

import pytest
from pages.demoqa import DemoQa
from pages.accordian import Accordian
from pages.alert import Alert
from pages.browser_tab import BrowserTab
def test_check_title_demo(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert browser.title == 'DEMOQA' #demo_qa_page.pageData["title"]

@pytest.mark.parametrize('pages',[Accordian, Alert,DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert browser.title == page.pageData['title']

