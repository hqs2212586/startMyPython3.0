# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于网络通讯的，基于TCP协议的一个套接字

phone.connect(('127.0.0.1', 8080))

while True:
    # 1、发命令
    cmd = input('>>:').strip()
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))

    # 2、命令结果拿到，并打印
    data = phone.recv(1024)
    """1024是一个坑，未来需要修复"""
    print(data.decode('utf-8'))

phone.close()
