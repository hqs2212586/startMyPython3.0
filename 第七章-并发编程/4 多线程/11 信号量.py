# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
信号量也是一把锁，可以指定信号量为5，对比互斥锁同一时间只能有一个任务抢到锁去执行，信号量同一时间可以有5个任务拿到锁去执行。
"""
# from threading import Thread, Semaphore, currentThread
# import time, random
#
# sm = Semaphore(3)    # 定义出坑的个数
#
# def task():
#     sm.acquire()
#     print("%s in" % currentThread().getName())
#     sm.release()
#     with sm:
#         print("%s in " % currentThread().getName())
#         time.sleep(random.randint(1, 3))
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = Thread(target=task)
#         t.start()
"""
Thread-1 in 
Thread-2 in 
Thread-3 in 
Thread-5 in 
Thread-6 in 
Thread-4 in 
Thread-7 in 
Thread-8 in 
Thread-9 in 
Thread-10 in 
"""

from threading import Thread,Semaphore
import threading
import time

def func():
    sm.acquire()
    print('%s get sm' %threading.current_thread().getName())
    time.sleep(3)
    sm.release()

if __name__ == '__main__':
    sm=Semaphore(5)
    for i in range(23):
        t=Thread(target=func)
        t.start()