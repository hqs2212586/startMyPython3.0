# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from multiprocessing import Process
import time

def task(name):
    print('%s 第一次' % name)
    time.sleep(1)
    print('%s 第二次' % name)
    time.sleep(1)
    print('%s 第三次' % name)


if __name__ == '__main__':
    for i in range(3):
        p = Process(target=task, args=('进程%s' % i, ))
        p.start()
"""
进程0 第一次
进程1 第一次
进程2 第一次
进程0 第二次
进程1 第二次
进程2 第二次
进程0 第三次
进程1 第三次
进程2 第三次
"""
# 以上输出效果和程序设想完全不同，这是因为并发运行,效率高,但竞争同一打印终端，谁抢到了谁打印。


from multiprocessing import Process, Lock
import time

def task(name, mutex):
    mutex.acquire()   # 上锁，哪个进程抢到锁，就一直给他运行
    print('%s 第一次' % name)
    time.sleep(1)
    print('%s 第二次' % name)
    time.sleep(1)
    print('%s 第三次' % name)
    mutex.release()   # 解锁


if __name__ == '__main__':
    mutex = Lock()   # 只实例化一次，并传给子进程，要保证所有进程用同一把锁
    for i in range(3):
        p = Process(target=task, args=('进程%s' % i, mutex))  # 传递给子进程的锁
        p.start()
"""
进程0 第一次
进程0 第二次
进程0 第三次
进程1 第一次
进程1 第二次
进程1 第三次
进程2 第一次
进程2 第二次
进程2 第三次
"""
# 由上可见，互斥锁的原理，就是把并发改成串行，降低了效率，但保证了数据安全不错乱