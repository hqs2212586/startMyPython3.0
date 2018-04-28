# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import time
import socket
import struct
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 9003))

while True:
    """1、发命令"""
    cmd = input('>>: ').strip()
    if not cmd:continue
    client.send(cmd.encode('utf-8'))
    """2、拿结果"""
    # 第一步：先收报头长度
    obj= client.recv(4)  # 接收四个bytes
    header_size = struct.unpack('i', obj)[0]
    # 第二步：再收报头
    header_bytes = client.recv(header_size)

    # 第三步：从报头中解析出对真实数据的描述信息（数据长度）
    header_json = header_bytes.decode('utf-8')
    header_dic = json.loads(header_json)
    print(header_dic)
    total_size = header_dic['total_size']

    # 第四步：接收真实的数据
    recv_size = 0
    recv_data = b''
    while recv_size < total_size:
        res = client.recv(1024)    # 最大不能超过操作系统缓存大小，一次收不完，多次收
        recv_data += res
        recv_size += len(res)  # 最后一次收的时候将不是1024,未来如果要查看进度的时候有问题

    print(recv_data.decode('utf-8'))

client.close()
