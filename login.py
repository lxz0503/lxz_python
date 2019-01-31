#this is a test to log in 163 mail box
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

url = 'http://www.maiziedu.com/'
login_text = '登录'
account = 'maizi_test@139.com'
pwd = 'abc123456'

def getEleTimes(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def openBrowser():
    ''' return a webdriver handle'''
    webdriver_handle =  webdriver.Firefox()
    return webdriver_handle

def openUrl(handle,url):
    handle.get(url)
    handle.maximize_window()

def findElement(d,arg):
    if text_id in arg:
        ele_login = getEleTimes(d, 10, lambda d: d.find_element_by_link_text(arg['text_id']))
        ele_login.click()

    user_ele = d.find_element_by_id(arg['user_id'])
    pwd_ele = d.find_element_by_id(arg['pwd_id'])
    login_ele = d.find_element_by_id(arg['login_id'])
    return user_ele,pwd_ele,login_ele

def sendVals(ele_tuple,arg):
    list_key = ['uname','pwd']
    i = 0
    for key in list_key:
        ele_tuple[i].send_keys('')
        ele_tuple[i].clear()
        ele_tuple[i].send_keys(arg[key])
        i+=1
    ele_tuple[2].click()

def checkResult(d, text):
    try:
        d.find_element_by_link_text(text)
        print("账号密码error")
    except:
        print("right")


def loginTest():
    d = openBrowser()
    openUrl(d,url)
    ele_dict = {'text_id':login_text,'user_id':'id_account_1','pwd_id':'id_password_1','login_id':'login_btn'}
    account_dict = {'uname':account,'pwd':pwd}
    ele_tuple = findElement(d, ele_dict)
    sendVals(ele_tuple,account_dict)
    checkResult(d,'账号格式不正确')

    ele_login = getEleTimes(d, 10, lambda d: d.find_element_by_link_text(login_text))
    ele_login.click()

    account_ele = d.find_element_by_id('id_account_1')
    account_ele.send_keys('')
    account_ele.clear()
    account_ele.send_keys(account)

    pwd_ele = d.find_element_by_id('id_password_1')
    pwd_ele.clear()
    pwd_ele.send_keys(pwd)
    d.find_element_by_id('login_btn').click()

    try:
        d.find_element_by_link_text('账号格式不正确')
        print("账号密码正确")
    except:


