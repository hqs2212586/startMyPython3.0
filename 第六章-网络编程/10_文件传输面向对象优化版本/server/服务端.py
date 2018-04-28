# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import time
import socket
import subprocess
import struct
import os
import json

share_dir = "/Users/hqs/PycharmProjects/startMyPython3.0/第六章-网络编程/9_文件传输函数优化版本/server/share"


def get(conn, cmds):
    filename = cmds[1]

    """3、以读的方式打开文件，读取文件内容发送给客户端"""
    # with open(filename, 'rb') as f:  直接读文件传输会有粘包问题
    # 第一步：制作固定长度的报头
    header_dic = {
        'filename': filename,  # ''
        'md5': 'xxdxxx',
        'file_size': os.path.getsize(r'%s/%s' % (share_dir, filename))  # 文件大小
    }
    header_json = json.dumps(header_dic)
    header_bytes = header_json.encode('utf-8')

    # 第二步：发送报头的长度
    conn.send(struct.pack('i', len(header_bytes)))

    # 第三步：再发报头
    conn.send(header_bytes)

    # 第四步：发送真实数据
    with open('%s/%s' % (share_dir, filename), 'rb') as f:
        # conn.send(f.read())   # 一下全读取，文件有几个T时会有问题
        for line in f:
            conn.send(line)  # 一行行发都会粘在一起，且节省内存


def put(conn, cmds):...


def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("127.0.0.1", 9001))  # bind()内为元组，0-65535：0-1024供操作系统使用
    server.listen(5)

    print('starting...')
    while True:
        conn, client_addr = server.accept()
        print(client_addr)

        while True:  # 通讯循环
            try:
                """1、收到客户端的命令"""
                res = conn.recv(8096)  # b'get a.txt'
                if not res:break
                """2、解析命令，提取相应命令参数"""
                cmds = res.decode('utf-8').split()  # ['get', 'a.txt']
                if cmds[0] == 'get':
                    get(conn, cmds)
                elif cmds[0] == 'put':
                    put(conn, cmds)


            except ConnectionResetError:
                break
        conn.close()

    server.close()


if __name__ == '__main__':
    run()
