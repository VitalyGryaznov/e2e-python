import os

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    HOME_PAGE_PROMO = (By.CSS_SELECTOR, ".block-promo.home-main")
    LOGIN_LINK = (By.CSS_SELECTOR, "header .authorization-link")

    @staticmethod
    @allure.step('Opening home page via url')
    def open_via_url(driver):
        with allure.step('opening home page'):
            driver.get(os.getenv("BASE_URL"))
        with allure.step('verifying the home page loaded'):
            home_page = HomePage(driver)
            home_page.verify_page_loaded()
        return home_page

    @allure.step('Verifying that home page has loaded')
    def verify_page_loaded(self):
        self.wait_for_element_to_be_visible(self.HOME_PAGE_PROMO)
