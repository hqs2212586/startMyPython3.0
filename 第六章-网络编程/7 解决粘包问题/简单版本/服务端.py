# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import time
import socket
import subprocess
import struct
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 9003))  # bind()内为元组，0-65535：0-1024供操作系统使用
server.listen(5)

print('starting...')
while True:
    conn, client_addr = server.accept()
    print(client_addr)

    while True:  # 通讯循环
        try:
            """1、收命令"""
            cmd = conn.recv(8096)
            if not cmd:break
            """2、拿到结果"""
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            """3、命令结果返回客户端"""
            # 第一步：制作固定长度的报头
            header_dic = {
                'filename': 'a.txt',
                'md5': 'xxdxxx',
                'total_size': len(stdout) + len(stderr)
            }
            header_json = json.dumps(header_dic)  # dump和dumps的区别
            header_bytes = header_json.encode('utf-8')

            # 第二步：先发送报头的长度
            conn.send(struct.pack('i', len(header_bytes)))
            # 第三步：将报头发给客户端
            conn.send(header_bytes)
            # conn.send(str(total_size).encode('utf-8'))  # 整型转换为字符串，编码后发出

            # 第四步：发送真实数据
            # conn.send(stdout+stderr)  # 由于粘包原理可优化改写如下
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionResetError:
            break
    conn.close()

server.close()