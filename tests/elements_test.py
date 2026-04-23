from pages.base_page import BasePage
import time

def test(driver):
    page = BasePage(driver, 'https://google.com')
    page.open()

    time.sleep(6)