# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
信号量也是一把锁，可以指定信号量为5，对比互斥锁同一时间只能有一个任务抢到锁去执行，信号量同一时间可以有5个任务拿到锁去执行。
"""
from threading import Thread, Semaphore, currentThread
import time, random

sm = Semaphore(3)    # 定义出坑的个数

def task():
    # sm.acquire()
    # print("%s in" % currentThread().getName())
    # sm.release()
    with sm:
        print("%s in " % currentThread().getName())
        time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=task)
        t.start()