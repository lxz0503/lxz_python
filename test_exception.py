try:
    open('a.txt','r')
except BaseException as e:
    print(e)
