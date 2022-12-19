from logs.testlogger import logger
from .locators import LoginPageLocators
from .base_page import BasePage
from .main_page import MainPage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_user_input()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_user_input(self):
        assert self.is_element_present(*LoginPageLocators.USER_INPUT), "User input is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT), "password input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "button input is not presented"
        assert self.is_element_present(*LoginPageLocators.REMEMBER_CHECKBOX), "remember checkbox is not presented"

    def fill_the_form(self, key1, key2, key3):
        self.fill_the_input(*LoginPageLocators.USER_INPUT, key1)
        self.fill_the_input(*LoginPageLocators.PASSWORD_INPUT, key2)
        self.fill_the_input(*LoginPageLocators.FARM_INPUT, key3)
        self.click_the_button(*LoginPageLocators.LOGIN_BUTTON)
        return MainPage(browser=self.browser, url=self.browser.current_url)

    def click_remember_me(self):
        if self.is_element_present(*LoginPageLocators.REMEMBER_CHECKBOX):
            logger.error("REMEMBER_CHECKBOX element is presented")
            if self.is_element_present(*LoginPageLocators.REMEMBER_CHECKBOX_SELECTED):
                self.click_the_button(*LoginPageLocators.REMEMBER_CHECKBOX)
            else:
                pass
                logger.info("CHECKBOX element has already been selected")
        else:
            logger.error("REMEMBER_CHECKBOX element is not presented!")

    def password_should_be_invisible(self):
        if self.is_element_present(*LoginPageLocators.PASSWORD_NOT_VISIBLE):
            assert self.is_element_present(*LoginPageLocators.PASSWORD_VISIBLE)
            logger.warning("PASSWORD is not in invisible mode")
            self.click_the_button(*LoginPageLocators.PASSWORD_VISIBLE)
            logger.info("PASSWORD has been switched to invisible mode")
        else:
            logger.error("NO VISIBLE MODE IS PRESENTED")
