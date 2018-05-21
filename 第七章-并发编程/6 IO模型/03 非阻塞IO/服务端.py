# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8093))
server.listen(5)
server.setblocking(False)   # 默认是True:阻塞，改为False:非阻塞
print("starting....")

rlist = []
wlist = []
while True:  # 链接循环
    try:
        conn, addr = server.accept()  # 问操作系统有没有来链接
        rlist.append(conn)
        print(rlist)
    except BlockingIOError:   # 没有链接捕捉异常
        # print("干其他活")
        # 收消息
        del_rlist = []
        for conn in rlist:
            try:
                data = conn.recv(1024)
                if not data:
                    del_rlist.append(conn)
                    continue
                # conn.send(data.upper())  # 传输的内容很多时，send也会有阻塞
                wlist.append((conn, data.upper()))  # 存放套接字及套接字准备发送的内容
            except BlockingIOError:
                continue
            except Exception:
                conn.close()
                del_rlist.append(conn)

        # 发消息
        del_wlist = []
        for item in wlist:
            try:
                conn = item[0]
                data = item[1]
                conn.send(data)
                del_wlist.append(conn)  # 正常，走到这一步
            except BlockingIOError:   # 没让发抛出异常
                pass

        for item in del_wlist:
            wlist.remove(item)

        for conn in del_rlist:
            rlist.remove(conn)

server.close()

"""
服务端不停建链接，解决了阻塞不能建链接的问题,
能够在等待任务完成的时间里干其他活了（包括提交其他任务，也就是 “后台” 可以有多个任务在“”同时“”执行

缺点：
1. 循环调用recv()将大幅度推高CPU占用率；这也是我们在代码中留一句time.sleep(2)的原因,否则在低配主机下极容易出现卡机情况
2. 任务完成的响应延迟增大了，因为每过一段时间才去轮询一次read操作，而任务可能在两次轮询之间的任意时间完成。这会导致整体数据吞吐量的降低。

解决方案：
    方案中recv()更多的是起到检测“操作是否完成”的作用，实际操作系统提供了更为高效的检测“操作是否完成“作用的接口，例如select()多路复用模式，可以一次检测多个连接是否活跃。
"""