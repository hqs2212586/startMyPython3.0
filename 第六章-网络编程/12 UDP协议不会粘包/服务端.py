# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from socket import *   # 尽量少用这种导入方式，会将所有名字加入名称空间，容易导致重复

# server = socket(AF_INET, SOCK_DGRAM)  # SOCK_STREAM指的流式协议，SOCK_DGRAM指得是数据报协议（但凡发数据，就已经是完整的数据报）
# server.bind(('127.0.0.1', 8080))
#
# res1 = server.recvfrom(1024)
# print('第一次：', res1)
#
# res2 = server.recvfrom(1024)
# print('第二次：', res2)
#
# server.close()
"""不会粘包
第一次： (b'hello', ('127.0.0.1', 57245))
第二次： (b'world', ('127.0.0.1', 57245))
"""
server = socket(AF_INET, SOCK_DGRAM)  # SOCK_STREAM指的流式协议，SOCK_DGRAM指得是数据报协议（但凡发数据，就已经是完整的数据报）
server.bind(('127.0.0.1', 8080))

res1 = server.recvfrom(1)  # 'hello'只收到'h',剩下的会丢失
print('第一次：', res1)

res2 = server.recvfrom(1024)
print('第二次：', res2)

server.close()
"""
第一次： (b'h', ('127.0.0.1', 52635))
第二次： (b'world', ('127.0.0.1', 52635))
"""