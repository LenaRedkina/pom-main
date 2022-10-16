from python_signIn.browser import Browser
from python_signIn.Pages.Sign_in import Locators
from selenium.webdriver.common.keys import Keys

class Element:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.element = self.driver.find_element(self.locator[0], self.locator[1])

    def click_on_element(self):
        self.element.click()


class InputElement(Element):
    def enter_text(self, text):
        self.click_on_element()
        self.element.send_keys(text)

    def get_text(self):
        return self.element.get_attribute("value")


class ButtonElement(Element):
    def key_code(self):
        return self.element.send_keys(Keys.ENTER)
