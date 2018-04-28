# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import socket
# 1、买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于网络通讯的，基于TCP协议的一个套接字
# print(phone)
"""
<socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 0)>
"""

# 2、绑定手机卡
phone.bind(('127.0.0.1', 9001))  # 本地回环地址,  端口0-65535（0-1024归系统使用）

# 3、开机
phone.listen(5)  # 最大挂起的链接数

# 4、等电话链接
print('starting...')
# res = phone.accept()  # 程序卡在这一步
# print(res)  # res包含链接对象
"""
starting...
===》
(<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8080), raddr=('127.0.0.1', 55868)>, ('127.0.0.1', 55868))
"""
# 改写分拆两个元组元素
conn, client_addr = phone.accept()
print(conn)
print(client_addr)
print('got a new connection from %s' % (client_addr, ))
"""
<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8080), raddr=('127.0.0.1', 55925)>
('127.0.0.1', 65197)
got a new connection from ('127.0.0.1', 65197)
"""

# 5、收发消息
data = conn.recv(1024)  # 1、单位是bytes 2、1024代表接收数据的最大数是1024个bytes
print('客户端数据', data)

conn.send(data.upper())  # 数据修改为大写后发送

# 6、挂电话
conn.close()

# 7、关机
phone.close()
"""
客户端数据 b'hello'
"""