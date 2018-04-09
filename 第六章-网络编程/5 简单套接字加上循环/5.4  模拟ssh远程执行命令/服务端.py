# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import socket
import subprocess

"""
需要服务端一直提供服务，
"""
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) # 启动关闭服务端时，系统端口没有回收，可以重用端口
phone.bind(('127.0.0.1', 8080))
phone.listen(5)  # 最大挂起的链接数

print('starting...')

while True:  # 链接循环
    conn, client_addr = phone.accept()
    print(client_addr)

    while True:  # 通信循环
        try:
            # 1、收命令
            cmd = conn.recv(1024)
            if not cmd:break   # 适用于linux

            # 2、执行命令，拿到结果
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,  # 命令传过来的是bytes格式，按照客户端编码解码
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

            stdout = obj.stdout.read()  # 服务器系统运行结果，Linux 是utf-8
            stderr = obj.stderr.read()

            # 3、把命令的结果返回给客户端
            conn.send(stdout+stderr)  # 无论对错信息都返回，'+'会生成新的内存空间，效率低
            """+是未来需要优化的点"""
        except ConnectionResetError:    # 使用于windows
            break

    conn.close()

phone.close()

