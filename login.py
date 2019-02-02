#this is a test to log in 163 mail box
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

url = 'http://www.maiziedu.com/'
login_text = '登录'
username = 'maizi_test@139.com'
pwd = 'abc123456'


def getEleTimes(driver, times, func):
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
    if 'text_id' in arg:
        ele_login = getEleTimes(d, 60, lambda d: d.find_element_by_link_text(arg['text_id']))
        ele_login.click()
    user_ele = d.find_element_by_id(arg['user_id'])  #//*[@id="id_account_l"]
    pwd_ele = d.find_element_by_xpath(arg['pwd_id'])  #//*[@id="id_password_l"]
    login_ele = d.find_element_by_id(arg['login_id'])
    return user_ele, pwd_ele, login_ele


def sendVals(ele_tuple, arg):
    #this is to input username and password
    list_key = ['username', 'pwd']
    i = 0
    for key in list_key:
        ele_tuple[i].send_keys('')
        ele_tuple[i].clear()
        ele_tuple[i].send_keys(arg[key])
        i += 1
    #this is for login button
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
    ele_dict = {'text_id': login_text, 'user_id': 'id_account_l', 'pwd_id': '//*[@id="id_password_l"]','login_id': 'login_btn'}
    account_dict = {'username': username, 'pwd': pwd}
    ele_tuple = findElement(d, ele_dict)
    sendVals(ele_tuple, account_dict)
    #根据xpath匹配到错误的账号或者密码
    checkResult(d, '//*[@id="login-form-tips"]')


if __name__ == '__main__':
    loginTest()




