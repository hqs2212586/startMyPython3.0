# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import socket

"""
需要服务端一直提供服务，
"""
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1', 8080))
phone.listen(5)  # 最大挂起的链接数

print('starting...')
"""
需要服务端一直提供服务，再添加一个循环。服务端的工作主要是：1、建立链接；2、通信
需要注意的是：服务端可以一直提供服务，但是不能并发。只有等前一个链接断了后，下一个客户端才能链接
"""
while True:  # 链接循环
    # 创建链接
    conn, client_addr = phone.accept()
    print(client_addr)

    while True:  # 通信循环
        try:
            data = conn.recv(1024)
            if not data:break
            print('客户端数据', data)

            conn.send(data.upper())
        except ConnectionResetError:
            break

    conn.close()

phone.close()

