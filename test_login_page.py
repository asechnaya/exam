import allure
import pytest

from pages.global_variables import FARM, LINK, PASSWORD, USER
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Login feature")
@allure.story("user should be able to login to search the cow")
@allure.title('Negative cases for login page')
@allure.testcase("https://st.scrdairy.com/", "Разработка автотестов для главной страницы")
@pytest.mark.xpass
class TestLoginPage:
    def test_login_with_remember_mark(self, browser):
        with allure.step("Открываем главную страницу"):
            browser.delete_all_cookies()
            page = LoginPage(browser, LINK)
            page.open()
            page.should_be_login_page()
            page.click_remember_me()
            page.fill_the_form(USER, PASSWORD, FARM)
            main_page = MainPage(browser, browser.current_url)
            main_page.should_be_main_page()

    def test_login_without_remember_mark(self, browser):
        browser.delete_all_cookies()
        page = LoginPage(browser, LINK)
        page.open()
        page.should_be_login_page()
        page.fill_the_form(USER, PASSWORD, FARM)
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_main_page()

    def test_password_should_be_not_visible(self, browser):
        browser.delete_all_cookies()
        page = LoginPage(browser, LINK)
        page.open()
        page.should_be_login_page()
        page.password_should_be_invisible()