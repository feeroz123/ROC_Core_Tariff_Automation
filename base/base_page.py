import logging

from base.selenium_driver import SeleniumDriver
from utilities import custom_logger as cl


class BasePage(SeleniumDriver):

    log = cl.custom_logging(logging.INFO)

    def __init__(self, driver):
        self.driver = driver

    def verify_page_title(self, expected_title):
        actual_title = self.getTitle()

        if actual_title == expected_title:
            self.log.info("Page Title Matched to :" + expected_title)
        else:
            self.log.info("Page Title Not Matched to :" + expected_title)

    def click_clear_button(self):
        self.clickElement("clear")

    def click_search_button(self):
        self.click_clear_button()
        self.clickElement("search")
