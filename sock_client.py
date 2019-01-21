#!/usr/bin/python
# encoding = UTF-8

import socket
import time

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('127.0.0.1',6876))

while True:
    cmd = raw_input("Send to server:").strip()
    if len(cmd) == 0:
        continue
    c.sendall(cmd)
    data = c.recv(1024)
    print data
    time.sleep(1)
c.close()
    
