# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 解决重启服务端时，服务端仍存在四次挥手的time_wait状态占用地址的情况：
# 方法一：加入一条socket配置，重用ip和端口
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  # 在bind前，启动关闭服务端时，系统端口没有回收，可以重用端口
# 方法二：调整linux内核参数
"""
在 /etc/sysctl.conf文件中添加：
net.ipv4.tcp_syncookies = 1  # 表示开启SYN Cookies，启用cookies来处理，可防范少量SYN攻击，默认为0，表示关闭
net.ipv4.tcp_tw_reuse = 1   # 表示开启重用。允许将TIME-WAIT sockets重新用于新的TCP连接，默认为0，表示关闭
net.ipv4.tcp_tw_recycle = 1  #表示开启TCP连接中TIME-WAIT sockets的快速回收，默认为0，表示关闭
net.ipv4.tcp_fin_timeout = 30   # 修改系统默认的TIMEOUT时间

执行 /sbin/sysctl -p让参数生效
"""

phone.bind(('127.0.0.1', 8080))
phone.listen(5)  # 最大挂起的链接数
print('starting...')
conn, client_addr = phone.accept()
print(client_addr)

while True:  # 通信循环
    try:
        data = conn.recv(1024)  # 客户端发出空消息，服务端没有收到
        if not data:break #  # 适用与Linux操作系统
        print('客户端数据', data)

        conn.send(data.upper())
    except ConnectionResetError: # 适用于windiws的操作系统
        break

conn.close()
phone.close()

