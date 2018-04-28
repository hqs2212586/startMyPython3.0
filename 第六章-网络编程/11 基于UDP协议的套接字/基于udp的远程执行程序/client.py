# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import socket

ip_port = ('127.0.0.1', 9001)
bufsize=1024

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input(">>: ").strip()
    udp_client.sendto(msg.encode('utf-8'), ip_port)  # 发消息

    data, server_addr = udp_client.recvfrom(bufsize)
    print(data, server_addr)

udp_client.close()