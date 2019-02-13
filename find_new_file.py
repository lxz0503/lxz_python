#!/usr/bin/env python
#encoding=UTF-8

import os

result_dir = 'D:\\Pycharm\\test_xiaozhan\\lxz_python'
lists = os.listdir(result_dir)
#sort files based on time
lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
print('the new file is: ' + lists[-1])
new_file = os.path.join(result_dir, lists[-1])
print(new_file)


