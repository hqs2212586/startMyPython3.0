# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


# join形式改写
from multiprocessing import Process
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
    else:
        print('<%s>购票失败' % name)


def task(name):
    search(name)
    get(name)


if __name__ == '__main__':
    for i in range(10):
        p = Process(target=task, args=('路人%s' % i, ))
        p.start()
        p.join()

"""
<路人0> 查看到剩余票数[1]
<路人0> 购票成功
<路人1> 查看到剩余票数[0]
<路人1>购票失败
<路人2> 查看到剩余票数[0]
<路人2>购票失败
<路人3> 查看到剩余票数[0]
<路人3>购票失败
<路人4> 查看到剩余票数[0]
<路人4>购票失败
<路人5> 查看到剩余票数[0]
<路人5>购票失败
<路人6> 查看到剩余票数[0]
<路人6>购票失败
<路人7> 查看到剩余票数[0]
<路人7>购票失败
<路人8> 查看到剩余票数[0]
<路人8>购票失败
<路人9> 查看到剩余票数[0]
<路人9>购票失败
"""

"""
对比互斥锁和join对比：两者都可以将并发改为串行，都保证了数据的安全性。
    1、互斥锁是把代码中对共享数据修改的部分代码改为串行。保证是一个一个来修改的。
    2、join是把代码整体修改为串行。
    
    
进程间内存是互相隔离的，但可以通过文件来共享数据、共享硬盘空间。但是文件共享数据实现进程间通讯依然存在问题：
    1、硬盘数据读取效率低 
    2、需要自己加锁处理

mutiprocessing模块提供的基于消息的IPC通信机制：队列和管道，可以帮助解决锁和效率的问题：
    1、队列和管道都是将数据存放于内存中，而队列又是基于（管道+锁）实现的，可以让我们从复杂的锁问题中解脱出来
    2、在进程数目增多时，往往可以获得更好的可扩展性
        
"""
