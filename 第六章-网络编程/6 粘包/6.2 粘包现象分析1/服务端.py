# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import time
import socket
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 9002))  # bind()内为元组，0-65535：0-1024供操作系统使用
server.listen(5)

conn, addr = server.accept()

# res1 = conn.recv(1024)   # 第一次收
# print('第一次', res1)
# res2 = conn.recv(1024)   # 第二次收
# print('第二次', res2)
"""
第一次 b'helloworld'
第二次 b''
"""
# 发生了粘包现象

# 客户端在两次发包间，间隔了1秒，不再粘包
"""
第一次 b'hello'
第二次 b'world'
"""

# 客户端间隔五秒发送，服务端第一次仅接收一个字符，服务端发生粘包
res1 = conn.recv(1)   # 第一次收
print('第一次', res1)
res2 = conn.recv(1024)   # 第二次收
print('第二次', res2)
"""
第一次 b'h'
第二次 b'ello'
"""

# 客户端间隔5秒，服务端间隔6秒
# res1 = conn.recv(1)   # 第一次收 b'hello'
# print('第一次', res1)
# time.sleep(6)
# res2 = conn.recv(1024)   # 第二次收
# print('第二次', res2)
"""
第一次 b'h'
第二次 b'elloworld'
"""