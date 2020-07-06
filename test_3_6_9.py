link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
import time

def test_open_link(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    laga = len(browser.find_elements_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket'))
    time.sleep(10)
    assert laga > 0, 'Ничего не найдено'

