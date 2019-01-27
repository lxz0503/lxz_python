from selenium import webdriver
import unittest
import time


class WebTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_visitURL(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        title = self.driver.title
        print(title)
        assert self.driver.title.find(u"搜狗搜索") >= 0, "assert error"

    def test_visitRecentURL(self):
        first_url = "http://www.sogou.com"
        second_url = "http://www.baidu.com"
        self.driver.get(first_url)
        self.driver.get(second_url)
        self.driver.back()
        time.sleep(5)
        self.driver.forward()

    def test_refreshCurrentUrl(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        time.sleep(5)
        self.driver.refresh()

    def test_maximizeWindow(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.minimize_window()

    def test_operateWindowHandle(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        now_handle = self.driver.current_window_handle
        print(now_handle)
        self.driver.find_element_by_id("kw").send_keys("w3cschool")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//h3[@class="t"]/a[@class="favurl"]').click()
        time.sleep(5)

    def test_getBasicInfo(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
