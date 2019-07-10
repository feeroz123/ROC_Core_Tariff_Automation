from base.base_page import BasePage
import logging
import utilities.custom_logger as cl


class LoginPage(BasePage):

    log = cl.custom_logging(logging.DEBUG)

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)     # Passing the driver instance to parent/super class
        self.driver = driver

    # Locators
    _usernameField = "username-input-area"  # id
    _passwordField = "password-input-area"  # id
    _loginButton = "btn"    # id


    def enterEmail(self, email):
        self.sendKeys(email, self._usernameField)

    def enterPassword(self, password):
        self.sendKeys(password, self._passwordField)

    def clickLoginButton(self):
        self.clickElement(self._loginButton)

    def login_user(self, email, password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyValidLogin(self):
        element_presence = self.isElementPresent("grouptTitle", locator_type="id")
        return element_presence

    def verifyInvalidLogin(self):
        element_presence = self.isElementPresent("//div[contains(text(), 'Invalid Credentials')]", locator_type="xpath")
        return element_presence

    def verifyTitle(self):
        if "ROC - Subex Ltd - Home Dashboard" in self.getTitle():
            return True
        else:
            return False
