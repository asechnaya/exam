import configparser

import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8-sig')
USER, PASSWORD, FARM = config.get("DEMO", 'Email'), config.get("DEMO", "Password"), config.get("DEMO", "FarmID")

LINK = "https://st.scrdairy.com/"
COW_GROUP = 15


@pytest.mark.smoke
class TestCowSearch:
    def test_user_can_find_a_cow(self, browser):
        login_page = LoginPage(browser, LINK)
        login_page.open()
        login_page.should_be_login_page()
        login_page.fill_the_form(USER, PASSWORD, FARM)
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_main_page()
        main_page.search_the_cow(COW_GROUP)
        main_page.should_be_history()
        main_page.click_on_heat()
        main_page.make_screenshot("screenshots/screen.png")

