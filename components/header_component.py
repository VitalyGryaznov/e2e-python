import os

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderComponent(BasePage):
    LOGIN_LINK = (By.CSS_SELECTOR, "header .authorization-link")
    HEADER = (By.CSS_SELECTOR, ".panel.header")
    LOGGED_IN_GREETING = (By.CSS_SELECTOR, ".logged-in")

    @allure.step('Verifying that login component has loaded')
    def verify_component_loaded(self):
        self.wait_for_element_to_be_visible(self.HEADER)

    @allure.step('Clicking on login link in the header')
    def click_on_login_link(self):
        self.click_on_element(self.LOGIN_LINK)

    @allure.step('Verifying that used is logged in')
    def verify_logged_in(self):
        self.wait_for_element_to_be_visible(self.LOGGED_IN_GREETING)
