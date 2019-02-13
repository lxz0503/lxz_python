from selenium import webdriver
import unittest
from lxz_python.login_page import LoginPage


class TestPageObj(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.username = '534188479'  # 调试的时候需要换成对应的QQ号
        self.password = 'pppp'  # 需要换成对应的密码

    def tearDown(self):
        self.driver.quit()

    def test_user_login(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.open()
        driver.maximize_window()
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id("switcher_plogin").click()
        login_page.type_username(self.username)
        login_page.type_password(self.password)
        login_page.type_submit()
        self.assertIn('QQ空间-分享生活，留住感动', driver.title)


if __name__ == '__main__':
    unittest.main()