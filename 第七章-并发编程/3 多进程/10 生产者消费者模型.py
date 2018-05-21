# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
为什么要使用生产者消费者模型？
    生产者指的是生产数据的任务，消费者指的是处理数据的任务。
    在并发编程中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，
    才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。

什么是生产者和消费者模式？
    生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。
    生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，
    直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，
    平衡了生产者和消费者的处理能力。

    这个阻塞队列就是用来给生产者和消费者解耦的
"""
# import time
#
# def producer():
#     for i in range(3):
#         res = '包子%s' % i
#         time.sleep(2)   # 模拟生产时间
#         print('生产者生产了%s' % res)
#
#         cosumer(res)
#
#
# def cosumer(res):
#     time.sleep(1)    # 模拟消费时间
#     print('消费者消费了%s' % res)
#
#
# producer()
"""上述代码的问题：生产者生产完了交给消费者，等消费者消费完生产者继续生产。两者需要互相等效率非常低"""


# 用生产者和消费者模型解决
"""
在生产者和消费者之间引入一个容器，用来装生产者生产的数据。消费者要处理的数据，直接从容器中拿。
    1、这样就解开了生产者和消费者之间的强耦合；2、平衡了生产者消费者之间的速度差。
    
只要程序中有两类任务是一类负责生产数据；一类负责处理数据，就可以引入生产者和消费者模型。

同时这也涉及到了进程间通信，正好可以利用队列实现。
"""
# from multiprocessing import Process, Queue
# import time
#
# def producer(q):
#     for i in range(10):
#         res = '包子%s' % i
#         time.sleep(0.5)   # 模拟生产时间
#         print('生产者生产了%s' % res)
#
#         q.put(res)  # 放入队列中
#
#
# def consumer(q):
#     while True:    # 一直从队列取一旦取空了，会加一把锁，程序卡在这里
#         res = q.get()   # 取队列中数据
#         time.sleep(1)    # 模拟消费时间
#         print('消费者消费了%s' % res)
#
# if __name__ == '__main__':
#     # 容器
#     q = Queue()
#     # 生产者
#     p1 = Process(target=producer, args=(q, ))
#     # 消费者
#     c1 = Process(target=consumer, args=(q, ))
#
#     p1.start()
#     c1.start()
#     print("主进程")
"""
主进程
生产者生产了包子0
生产者生产了包子1
生产者生产了包子2
消费者消费了包子0
生产者生产了包子3
消费者消费了包子1
生产者生产了包子4
生产者生产了包子5
消费者消费了包子2
生产者生产了包子6
生产者生产了包子7
...
消费者消费了包子9
"""

# 为了解决队列取空锁死的问题，做如下修改：
from multiprocessing import Process, Queue
import time

def producer(q):
    for i in range(10):
        res = '包子%s' % i
        time.sleep(0.5)   # 模拟生产时间
        print('生产者生产了%s' % res)

        q.put(res)  # 放入队列中


def consumer(q):
    while True:    # 一直从队列取一旦取空了，会加一把锁，程序卡在这里
        res = q.get()   # 取队列中数据
        if res is None:break
        time.sleep(1)    # 模拟消费时间
        print('消费者消费了%s' % res)

if __name__ == '__main__':
    # 容器
    q = Queue()
    # 生产者
    p1 = Process(target=producer, args=(q, ))
    # 消费者
    c1 = Process(target=consumer, args=(q, ))

    p1.start()
    c1.start()

    p1.join()   # 保证生产者都执行完，主进程才执行完
    q.put(None)  # 往队列里放入None,给消费者判断
    print("主进程")
"""
生产者生产了包子0
生产者生产了包子1
生产者生产了包子2
消费者消费了包子0
生产者生产了包子3
消费者消费了包子1
生产者生产了包子4
生产者生产了包子5
消费者消费了包子2
生产者生产了包子6
生产者生产了包子7
消费者消费了包子3
生产者生产了包子8
生产者生产了包子9
主进程
消费者消费了包子4
消费者消费了包子5
消费者消费了包子6
消费者消费了包子7
消费者消费了包子8
消费者消费了包子9
"""

# 生产者和消费者有多个情况：
from multiprocessing import Process, Queue
import time

def producer(q):
    for i in range(10):
        res = '包子%s' % i
        time.sleep(0.5)   # 模拟生产时间
        print('生产者生产了%s' % res)

        q.put(res)  # 放入队列中

        # q.put(None)  # 这种方式会将消费者提前停止


def consumer(q):
    while True:    # 一直从队列取一旦取空了，会加一把锁，程序卡在这里
        res = q.get()   # 取队列中数据
        if res is None:break
        time.sleep(1)    # 模拟消费时间
        print('消费者消费了%s' % res)

if __name__ == '__main__':
    # 容器
    q = Queue()
    # 生产者
    p1 = Process(target=producer, args=(q, ))
    p2 = Process(target=producer, args=(q,))
    p3 = Process(target=producer, args=(q,))
    # 消费者
    c1 = Process(target=consumer, args=(q, ))
    c2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()   # 保证生产者都执行完，主进程才执行完
    p2.join()
    p3.join()
    # 跟在正常信号后面，必须保证所有的生产者都生产结束
    q.put(None)  # 往队列里放入None,给消费者判断
    q.put(None)  # 有几个消费者就需要几个结束信号
    print("主进程")

"""
总结：
    1、生产者消费者模型什么时候用？
        程序中有两类角色：一类生产数据；一类消费数据
    2、怎么叫生产者消费者模型？
        引入队列解决生产者和消费者之间的耦合，这个并不依赖进程，这实际是介绍了一种编程方式。
        如果使用了Queue,说明生产者、消费者、queue都在一台机器，这就是集中式架构了，严重影响性能和稳定性。
        基于网络通信的消息队列：Rabbitmq
    3、好处：
        （1）程序解耦合
        （2）平衡生产者和消费者之间的速度差
"""