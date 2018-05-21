# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 经过前面的分析：GIL导致同一时刻同一进程的多个线程只能有一个出来执行，
# 如果要利用多核优势，应该用多进程，但是进程开销太大；运用多线程，开销小了，但是利用不了多核优势。如何解决这个悖论呢？

"""
前提论点：
    1、cpu到底是用来做计算的，还是用来做I/O的？
    2、多cpu，意味着可以有多个核并行完成计算，所以多核提升的是计算性能
    3、每个cpu一旦遇到I/O阻塞，仍然需要等待，所以多核对I/O操作没什么用处
    
结论：
    1、对计算来说，cpu越多越好，但是对于I/O来说，再多的cpu也没用
    2、当然对运行一个程序来说，随着cpu的增多执行效率肯定会有所提高（不管提高幅度多大，总会有所提高），
    这是因为一个程序基本上不会是纯计算或者纯I/O，所以我们只能相对的去看一个程序到底是计算密集型还是I/O密集型，从而进一步分析python的多线程到底有无用武之地
    

假设我们有四个任务需要处理，处理方式肯定是要玩出并发的效果，解决方案可以是：
    方案一：开启四个进程
    方案二：一个进程下，开启四个线程

单核情况下，分析结果:
    如果四个任务是计算密集型，没有多核来并行计算，方案一徒增了创建进程的开销，方案二胜
    如果四个任务是I/O密集型，方案一创建进程的开销大，且进程的切换速度远不如线程，方案二胜

多核情况下，分析结果：
    如果四个任务是计算密集型，多核意味着并行计算，在python中一个进程中同一时刻只有一个线程执行用不上多核，方案一胜
    如果四个任务是I/O密集型，再多的核也解决不了I/O问题，方案二胜

对应场景：
    金融类项目对计算要求比较高要用计算密集型，应该用多进程。对机器的开销比较大
    多线程就利用于IO密集型：socket、爬虫、web
"""

# 多线程性能测试：
# 如果并发的多个任务是计算密集型：多进程效率高
# from multiprocessing import Process
# from threading import Thread
# import os,time
# def work():
#     res=0
#     for i in range(100000000):   # 纯计算任务
#         res*=i
#
#
# if __name__ == '__main__':
#     l=[]
#     print(os.cpu_count())  # 本机为4核
#     start=time.time()
#     for i in range(4):
#         # p=Process(target=work)  # 耗时10s多
#         p=Thread(target=work)  # 耗时20s多
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     stop=time.time()
#     print('run time is %s' %(stop-start))
# 由执行结果可以看到，多进程执行效率远高于多线程，运用了多核优势


# 如果并发的多个任务是I/O密集型：多线程效率高
from multiprocessing import Process
from threading import Thread
import threading
import os,time
def work():
    time.sleep(2)   # 模拟i/o类型，大部分时间都睡着在
    print('===>')

if __name__ == '__main__':
    l=[]
    print(os.cpu_count()) #本机为4核
    start=time.time()
    for i in range(400):
        p=Process(target=work) #耗时3s多,大部分时间耗费在创建进程上
        # p=Thread(target=work) #耗时2s多
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop=time.time()
    print('run time is %s' %(stop-start))
# 由执行结果看出来，多线程的执行效率和多进程的差别是数量级的差别，面对I/O密集任务应该使用多线程。





