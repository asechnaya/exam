from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_OUT_BUTTON = (By.CLASS_NAME, "btn-profile")
    LOGIN_OUT_ICON = (By.CLASS_NAME, "icon.icon-sign-out")
    LOGIN_OUT_TEXT = (By.XPATH, "//div[6]")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".icon-find")
    SEARCH_INPUT = (By.CSS_SELECTOR, ".txt-search")
    COW_NUMBER = (By.CSS_SELECTOR, "div.search-results-types > ul > li:nth-child(1) > span > span > span:nth-child(3)")


class AfterSearchLocators:
    ANIMAL_NAME = (By.CLASS_NAME, "animal-name")
    TITLE = (By.CSS_SELECTOR, ".animal-events-title")
    ANIMAL_CONTENT = (By.CSS_SELECTOR, ".event-cell-content")
    HEAT = (By.LINK_TEXT, "Heat")
    HEAT_DIAGRAM = (By.CSS_SELECTOR, "#chart-container_ChartAreaBorder")


class LoginPageLocators:
    LOGIN_FORM = (By.NAME, "loginForm")
    USER_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    FARM_INPUT = (By.NAME, "farmId")
    PASSWORD_VISIBLE = (By.CSS_SELECTOR, ".hide-password")
    PASSWORD_NOT_VISIBLE = (By.CSS_SELECTOR, ".show-password")
    REMEMBER_CHECKBOX = (By.CSS_SELECTOR, "div.form-field.form-field-title.remember-me")
    REMEMBER_CHECKBOX_SELECTED = (By.CSS_SELECTOR, "div.form-field.form-field-title.remember-me.selected")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-btn")
