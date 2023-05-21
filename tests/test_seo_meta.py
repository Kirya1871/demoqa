import time

import pytest
from pages.demoqa import DemoQa
from pages.accordian import Accordian
from pages.alert import Alert
from pages.browser_tab import BrowserTab

@pytest.mark.parametrize("pages", [Accordian, Alert,DemoQa, BrowserTab])
def test_seo_meta(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.metaView.exist()
    assert page.metaView.get_dom_attribute('name') == "viewport"
    assert page.metaView.get_dom_attribute('content') == "width=device-width, initial-scale=1"
