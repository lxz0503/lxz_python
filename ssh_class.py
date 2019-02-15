"""this is for ssh test """

# !/usr/bin/python

import sys, re
from pexpect import pxssh
class SSH(object):
    def __init__(self, host_name, user_name, password):
        self.host_name = host_name
        self.user_name = user_name
        self.password = password
        self.s = None

    def connect(self):
        try:
            s = pxssh.pxssh(timeout=60*60)
            s.login(server=self.host_name, username=self.user_name, password=self.password)
            s.logfile = sys.stdout
            self.s = s
        except pxssh.ExceptionPxssh as e:
            print(e)

    def disconnect(self):
        self.s.logout()

    def send_cmd(self, cmd):
        self.s.sendline(cmd)
        self.s.prompt()
        print(self.s.before)
        return self.s.before


def real_ssh_test(ssh_config, cmd):
    ssh = SSH(ssh_config['host_name'],ssh_config['username'],ssh_config['password'])
    ssh.connect()
    for i in cmd:
        ssh.send_cmd(i)
    ssh.disconnect()


if __name__ == "__main__":
    ssh_config = {'host_name':'128.224.163.8','username':'windriver','password':'windriver'}
    cmd = ['uname -a','cat /proc/version']
    real_ssh_test(ssh_config,cmd)
