# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import time
import socket
import subprocess
import struct

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
            cmd = conn.recv(8096)
            if not cmd:break
            """2、执行命令，拿到结果"""
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            """3、命令结果返回客户端"""
            # 第一步：制作固定长度的报头
            total_size = len(stdout) + len(stderr)  # 整型
            header = struct.pack('i', total_size)  # 隐患：struct的i 的取值区间是-2147483648~2147483648

            # 第二步：将报头发给客户端
            conn.send(header)
            # conn.send(str(total_size).encode('utf-8'))  # 整型转换为字符串，编码后发出

            # 第三步：发送真实数据
            # conn.send(stdout+stderr)  # 由于粘包原理可优化改写如下
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionResetError:
            break
    conn.close()

server.close()