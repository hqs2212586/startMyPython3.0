# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于网络通讯的，基于TCP协议的一个套接字

phone.connect(('127.0.0.1', 8080))  # 服务端先启动后启动客户端

while True:  # 通信循环
    msg = input('>>:').strip()  # msg=''
    # 修改办法
    if not msg:continue  # 输入空，不发送消息
    phone.send(msg.encode('utf-8'))  # phone.send(b'')
    # print('has send') # 定位不能发空的缘故
    data = phone.recv(1024)  # 服务端没有回消息，因此收不到消息
    print(data.decode('utf-8'))

phone.close()
