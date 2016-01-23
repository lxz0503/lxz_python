#!/usr/bin/python
# encoding = UTF-8

import socket
import time,os
from thread import *

### Function for handling connections. This will be used to create threads
def clientThread(conn):     
####### infinite loop so that function do not terminate and thread do not end.
    while True:         
        data = conn.recv(1024)    
        if not data: 
            break 
#       reply = 'OK...' + data
        reply = os.popen(data).read()
        if len(reply) != 0:     
            conn.sendall(reply) 
        else:
            conn.sendall("no reply for this command")   
    conn.close()
######## main 函数 #################################
if __name__ == "__main__":
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',6876))  #端口可以更换，如果报错
    s.listen(10)
###########  now keep talking with the client ######
    while 1:
        conn, addr = s.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])     
#### start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
        start_new_thread(clientThread ,(conn,))
 
    s.close()


    
