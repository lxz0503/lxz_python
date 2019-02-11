#!/usr/bin/env python
import codecs


def getWebInfo(path):
    webinfo = {}
    config = open(path)
    for line in config:
        result = [ele.strip() for ele in line.split('=')]
        print(result)
        webinfo.update(dict([result]))
    return webinfo
	

def getUserInfo(path):
    user_info = []
    config = codecs.open(path,'r', 'utf-8')
    for line in config:
        user_dict = {}
        result = [ele.strip() for ele in line.split(' ')]
        for r in result:
            account = [ele.strip() for ele in r.split('=')]
            user_dict.update(dict([account]))
    user_info.append(user_dict)
    return user_info


if __name__ == '__main__':
    webinfo = getWebInfo(r'F:\Pycharm\Selenium_Xiaozhan\lxz_python\webinfo.txt')
    for key in webinfo:
        print(key,webinfo[key])
    user_info = getUserInfo(r'F:\Pycharm\Selenium_Xiaozhan\lxz_python\userinfo.txt')
    for l in user_info:
        print(l)