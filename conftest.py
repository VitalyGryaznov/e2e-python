import os

import allure
import pytest
from selenium import webdriver

from dotenv import load_dotenv

env = os.getenv("ENV")

if env == 'local':
    load_dotenv("env/.env.local")
elif env == 'staging':
    load_dotenv("env/.env.staging")
else:
    load_dotenv("env/.env.local")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    # driver.get_screenshot_as_file('screenshots/selenium-get-screenshot-as-file.png')
    driver.quit()

def pytest_runtest_makereport(item, call):
    if call.when == 'call' and call.excinfo is not None:
        if "driver" in item.fixturenames:
            web_driver = item.funcargs["driver"]
            # Capture the screenshot and save it as a byte array
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name="screenshot on failure",
                attachment_type=allure.attachment_type.PNG
            )