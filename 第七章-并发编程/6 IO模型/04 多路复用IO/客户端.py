# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from socket import *
c=socket(AF_INET,SOCK_STREAM)
c.connect(('127.0.0.1',8093))

while True:
    msg=input('>>: ')
    if not msg:continue
    c.send(msg.encode('utf-8'))
    data=c.recv(1024)
    print(data.decode('utf-8'))