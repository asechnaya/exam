import configparser
import time

import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8-sig')
USER, PASSWORD, FARM = config.get("DEMO", 'Email'), config.get("DEMO", "Password"), config.get("DEMO", "FarmID")

LINK = "https://st.scrdairy.com/"


@pytest.mark.login
class TestLoginPage:
    def test_login_with_remember_mark(self, browser):
        browser.delete_all_cookies()
        page = LoginPage(browser, LINK)
        page.open()
        page.should_be_login_page()
        page.click_remember_me()
        page.fill_the_form(USER, PASSWORD, FARM)
        time.sleep(4)

    def test_login_without_remember_mark(self, browser):
        browser.delete_all_cookies()
        page = LoginPage(browser, LINK)
        page.open()
        page.should_be_login_page()

    def test_password_should_be_not_visible(self, browser):
        browser.delete_all_cookies()
        page = LoginPage(browser, LINK)
        page.open()
        page.should_be_login_page()
        page.password_is_invisible()