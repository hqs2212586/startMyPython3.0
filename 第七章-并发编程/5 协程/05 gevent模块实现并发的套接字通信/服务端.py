# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 基于gevent实现
from gevent import monkey;monkey.patch_all()  # 标准写法，打补丁识别所有阻塞
#如果不想用money.patch_all()打补丁,可以用gevent自带的socket
# from gevent import socket
# s=socket.socket()
from gevent import spawn
from socket import *


def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())

        except ConnectionResetError:
            break
    conn.close()


def server(ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        conn, addr = server.accept()  # 建链接
        spawn(communicate, conn)

    server.close()


if __name__ == '__main__':
    g = spawn(server, '127.0.0.1', 8091)
    g.join()   # 如果不写这个，程序直接结束