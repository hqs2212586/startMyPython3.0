# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
注意与进程queue的区别，理解线程queue的意义。
"""
# import queue
#
# q = queue.Queue(3)  # 生成队列，存数据最大值是3  先进先出
#
# q.put("first")   # 放值进去
# q.put(2)
# q.put("third")
# # q.put(4)   # 队列满了，阻塞
#
# print(q.get())   # 取数据
# print(q.get())
# print(q.get())
"""
first
2
third
"""


"""
queue的get()方法参数问题
"""
# import queue
#
# q = queue.Queue(3)  # 生成队列，存数据最大值是3  先进先出
#
# q.put("first")   # 放值进去
# q.put(2)
# q.put("third")
# # q.put(4)   # 队列满了，阻塞
# # q.put(4, block=False)   # 默认是block=True,    改为False后，队列满了还加数据，程序报错raise Full queue.Full
# # q.put(4, block=True, timeout=3)   # 设置了block=True队列满不会直接报错了，但是还加上了timeout=3,程序会等3秒后提示报错queue.Full
#
# # 同理get()方法也有这些参数
# print(q.get())   # 取数据
# print(q.get())
# print(q.get())
# # print(q.get(block=False))   # 在队列空，还取时，一般是卡住，但加入了block=False参数的话，会提示报错queue.Empty
# print(q.get_nowait())       # 这个效果同上
# print(q.get(block=True, timeout=3))    # 队列空，还取数据时，会按照timeout时间等待，到时间后提示queue.Empty


"""
后进先出——》堆栈
"""
import queue

q = queue.LifoQueue(3)   # 堆栈
q.put("first")
q.put(2)
q.put("third")

print(q.get())  # third
print(q.get())  # 2
print(q.get())  # first


"""
优先级队列
    数字越小优先级越高(指的是取出的优先级)
"""
import queue

q = queue.PriorityQueue(3)

q.put(10, 'one')
q.put(40, 'two')
q.put(30, 'three')

print(q.get())   # 10
print(q.get())   # 30
print(q.get())   # 40
