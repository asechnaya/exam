import pytest
import allure

from pages.global_variables import COW_GROUP, FARM, LINK, PASSWORD, USER
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.smoke
@allure.feature("Cow search feature")
@allure.story("user should be able to search cow and to make a screenshot")
@allure.title('Negative cases for login page')
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

