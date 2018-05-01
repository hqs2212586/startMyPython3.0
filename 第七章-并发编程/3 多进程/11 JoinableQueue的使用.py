# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# JoinableQueue的用法和queue类似，只是这个queue是可以被join的
from multiprocessing import Process, JoinableQueue
import time

def producer(q):
    for i in range(2):
        res = '包子%s' % i
        time.sleep(0.5)   # 模拟生产时间
        print('生产者生产了%s' % res)

        q.put(res)  # 放入队列中
    q.join()  # 生产者生产完等队列把数据都取完


def consumer(q):
    while True:
        res = q.get()   # 取队列中数据
        if res is None:break
        time.sleep(1)    # 模拟消费时间
        print('消费者消费了%s' % res)
        q.task_done()   # 提供的接口，消费者告诉生产者取走了一个数据


if __name__ == '__main__':
    # 容器
    q = JoinableQueue()
    q.join()    # 等队列执行完（等队列取完）

    # 生产者
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=producer, args=(q,))
    p3 = Process(target=producer, args=(q,))
    # 消费者
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))
    # 主进程执行完之后，守护进程也终止，因此把消费者设置为守护进程
    c1.daemon=True
    c2.daemon=True

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()

    print("主进程")
"""
生产者生产了包子0
生产者生产了包子0
生产者生产了包子0
生产者生产了包子1
生产者生产了包子1
生产者生产了包子1
消费者消费了包子0
消费者消费了包子0
消费者消费了包子0
消费者消费了包子1
消费者消费了包子1
消费者消费了包子1
主进程
"""