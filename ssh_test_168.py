"""this is for ssh test """

#!/usr/bin/python
#coding=utf-8

import sys,re
from pexpect import pxssh

def ssh_test(server,username,password):
    
    try:
        s = pxssh.pxssh(timeout=6)
        s.login(server, username, password)
        s.logfile=sys.stdout #print your output on the screen
        #logFileId=open("logfile.txt",'w') #record test log to a file
        #s.logfile=logFileId
        s.sendline("cat /proc/version")
        s.prompt()
		s.sendline("cd /home/windriver/SPIN")
		s.prompt()
		s.sendline("mkdir xiaozhan")
		s.prompt()
        print s.before
    except pxssh.ExceptionPxssh as e:
        print "pxssh failed to login"
        print e
		s.logout()

def main():
    server = "128.224.163.8"
    username = "windriver"
    password = "windriver"
    ssh_test(server,username,password)



if __name__ == "__main__":
    main()
