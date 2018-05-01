# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 函数化改写
from socket import *
from multiprocessing import Process


def talk(conn):
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
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)  # 链接循环
    server.bind((ip, port))
    server.listen(5)

    while True:
        conn, address = server.accept()   # 主进程一直建链接
        p = Process(target=talk, args=(conn,))  # 注意conn参数传入
        p.start()

    server.close()


if __name__ == '__main__':
    server('127.0.0.1', 9001)