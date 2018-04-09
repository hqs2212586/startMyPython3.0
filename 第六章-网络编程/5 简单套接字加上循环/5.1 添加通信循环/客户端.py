# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import socket
# 1、买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于网络通讯的，基于TCP协议的一个套接字
#print(phone)

# 2、拨号
phone.connect(('127.0.0.1', 8080))  # 服务端先启动后启动客户端

# 3、发、收消息
while True:  # 通信循环
    msg = input('>>:').strip()
    phone.send(msg.encode('utf-8'))
    data = phone.recv(1024)  # 收到服务端大写之后的字符
    print(data)

# 4、关闭
phone.close()
"""
>>:hello
b'HELLO'
>>:xiugeng
b'XIUGENG'
"""