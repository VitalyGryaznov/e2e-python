from time import sleep
import os

import allure
import pytest

from components.header_component import HeaderComponent
from helpers.data_helper import get_valid_credentials, get_invalid_credentials
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.feature('login')
@allure.story('positive login cases')
@pytest.mark.login
def test_successful_login(driver):
    """
    This test is checking that after entering valid credentials user is logged in
    """
    credentials = get_valid_credentials()
    home_page = HomePage.open_via_url(driver)
    header_component = HeaderComponent(driver)
    header_component.verify_component_loaded()
    header_component.click_on_login_link()
    login_page = LoginPage(driver)
    login_page.verify_page_loaded()
    login_page.enter_credentials(credentials)
    login_page.submit_login_form()
    home_page.verify_page_loaded()
    header_component.verify_logged_in()


@allure.feature('login')
@allure.story('negative login cases')
@pytest.mark.login
def test_login_with_invalid_credentials(driver):
    """
       This test is checking that after invalid credentials user can see error message on the login page
    """
    credentials = get_invalid_credentials()
    login_page = LoginPage.open_via_url(driver)
    login_page.enter_credentials(credentials)
    login_page.submit_login_form()
    login_page.verify_login_error_is_displayed()
    login_page.verify_page_loaded()
