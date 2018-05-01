# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
进程彼此之间互相隔离，要实现进程间通信（IPC）：
    multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的

创建队列的类（底层就是以管道和锁定的方式实现）：
    Queue([maxsize]):创建共享的进程队列，Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。
    队列的特性是先进先出，且队列内可以存放任意python类型数据。

参数介绍：
    maxsize是队列中允许最大项数，省略则无大小限制。
    但需要明确：
        1、队列内存放的是消息而非大数据
        2、队列占用的是内存空间，因而maxsize即便是无大小限制也受限于内存大小

主要方法介绍：
    q.put方法用以插入数据到队列中。
    q.get方法可以从队列读取并且删除一个元素。
"""

from multiprocessing import Queue

# 队列中应该放消息，不应该放大文件大数据
# 队列可以不设置长度，但是队列是受制于内存大小的，不可能无限存放
q = Queue(3)  # 指定队列大小
q.put('hello')
q.put({'a': 1})
q.put([3,3,3,])

print(q.full())   # 查看队列是否满了  # True
# q.put(123)    # 队列满了再往里面放时，被锁住，只能在原地卡着。

print(q.get())
print(q.get())
print(q.get())
print(q.empty())   # 判断队列是否全部清空  # True

# print(q.get())   # 由于已经空了，程序也卡在原处
"""
True
hello
{'a': 1}
[3, 3, 3]
True
"""