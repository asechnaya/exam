from datetime import datetime

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from logs.testlogger import logger


class BasePage:
    def __init__(self, browser, url, timeout=20):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self, timeout=13):
        self.browser.get(self.url)
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        self.browser.implicitly_wait(timeout)

    def element_exists(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            logger.error(f"{what} element is not presented")
            return False

    def is_element_present(self, how, what):
        self.element_exists(how, what)
        return True

    def fill_the_input(self, how, what, key):
        self.element_exists(how, what)
        self.browser.find_element(how, what).send_keys(key)

    def click_the_button(self, how, what):
        self.element_exists(how, what)
        self.browser.find_element(how, what).click()

    def get_the_text(self, how, what):
        self.element_exists(how, what)
        try:
            text = self.browser.find_element(how, what).text
            return text
        except AttributeError:
            logger.error(f"{what} element is not presented")

    def make_screenshot(self, name):
        timing = str(datetime.now().strftime("_%d_%m_%y_%H-%M-%S"))
        logger.info(f"Screenshot has been captured at {datetime.now().isoformat()}")
        try:
            self.browser.save_screenshot(name + timing + ".jpg")
        except ModuleNotFoundError:
            logger.error("No module screenshot problem")
            return False
