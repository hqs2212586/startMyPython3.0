# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
协程是基于单线程来实现并发，需要从应用程序级别找到解决方案。任务切换前保存任务运行状态 。 
"""
# 实现一个任务切到另一个任务，实现了单线程下并发的效果，达到协程的效果。
# 并发的本质：切换+保存状态，切换分两种：
# 1、是该任务发生了阻塞
# 2、是该任务计算的时间过长或有一个优先级更高的程序替代了它

"""
1 yiled可以保存状态，yield的状态保存与操作系统的保存线程状态很像，但是yield是代码级别控制的，更轻量级
2 send可以把一个函数的结果传给另外一个函数，以此实现单线程内程序之间的切换
"""
import time
def producer():
    g = consumer()
    next(g)
    for i in range(1000000):
        g.send(i)   # send一次就会切到consumer


def consumer():
    while True:
        res = yield   # yield收到producer  i的值，处理完切回producer的for循环

start_time = time.time()
producer()
stop_time = time.time()
print(stop_time-start_time)
"""0.26706719398498535"""


# 并发切换分两种，但只有遇到阻塞了切换会提升效率，串行改写如下：
import time
def producer():
    res = []
    for i in range(1000000):
        res.append(i)
    return res

def consumer(res):
    pass

start_time = time.time()
res = producer()
consumer(res)
stop_time = time.time()
print(stop_time-start_time)
"""0.18116021156311035"""
# 结论：这种形式的并发反而降低了效率


"""
协程总结：是单线程下的并发，又称微线程，纤程。英文名Coroutine。
一句话说明什么是协程：协程是一种用户态的轻量级线程，即协程是由用户程序自己控制调度的。
    用户态指的是应用程序内去控制的，操作系统认为是一个线程；用户自己控制调度比操作系统，速度会快很多
    
强调：
    1. python的线程属于内核级别的，即由操作系统控制调度（如单线程遇到io或执行时间过长就会被迫交出cpu执行权限，切换其他线程运行）
    2. 单线程内开启协程，一旦遇到io，就会从应用程序级别（而非操作系统）控制切换，以此来提升效率（！！！非io操作的切换与效率无关）

优点：
    1. 协程的切换开销更小，属于程序级别的切换，操作系统完全感知不到，因而更加轻量级
    2. 单线程内就可以实现并发的效果，最大限度地利用cpu （占用CPU的时间多了，就叫做效率高，对操作系统的一种欺骗）
    
缺点：
    1. 协程的本质是单线程下，无法利用多核，可以是一个程序开启多个进程，每个进程内开启多个线程，每个线程内开启协程
    2. 协程指的是单个线程，因而一旦协程出现阻塞，将会阻塞整个线程（只能实现并发，不能实现并行）
    
特点：
    1、必须在只有一个单线程里实现并发
    2、修改共享数据不需加锁（本质是一个一个执行，因此不需要考虑加锁）
    3、用户程序里自己保存多个控制流的上下文栈（自己控制切换）
    4、附加：一个协程遇到IO操作自动切换到其它协程（如何实现检测IO，yield、greenlet都无法实现，就用到了gevent模块（select机制））
"""