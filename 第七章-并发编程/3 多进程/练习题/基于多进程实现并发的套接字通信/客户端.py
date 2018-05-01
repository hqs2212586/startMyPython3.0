# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 运行一次启动一个客户端进程
# 这种情况还是存在问题：启动多个进程后，本机操作系统会崩溃掉
from socket import *


client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 9001))

while True:
    msg = input(">>: ").strip()
    if not msg:continue

    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))
