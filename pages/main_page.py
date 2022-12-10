from .base_page import BasePage
from .locators import AfterSearchLocators, MainPageLocators


class MainPage(BasePage):
    def should_be_main_page(self):
        self.should_search_button()
        self.should_be_demo_url()
        self.should_be_logout_icon()

    def should_be_demo_url(self):
        assert '/demo/' in self.browser.current_url, "Demo dashboard url is not found"

    def should_search_button(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_BUTTON), 'Search button is not presented'

    def should_be_logout_icon(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_OUT_BUTTON), 'LogOut image is not presented'
        assert self.is_element_present(*MainPageLocators.LOGIN_OUT_ICON), 'LogOut icon is not presented'

    def should_be_history(self):
        assert self.is_element_present(*AfterSearchLocators.ANIMAL_NAME), "Animal name is not presented"
        assert self.get_the_text(*AfterSearchLocators.ANIMAL_NAME) == "15", "Animal name is not presented"
        assert self.is_element_present(*AfterSearchLocators.TITLE), "Title is not presented"
        assert self.is_element_present(*AfterSearchLocators.ANIMAL_CONTENT), "History is not presented"

    def search_the_cow(self, key):
        self.click_the_button(*MainPageLocators.SEARCH_BUTTON)
        self.fill_the_input(*MainPageLocators.SEARCH_INPUT, key)
        self.click_the_button(*MainPageLocators.COW_NUMBER)

    def logout(self):
        self.is_element_present(*MainPageLocators.LOGIN_OUT_BUTTON)
        self.click_the_button(*MainPageLocators.LOGIN_OUT_ICON)
        self.get_the_text(*MainPageLocators.LOGIN_OUT_TEXT)
        self.click_the_button(*MainPageLocators.LOGIN_OUT_TEXT)



