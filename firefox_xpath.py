#xpath with firefox

import time
from selenium import webdriver

url = "http://www.baidu.com"
driver = webdriver.Firefox()
driver.get(url)
now_handle = driver.current_window_handle
print(now_handle)
driver.find_element_by_id("kw").send_keys("w3cschool")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.find_element_by_xpath('//h3[@class="t"]/a[@class="favurl"]').click()
time.sleep(5)

#ele = b.find_element_by_css_selector('input[name="first name"]')
#ele.send_keys('aaaa')
#print(id(ele))
