import unittest

import allure
from allure_commons.types import AttachmentType
from locators import *
from selenium import webdriver
import time
from keywords import Keywords
from allure_behave.hooks import allure_report
from selenium.webdriver.support import expected_conditions as EC


@allure.severity(allure.severity_level.NORMAL)
class createEmail(unittest.TestCase, Keywords):


    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--incognito")
        self.driver = webdriver.Chrome(executable_path="\Chromedriver\chromedriver.exe", options=self.options)
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument("--test-type")
        self.driver.maximize_window()


    def test_email_reg(self):

        self.driver.get("http://automationpractice.com/")

        self.clickBtn(Login_Page.login_tab)
        self.checkElementPresence(Login_Page.login_page_check)
        self.inputText(Login_Page.login_email_box)
        self.clickBtn(Login_Page.login_email_submit)
        allure.attach(self.driver.get_screenshot_as_png(), name="test_email_reg",attachment_type=AttachmentType.PNG)
        # allure_report("allure_report")

    def tearDown(self):

        self.driver.close()

# if __name__ == '__main__':
#     unittest.main()
