# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 线程的互斥锁和进程类似，都是将并行改为串行。牺牲数据保证数据安全。
# 区别是：一个进程下的多个线程，不依赖其他手段就可以实现数据的共享，共享就会带来竞争，可能会将数据改乱。
# import time
# from threading import Thread
#
# n = 100
#
#
# def task():
#     global n
#     temp = n
#     time.sleep(0.1)
#     n = temp - 1
#
#
# if __name__ == '__main__':
#     t_l = []
#     for i in range(100):
#         t = Thread(target=task)
#         t_l.append(t)
#         t.start()
#
#     for t in t_l:
#         t.join()
#
#     print("主线程", n)
"""
主线程 99
"""
# 结果是99不是0 ：这是因为100个线程在一个进程内，第一个线程启动，查看到n=100后，线程睡眠0.1秒。
# 这个时间已经足够后面这100个线程启动并读取到n=100，并都停在睡眠0.1秒这一步，睡完后，就依次执行100-1,因此得到n=99。

# 现在这个并发虽然效率高，但是数据不安全。需要引入互斥锁。
import time
from threading import Thread
from threading import Lock

n = 100


def task():
    global n
    mutex.acquire()   # 抢一把锁，其他线程都卡在这一步，等前一个线程释放这把锁，效率严重降低
    temp = n
    time.sleep(0.1)
    n = temp - 1
    mutex.release()   # 释放锁


if __name__ == '__main__':
    mutex = Lock()
    t_l = []
    for i in range(100):
        t = Thread(target=task)
        t_l.append(t)
        t.start()

    for t in t_l:
        t.join()

    print("主线程", n)
"""
主线程 0
"""