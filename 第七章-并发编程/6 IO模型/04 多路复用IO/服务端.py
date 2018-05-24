# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from socket import *
import select

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1',8093))
server.listen(5)
server.setblocking(False)
print('starting...')

rlist=[server,]   # 存收消息套接字
wlist=[]          # 存发消息套接字
wdata={}

while True:
    # 第三个空列表代表出异常的列表，0.5代表超时时间——每0.5秒问一次
    rl,wl,xl=select.select(rlist,wlist,[],0.5)
    print(wl)
    for sock in rl:       # 处理读列表
        if sock == server:
            conn,addr=sock.accept()   # 建成链接
            rlist.append(conn)      # 加入列表
        else:
            try:
                data=sock.recv(1024)
                if not data:
                    sock.close()
                    rlist.remove(sock)
                    continue
                wlist.append(sock)  # 写列表加入套接字
                wdata[sock]=data.upper()  # 保存套接字对应的数据
            except Exception:
                sock.close()   # 关闭没用链接
                rlist.remove(sock)   # 清掉监测列表rlist中

    for sock in wl:   # wl有值之后
        sock.send(wdata[sock])  # 执行send操作
        wlist.remove(sock)      # 从监测列表wlist删除sock
        wdata.pop(sock)         # 因为已经发完，从wdata删除记录

server.close()