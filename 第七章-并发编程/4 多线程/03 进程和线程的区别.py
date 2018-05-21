# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


# 1、进程的开销远大于线程
import time
from multiprocessing import Process
from threading import Thread


def piao(name):
    print('%s piaoing' % name)
    time.sleep(2)
    print('%s piao end' % name)

if __name__ == '__main__':
    # p1 = Process(target=piao, args=('进程', ))
    # p1.start()
    """
    主线程
    进程 piaoing
    进程 piao end
    """


    t1 = Thread(target=piao, args=('线程', ))
    t1.start()
    """
    线程 piaoing
    主线程
    线程 piao end
    """
    print("主线程")
# 对比可知，线程开销远小于进程，因为进程需要申请内存空间。



# 2、同一进程内的多个线程共享该进程的地址空间
from threading import Thread
from multiprocessing import Process

n = 100
def task():
    global n
    n = 0

if __name__ == '__main__':
    """进程验证：
    p1 = Process(target=task,)
    p1.start()   # 会把子进程的n改为了0，看是否影响主进程
    p1.join()
    print("主进程", n)   # 主进程 100
    # 由此可见进程间是隔离的，子进程变量修改不影响主进程
    """

    """线程验证"""
    t1 = Thread(target=task, )
    t1.start()
    t1.join()
    print("主线程", n)   # 主线程 0


# 3、pid观察
from threading import Thread
from multiprocessing import Process, current_process  # current_process查看进程ID号
import os   # os.getpid()也可以查看进程ID

n = 100
def task():
    # print(current_process().pid)
    print('子进程PID:%s   父进程的PID：%s' % (os.getpid(), os.getppid()))

if __name__ == '__main__':
    p1 = Process(target=task,)
    p1.start()

    # print("主线程", current_process().pid)
    print("主线程", os.getpid())
"""
主线程 6455
子进程PID:6456   父进程的PID：6455
"""


# 4、研究线程
from threading import Thread
import os   # os.getpid()也可以查看进程ID

n = 100
def task():
    # print(current_process().pid)
    print('线程的进程 PID:%s' % os.getpid())

if __name__ == '__main__':
    t1 = Thread(target=task,)
    t1.start()

    # print("主线程", current_process().pid)
    print("主线程", os.getpid())
"""说明两个线程是同一个进程：
线程的进程 PID:6493
主线程 6493
"""