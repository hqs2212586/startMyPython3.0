# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 使用时，可以一个程序运行多次，这是多个不同的in
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(("127.0.0.1", 8091))

while True:
    msg = input(">>").strip()
    if not msg:continue
    client.send(msg.encode("utf-8"))
    data = client.recv(1024)
    print(data.decode("utf-8"))

client.close()