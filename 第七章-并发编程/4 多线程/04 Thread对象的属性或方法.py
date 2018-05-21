# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


# 需要注意的是线程没有子线程的概念，线程都是属于进程的
from threading import Thread, currentThread   # 得到线程对象的方法
from threading import active_count    # 得到活跃进程数
from threading import enumerate   # 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
import time

def task():
    print("%s is running" % currentThread().getName())   # 对象下有一个getName()方法
    time.sleep(2)
    print("%s is done" % currentThread().getName())

if __name__ == '__main__':
    # getName()方法返回线程名
    # t = Thread(target=task, name='子线程1')
    # t.start()
    # print("主进程", currentThread().getName())
    """
    子线程1 is running
    主进程 MainThread
    子线程1 is done
    """
    # setName()方法设置线程名
    # t = Thread(target=task, name='子线程1')
    # t.start()
    # t.setName('儿子线程1')   # 修改进程名称
    # currentThread().setName("主线程")   # 设置主线程名称（默认是MainThread）
    # print(t.isAlive())    # 判断线程是否存活
    # print("主进程", currentThread().getName())
    """
    子线程1 is running
    True
    主进程 主线程
    儿子线程1 is done
    """
    # t = Thread(target=task, name='子线程1')
    # t.start()
    # t.setName('儿子线程1')  # 修改进程名称
    # t.join()  # 主线程等子进程运行完毕再执行
    # currentThread().setName("主线程")  # 设置主线程名称（默认是MainThread）
    # print(t.isAlive())  # 判断线程是否存活
    # print("主进程", currentThread().getName())
    """
    子线程1 is running
    儿子线程1 is done
    False
    主进程 主线程
    """
    # 测试threading.active_count方法
    # t = Thread(target=task, name='子线程1')
    # t.start()
    # print(active_count())
    """
    子线程1 is running
    2
    子线程1 is done
    """
    # 对上面改写添加一个join()
    # t = Thread(target=task, name='子线程1')
    # t.start()
    # t.join()   # 运行完才执行主线程，因此后面打印的活跃线程数是一个
    # print(active_count())
    """
    子线程1 is running
    子线程1 is done
    1
    """
    # threading.enumerate()方法：返回一个包含正在运行的线程的list
    t = Thread(target=task, name='子线程1')
    t.start()
    print(enumerate())
    """
    子线程1 is running
    [<_MainThread(MainThread, started 4320744256)>, <Thread(子线程1, started 123145383735296)>]
    子线程1 is done
    """