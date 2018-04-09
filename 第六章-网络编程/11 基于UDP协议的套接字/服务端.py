# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# import socket
from socket import *   # 尽量少用这种导入方式，会将所有名字加入名称空间，容易导致重复
# server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # 可以看到需要引用的socket的模块非常多。改用from socket import *导入
server = socket(AF_INET, SOCK_DGRAM)  # SOCK_STREAM指的流式协议，SOCK_DGRAM指得是数据报协议（但凡发数据，就已经是完整的数据报）
server.bind(('127.0.0.1', 8080))

# server.listen(5)  # 挂起的链接数，TCP协议需要，UDP不需要

# while True:
#     conn, addr = server.accept()  # 用来建立链接，UDP不需要

while True:
    data, client_addr = server.recvfrom(1024)   # 收消息
    print(data)

    server.sendto(data.upper(), client_addr)    # 发消息，取收消息的地址
server.close()
