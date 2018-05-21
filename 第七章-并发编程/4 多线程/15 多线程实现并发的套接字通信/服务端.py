# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from socket import *
from threading import Thread

# 通讯和建立链接分开，启动不同的线程，大家是并发执行。
def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
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
        t = Thread(target=communicate, args=(conn,))  # 建一个链接创一个线程
        t.start()
        # communicate(conn)

    server.close()


if __name__ == '__main__':
    server('127.0.0.1', 8091)   # 主线程

"""
这种解决方案的问题是：当客户端越来越多后，线程也会越来越多，会带来服务崩溃的问题。
"""
