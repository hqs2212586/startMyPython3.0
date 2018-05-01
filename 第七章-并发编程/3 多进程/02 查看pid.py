# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from multiprocessing import Process
import time,os

def task():
    print('%s is running, parent id is <%s>' % (os.getpid(), os.getppid()))   # 进程和父进程查看方式
    time.sleep(3)
    print("%s is done, parent id is <%s>" % (os.getpid(), os.getppid()))

if __name__ == '__main__':
    # p = Process(target=task, args=('子进程1',))   # 报错提示去掉参数TypeError: task() takes 0 positional arguments but 1 was given
    p = Process(target=task, )
    p.start()   # 给操作系统发送一个信号
    print('主进程', os.getpid(), 'pycharm ID', os.getppid())
"""
主进程 713 pycharm ID 504
714 is running, parent id is <713>
714 is done, parent id is <713>
"""