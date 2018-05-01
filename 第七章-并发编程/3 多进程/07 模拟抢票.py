# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# from multiprocessing import Process
# import json, time
#
# def search(name):
#     """查票"""
#     time.sleep(1)   # 模拟网络延迟,并发去看票数
#     dic = json.load(open('db.txt', 'r', encoding='utf-8'))
#     print('<%s> 查看到剩余票数[%s]' %(name, dic['count']))
#
#
# def get(name):
#     """买票"""
#     time.sleep(1)   # 模拟网络延迟
#     dic = json.load(open('db.txt', 'r', encoding='utf-8'))
#     if dic['count'] > 0:    # 确认有票
#         dic['count'] -= 1
#         time.sleep(3)
#         # 写入文件，即购票成功，这个必须是基于其他人购票的结果，由并发改为串行
#         json.dump(dic, open('db.txt', 'w', encoding='utf-8'))
#         print('<%s> 购票成功' % name)
#
#
# def task(name):
#     search(name)
#     get(name)
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         p = Process(target=task, args=('路人%s' % i, ))
#         p.start()
"""
<路人1> 查看到剩余票数[1]
<路人0> 查看到剩余票数[1]
<路人2> 查看到剩余票数[1]
<路人4> 查看到剩余票数[1]
<路人3> 查看到剩余票数[1]
<路人5> 查看到剩余票数[1]
<路人6> 查看到剩余票数[1]
<路人7> 查看到剩余票数[1]
<路人8> 查看到剩余票数[1]
<路人9> 查看到剩余票数[1]
<路人1> 购票成功
<路人0> 购票成功
<路人2> 购票成功
<路人3> 购票成功
<路人4> 购票成功
<路人5> 购票成功
<路人6> 购票成功
<路人8> 购票成功
<路人7> 购票成功
<路人9> 购票成功
"""
"""
db.txt里只有一张票，由于并发卖出了10次。需要把购票行为改为串行，只有第一个人可以买到票
"""
from multiprocessing import Process, Lock
import json, time

def search(name):
    """查票"""
    time.sleep(1)   # 模拟网络延迟,并发去看票数
    dic = json.load(open('db.txt', 'r', encoding='utf-8'))
    print('<%s> 查看到剩余票数[%s]' %(name, dic['count']))


def get(name):
    """买票"""
    time.sleep(1)   # 模拟网络延迟
    dic = json.load(open('db.txt', 'r', encoding='utf-8'))
    if dic['count'] > 0:    # 确认有票
        dic['count'] -= 1
        time.sleep(3)
        # 写入文件，即购票成功，这个必须是基于其他人购票的结果，由并发改为串行
        json.dump(dic, open('db.txt', 'w', encoding='utf-8'))
        print('<%s> 购票成功' % name)


def task(name, mutex):
    search(name)   # 查票并发执行，人人都可以看到票
    mutex.acquire()    # 上锁
    get(name)      # 购票改为串行，其他人都必须等着
    mutex.release()    # 解锁


if __name__ == '__main__':
    mutex = Lock()
    for i in range(10):
        p = Process(target=task, args=('路人%s' % i, mutex))
        p.start()
"""
<路人0> 查看到剩余票数[1]
<路人1> 查看到剩余票数[1]
<路人2> 查看到剩余票数[1]
<路人3> 查看到剩余票数[1]
<路人4> 查看到剩余票数[1]
<路人5> 查看到剩余票数[1]
<路人6> 查看到剩余票数[1]
<路人7> 查看到剩余票数[1]
<路人8> 查看到剩余票数[1]
<路人9> 查看到剩余票数[1]
<路人0> 购票成功
"""