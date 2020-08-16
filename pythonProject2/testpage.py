import unittest
from locators import *
from selenium import webdriver
import time
from keywords import Keywords
from selenium.webdriver.support import expected_conditions as EC



class createEmail(unittest.TestCase, Keywords):


    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--incognito")
        self.driver = webdriver.Chrome(executable_path="D:\Chromedriver\chromedriver.exe", options=self.options)
        self.driver.maximize_window()


    def test_email_reg(self):
        self.driver.get("http://automationpractice.com/")
        self.clickBtn(Login_Page.login_tab)
        self.checkElementPresence(Login_Page.login_page_check)
        self.inputText(Login_Page.login_email_box)
        self.clickBtn(Login_Page.login_email_submit)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
