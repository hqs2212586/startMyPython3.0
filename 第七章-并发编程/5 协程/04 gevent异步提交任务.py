# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from gevent import monkey;monkey.patch_all()
import gevent
import time

def eat(name):
    print('%s eat food 1' % name)
    time.sleep(2)
    print('%s eat food 2' % name)

def play(name):
    print('%s play 1' % name)
    time.sleep(1)
    print('%s play 2' % name)

g1=gevent.spawn(eat, 'egon')   # 创建一个协程对象g1，spawn括号内第一个参数是函数名
g2=gevent.spawn(play, 'alex')
"""
直接执行上述代码，没有任何输出。线程把代码运行完直接结束，任务还没来的及开启就结束了。
"""
# time.sleep(1)  # 睡一秒是不够的，到时间，线程依然是结束了
"""
egon eat food 1
alex play 1
"""
# time.sleep(5)
"""
egon eat food 1
alex play 1
alex play 2
egon eat food 2  ————》这一行输出完后，还要等sleep的5秒全部睡晚，程序结束
"""
# 解决方案一：上述两步合作一步
# g1.join()  # 等待g1结束
# g2.join()  # 等待g2结束

# 解决方案二：
gevent.joinall([g1, g2])