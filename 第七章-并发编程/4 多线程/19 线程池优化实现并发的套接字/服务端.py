# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


"""
原先多线程解决方案的问题是：当客户端越来越多后，线程也会越来越多，会带来服务崩溃的问题。
    不应该随着客户端数量增加不断地增加线程，需要基于线程池实现，限制线程数量
"""
from socket import *
from concurrent.futures import ThreadPoolExecutor


def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            # if not data:continue   # 这里卡了很久，需要注意,这种情况下关闭客户端，线程池没有减少
            # if data.decode('utf-8') == 'q':break  # 测试，这种情况下，线程池减少，新进程加入进程池
            if not data:break
            conn.send(data.upper())

        except ConnectionResetError:
            break
    conn.close()


def server(ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        conn, addr = server.accept()   # 建链接
        pool.submit(communicate, conn)

    server.close()


if __name__ == '__main__':
    pool = ThreadPoolExecutor(2)  # 一般写机器可承受的范围内
    server('127.0.0.1', 8092)   # 主线程

