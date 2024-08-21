import os

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

PAGE_SUB_URL = 'customer/account/login'


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "pass")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".action.login.primary")
    LOGIN_ERROR = (By.CSS_SELECTOR, ".messages [role=alert]")



    @staticmethod
    @allure.step('Opening login page via url')
    def open_via_url(driver):
        BASE_URL = os.getenv("BASE_URL")
        LOGIN_LINK = BASE_URL + PAGE_SUB_URL
        driver.get(LOGIN_LINK)
        page = LoginPage(driver)
        page.verify_page_loaded()
        return page

    @allure.step('Verifying that login page has loaded')
    def verify_page_loaded(self):
        self.wait_for_element_to_be_visible(self.EMAIL_INPUT)
        self.wait_for_element_to_be_visible(self.SUBMIT_BUTTON)

    @allure.step('Entering credentials on the login page')
    def enter_credentials(self, credentials):
        self.enter_text(self.PASSWORD_INPUT, credentials["password"])
        self.enter_text_and_verify(self.EMAIL_INPUT, credentials["email"])

    @allure.step('Submitting login form')
    def submit_login_form(self):
        self.click_on_element(self.SUBMIT_BUTTON)

    @allure.step('Verifying that error message is displayed on the login page')
    def verify_login_error_is_displayed(self):
        self.wait_for_element_to_be_visible(self.LOGIN_ERROR)


