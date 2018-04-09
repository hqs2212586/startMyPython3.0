# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import socket
# 1、买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于网络通讯的，基于TCP协议的一个套接字
# 2、绑定手机卡
phone.bind(('127.0.0.1', 8080))  # 本地回环地址,  端口0-65535（0-1024归系统使用）
# 3、开机
phone.listen(5)  # 最大挂起的链接数（TCP协议需要）
# 4、等电话链接
print('starting...')
conn, client_addr = phone.accept()  # accept是建立链接
print(client_addr)  # 客户端一启动打印 （'127.0.0.1',56641）

# 5、收发消息
while True:  # 通信循环
    data = conn.recv(1024)  # 1、单位是bytes 2、1024代表接收数据的最大数是1024个bytes
    print('客户端数据', data)

    conn.send(data.upper())  # 数据修改为大写后发送
# 6、挂电话
conn.close()
# 7、关机
phone.close()
"""
starting...
('127.0.0.1', 56641)
客户端数据 b'hello'
客户端数据 b'xiugeng'
"""
