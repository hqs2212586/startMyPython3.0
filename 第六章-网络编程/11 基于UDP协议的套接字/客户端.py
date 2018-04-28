# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('>>: ').strip()
    client.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))  # 发消息

    data, server_addr = client.recvfrom(1024)   # 收消息
    print(data, server_addr)

client.close()
