# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


"""
死锁： 是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，若无外力作用，它们都将无法推进下去。
      此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程
"""
from threading import Thread, Lock
import time

# 实例化两把锁
mutexA = Lock()
mutexB = Lock()


class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print("%s 拿到A锁" % self.name)

        mutexB.acquire()
        print("%s 拿到了B锁" % self.name)

        mutexB.release()
        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print("%s 拿到B锁" % self.name)
        time.sleep(0.1)   # 线程1在此休息0.1秒
        mutexA.acquire()
        print("%s 拿到了A锁" % self.name)

        mutexA.release()
        mutexB.release()

if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()   # 信号提交，就几乎立马启动了
"""程序输出下面内容后，卡住了
Thread-1 拿到A锁
Thread-1 拿到了B锁
Thread-1 拿到B锁
Thread-2 拿到A锁   ————》线程1睡着时，线程2拿到A锁，要去拿B锁，B锁在线程1手里，线程1睡完要去拿A锁，A锁在线程2手里，因此产生死锁。
"""
# 上述例子也说明：自己处理锁其实非常繁琐也非常危险，一定要在适当的时候考虑把锁释放掉。处理不当就会出现死锁，整个程序就会卡在原地。


"""
互斥锁只能acquire一次
"""
from threading import Thread, Lock

mutexA = Lock()

mutexA.acquire()
mutexA.release()


"""
递归锁：可以连续acquire多次，每acquire一次计数器加1；只要计数不为0，就不能被其他线程抢到（只有计数为0，才能被抢到acquire）
       在Python中为了支持在同一线程中多次请求同一资源，python提供了可重入锁RLock
"""
from threading import Thread, RLock
import time

"""链式赋值"""
mutexA=mutexB=RLock()   # 使用递归锁可以

class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()    # 递归锁计数器加1
        print("%s 拿到A锁" % self.name)

        mutexB.acquire()
        print("%s 拿到了B锁" % self.name)

        mutexB.release()   # 递归锁计数器减1
        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print("%s 拿到B锁" % self.name)
        time.sleep(1)   # 线程1在此休息0.1秒
        mutexA.acquire()
        print("%s 拿到了A锁" % self.name)

        mutexA.release()
        mutexB.release()    # 计数为0，其他线程可以抢acquire

if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()   # 信号提交，就几乎立马启动了
""" 第一个线程计数器为0 后，其他线程可以开始抢acquire，因此顺序是不固定的。
Thread-1 拿到A锁
Thread-1 拿到了B锁
Thread-1 拿到B锁
Thread-1 拿到了A锁
Thread-2 拿到A锁
Thread-2 拿到了B锁
Thread-2 拿到B锁
Thread-2 拿到了A锁
Thread-4 拿到A锁
Thread-4 拿到了B锁
Thread-4 拿到B锁
Thread-4 拿到了A锁
Thread-6 拿到A锁
Thread-6 拿到了B锁
Thread-6 拿到B锁
Thread-6 拿到了A锁
Thread-8 拿到A锁
Thread-8 拿到了B锁
Thread-8 拿到B锁
Thread-8 拿到了A锁
Thread-10 拿到A锁
Thread-10 拿到了B锁
Thread-10 拿到B锁
Thread-10 拿到了A锁
Thread-5 拿到A锁
Thread-5 拿到了B锁
Thread-5 拿到B锁
Thread-5 拿到了A锁
Thread-9 拿到A锁
Thread-9 拿到了B锁
Thread-9 拿到B锁
Thread-9 拿到了A锁
Thread-7 拿到A锁
Thread-7 拿到了B锁
Thread-7 拿到B锁
Thread-7 拿到了A锁
Thread-3 拿到A锁
Thread-3 拿到了B锁
Thread-3 拿到B锁
Thread-3 拿到了A锁
"""