# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# multiprocess模块的完全模仿了threading模块的接口，二者在使用层面，有很大的相似性
# 方式一：
import time, random
# from multiprocessing import Process
from threading import Thread


def piao(name):
    print('%s piaoing' % name)
    time.sleep(random.randrange(1, 5))
    print('%s piao end' % name)

if __name__ == '__main__':
    t1 = Thread(target=piao, args=('egon', ))
    t1.start()  # 主线程向操作系统发信号，又开了一个线程
    print("主线程")   # 执行角度看是主线程，从资源角度看是主进程
# 这个程序总体是一个进程、两个线程
"""
egon piaoing
主进程
egon piao end
"""



# 方式二：定制自己的线程
import time, random
# from multiprocessing import Process
from threading import Thread

class MyThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("%s piaoing" % self.name)
        time.sleep(random.randrange(1, 5))
        print("%s piao end" % self.name)

if __name__ == '__main__':
    t1 = MyThread('egon')
    t1.start()  # 主线程向操作系统发信号，又开了一个线程
    print("主线程")
"""
egon piaoing
主线程
egon piao end
"""