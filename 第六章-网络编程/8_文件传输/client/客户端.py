# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import time
import socket
import struct
import json

download_dir = '/Users/hqs/PycharmProjects/startMyPython3.0/第六章-网络编程/8_文件传输/client/download'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 9001))

while True:
    """1、发命令"""
    cmd = input('>>: ').strip()   # get a.txt软件自定义命名标准
    if not cmd:continue
    client.send(cmd.encode('utf-8'))
    """2、以写的方式打开新文件，接收服务端发来的文件内容写入新文件中"""
    # 第一步：先收报头长度
    header = client.recv(4)
    header_size = struct.unpack('i', header)[0]

    # 第二步：收取报头
    header_bytes = client.recv(header_size)

    # 第三步：从报头中解析出对真实数据的描述信息（数据长度）
    header_json = header_bytes.decode('utf-8')
    header_dic = json.loads(header_json)
    print(header_dic)
    total_size = header_dic['file_size']
    filename = header_dic['filename']

    # 第四步：接收真实的数据
    with open('%s/%s' % (download_dir, filename), 'wb') as f:  # 在同一台机器上，相同的路径会导致文件清空,需要指定目录
        recv_size = 0
        # recv_data = b''   拼接字符串不需要了
        while recv_size < total_size:
            line = client.recv(1024)    # 最大不能超过操作系统缓存大小，一次收不完，多次收
            f.write(line)   # 一边收一边写
            recv_size += len(line)  # 最后一次收的时候将不是1024,未来如果要查看进度的时候有问题
            print('总大小: %s 已下载：%s' % (total_size, recv_size))
client.close()
