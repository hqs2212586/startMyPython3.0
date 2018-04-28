# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import time
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 9002))

# 使用了优化方法（Nagle算法），将多次间隔较小且数据量小的数据，合并成一个大的数据块，然后进行封包。
client.send('hello'.encode('utf-8'))
# time.sleep(1)  # 休息一秒看是否还粘包
time.sleep(5)
client.send('world'.encode('utf-8'))
