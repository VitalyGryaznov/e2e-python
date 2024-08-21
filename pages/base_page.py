from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def wait_for_element_to_be_visible(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator))

    def enter_text_and_verify(self, locator, text):
        print("Entering text {0} to element {1} {2}".format(text, locator[0], locator[1]))
        element = self.wait_for_element_to_be_visible(locator)
        element.send_keys(text)
        self.wait.until(expected_conditions.text_to_be_present_in_element_value(locator, text))

    def enter_text(self, locator, text):
        print("Entering text {0} to element {1} {2}".format(text, locator[0], locator[1]))
        element = self.wait_for_element_to_be_visible(locator)
        element.send_keys(text)


    def click_on_element(self, locator):
        print("clicking on element with locator: {0} {1}".format(locator[0], locator[1]))
        element = self.wait_for_element_to_be_visible(locator)
        self.wait_for_element_to_be_clickable(locator)
        element.click()