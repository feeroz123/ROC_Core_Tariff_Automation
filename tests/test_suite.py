import unittest

import pytest

from pages.home_page.homepage import HomePage
from pages.login_page.login_page import LoginPage
from utilities.test_status import TestStatus


@pytest.mark.usefixtures("class_setup")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_user_login(self):
        self.lp.login_user("Root", "welcome1")

        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title Verification")

        result2 = self.lp.verifyValidLogin()
        self.ts.mark_final("Test_Valid_Login", result2, "Login Verification")

        self.hp.navigateTo("Tariffs")
