#!/usr/bin/python
#coding=utf-8
""" this is used to capture output or log"""
import pexpect,os,sys
#method one start

#child=pexpect.spawn('ls -l')
#output=child.read()
#output=child.readlines()
#print output

#method one end

#a=pexpect.run('ls -l')
#print a

#b=os.system('ls -l')
#print b
print pexpect.__version__
cmd="ssh root@128.224.166.46"
s=pexpect.spawn(cmd,timeout=5)
logFileId=open("logfile.txt",'w')
s.logfile=logFileId
#s.setecho(False)
i=s.expect(['root@pek-xli3-d2 ',
             'password:',
             'Are you sure you want to continue connecting',
             pexpect.EOF,
             pexpect.TIMEOUT])
for i in range(5):
    if i==0:
        pass
    elif i==1:
        s.sendline("kernel")
        s.expect("root@pek-xli3-d2 ")
       # print s.before
       # print s.after
        print "aaaaa"
        break
    
    elif i==2:
        s.sendline("yes")
        s.expect("password:")
        s.sendline("kernel")
        s.expect("root@pek-xli3-d2 ")
        print "bbbbb"
        break
    elif i==3 or i==4:
        print "error"
#print "xiaozhan"
s.sendline("ifconfig")
s.expect("root@pek-xli3-d2 ")
s.sendline("ls -l")
s.expect("root@pek-xli3-d2 ")
#s.expect(")
#print s.before
#print s.after
#s.sendline("ls -l")
#s.expect("xiaozhan")
#print s.before
#print i
#print s.before
#print s.after
