#this is a test to log in 163 mail box
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

url = 'http://www.maiziedu.com/'
login_text = '登录'
username = 'maizi_test@139.com'
pwd = 'abc123456'


def getEleTimes(driver, times, func):
    #设置了页面等待时间，用来找到耗时比较长的页面元素
    return WebDriverWait(driver, times).until(func)


def openBrowser():
    ''' return a webdriver handle'''
    webdriver_handle = webdriver.Firefox()
    return webdriver_handle


def openUrl(handle,url):
    handle.get(url)
    handle.maximize_window()


def findElement(d, arg):
    #this is to find username, password and login button
    #耗时比较长，默认60秒后超时，查找'登录'这个元素耗时比较长
    if 'text_id' in arg:
        ele_login = getEleTimes(d, 60, lambda d: d.find_element_by_link_text(arg['text_id']))
        ele_login.click()
    user_ele = d.find_element_by_id(arg['user_id'])  #//*[@id="id_account_l"]，找到对应用户名的那个元素
    pwd_ele = d.find_element_by_xpath(arg['pwd_id'])  #//*[@id="id_password_l"]，找到对应密码的那个元素
    login_ele = d.find_element_by_id(arg['login_id'])  #找到对应登录按钮的那个元素
    return user_ele, pwd_ele, login_ele   #返回三个元素，组成一个三元祖


def sendVals(ele_tuple, arg):
    #this is to input username and password
    list_key = ['username', 'pwd']
    i = 0
    for key in list_key:
        ele_tuple[i].send_keys('')
        ele_tuple[i].clear()
        #分别对应用户名和密码那个元素，然后输入内容
        ele_tuple[i].send_keys(arg[key])
        i += 1
    #this is to click login button
    ele_tuple[2].click()


def checkResult(d, text):
    try:
        d.find_element_by_xpath(text)  #//*[@id="login-form-tips"]
        print("账号或者密码错误，请重新输入")
    except:
        print("right")


def loginTest():
    d = openBrowser()
    openUrl(d, url)
    #下面的字典包含了首页的登陆，邮箱页的用户名，密码
    ele_dict = {'text_id': login_text, 'user_id': 'id_account_l', 'pwd_id': '//*[@id="id_password_l"]','login_id': 'login_btn'}
    #下面的字典用来保存登录用的用户名和密码
    account_dict = {'username': username, 'pwd': pwd}
    #找到各个登录用的元素
    ele_tuple = findElement(d, ele_dict)
    #找到元素后，分别点击或者输入内容
    sendVals(ele_tuple, account_dict)
    #检查结果，根据xpath匹配到错误的账号或者密码
    checkResult(d, '//*[@id="login-form-tips"]')


if __name__ == '__main__':
    loginTest()




