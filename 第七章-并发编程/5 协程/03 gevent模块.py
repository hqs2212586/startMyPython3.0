# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
安装:pip3 install gevent
gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。 
    Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。
"""
import gevent
import time

def eat(name):
    print("%s eat 1" % name)
    # time.sleep(1)  # 不切，不能识别其他程序的I/O操作
    gevent.sleep(3)  # gevent只能识别自己模拟的I/O操作
    print("%s eat 2" % name)

def play(name):
    print("%s play 1" % name)
    gevent.sleep(4)
    print("%s paly 2" % name)


start_time = time.time()
g1 = gevent.spawn(eat, 'egon')
g2 = gevent.spawn(play, "alex")
# 异步提交，提交后不会等待完成结果

g1.join()
g2.join()
stop_time = time.time()
print(stop_time-start_time)
"""
egon eat 1
alex play 1
egon eat 2  ----->等三秒
alex paly 2 —————>再等一秒
4.006500005722046
"""

"""
time.sleep(2)或其他的阻塞,gevent是不能直接识别的需要用下面一行代码,打补丁,就可以识别了
from gevent import monkey;monkey.patch_all()必须放到被打补丁者的前面，如time，socket模块之前
或者我们干脆记忆成：要用gevent，需要将from gevent import monkey;monkey.patch_all()放到文件的开头
"""
from gevent import monkey;monkey.patch_all()
import gevent
import time
def eat():
    print('eat food 1')
    time.sleep(2)
    print('eat food 2')

def play():
    print('play 1')
    time.sleep(1)
    print('play 2')

g1=gevent.spawn(eat)
g2=gevent.spawn(play)
gevent.joinall([g1,g2])
print('主')
"""
eat food 1
play 1
play 2
eat food 2
主
"""