# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import socket
import subprocess

ip_port = ('127.0.0.1', 9001)  # 元组
bufsize = 1024

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(ip_port)

while True:
    # 收消息
    cmd, addr = udp_server.recvfrom(bufsize)
    print("用户命令----->", cmd)

    # 逻辑处理
    res = subprocess.Popen(cmd.decode('utf-8'),
                           shell=True,
                           stderr=subprocess.PIPE,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE)
    stdout = res.stdout.read()
    stderr = res.stderr.read()

    # 发消息
    udp_server.sendto(stderr, addr)
    udp_server.sendto(stdout, addr)

udp_server.close()