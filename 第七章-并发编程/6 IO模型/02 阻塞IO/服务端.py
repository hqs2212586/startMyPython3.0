# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# from socket import *
#
# server = socket(AF_INET, SOCK_STREAM)
# server.bind(('127.0.0.1', 8093))
# server.listen(5)
#
# while True:  # 链接循环
#     print("starting....")
#     conn, addr = server.accept()   # 等对方来连————阻塞（操作系统会将cpu拿走）
#     print(addr)
#
#     while True:  # 通讯循环
#         try:
#             data = conn.recv(1024)  # 等待收消息————阻塞
#             if not data: break
#             conn.send(data.upper())
#         except ConnectionResetError:
#             break
#
#     conn.close()
# server.close()

"""
blocking IO的特点就是在IO执行的两个阶段（等待数据和拷贝数据两个阶段）都被block了
"""
from socket import *
from threading import Thread

def communicate(conn):
    while True:  # 通讯循环
        try:
            data = conn.recv(1024)  # 等待收消息————阻塞
            if not data: break
            conn.send(data.upper())
        except ConnectionResetError:
            break

    conn.close()

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8093))
server.listen(5)

while True:  # 链接循环
    print("starting....")
    conn, addr = server.accept()   # 等对方来连————阻塞（操作系统会将cpu拿走）
    print(addr)

    t=Thread(target=communicate, args=(conn,))
    t.start()

server.close()

"""
一个简单的解决方案：

    在服务器端使用多线程（或多进程）。多线程（或多进程）的目的是让每个连接都拥有独立的线程（或进程），
这样任何一个连接的阻塞都不会影响其他的连接。

该方案问题：
    开启多进程或都线程的方式，在遇到要同时响应成百上千路的连接请求，则无论多线程还是多进程都会严重占据系统资源，
降低系统对外界响应效率，而且线程与进程本身也更容易进入假死状态。
"""

"""
改进方案：
    很多程序员可能会考虑使用“线程池”或“连接池”。“线程池”旨在减少创建和销毁线程的频率，
其维持一定合理数量的线程，并让空闲的线程重新承担新的执行任务。“连接池”维持连接的缓存池，尽量重用已有的连接、
减少创建和关闭连接的频率。这两种技术都可以很好的降低系统开销，都被广泛应用很多大型系统，如websphere、tomcat和各种数据库等。

改进后方案其实也存在着问题：
    “线程池”和“连接池”技术也只是在一定程度上缓解了频繁调用IO接口带来的资源占用。而且，所谓“池”始终有其上限，
当请求大大超过上限时，“池”构成的系统对外界的响应并不比没有池的时候效果好多少。所以使用“池”必须考虑其面临的响应规模，
并根据响应规模调整“池”的大小。（规模过大，反而会降低效率）
"""

"""
对应上例中的所面临的可能同时出现的上千甚至上万次的客户端请求，“线程池”或“连接池”或许可以缓解部分压力，但是不能解决所有问题。
总之，多线程模型可以方便高效的解决小规模的服务请求，但面对大规模的服务请求，多线程模型也会遇到瓶颈，可以用非阻塞接口来尝试解决这个问题。
"""