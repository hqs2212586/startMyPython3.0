# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


"""
event实现线程之间同步
from threading import Event
event.isSet()：返回event的状态值；
event.wait()：如果 event.isSet()==False将阻塞线程；
event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
event.clear()：恢复event的状态值为False。  ————set()后再clear()，重置到初始状态。
"""
# from threading import Thread, Event
# import time
#
# event = Event()
#
# def student(name):
#     print("学生%s正在听课" % name)
#     event.wait()   # 在原地等待
#     print("学生%s课间活动" % name)
#
#
# def teacher(name):
#     print("老师%s 正在授课" % name)
#     time.sleep(7)
#     event.set()    # 这个运行后等待结束
#
#
# if __name__ == '__main__':
#     stu1 = Thread(target=student, args=('alex',))
#     stu2 = Thread(target=student, args=('wxx',))
#     stu3 = Thread(target=student, args=('yxx',))
#     t1 = Thread(target=teacher, args=('egon',))
#
#     stu1.start()
#     stu2.start()
#     stu3.start()
#     t1.start()
"""
学生alex正在听课
学生wxx正在听课
学生yxx正在听课
老师egon 正在授课  ------->在这里等7秒后，学生开始做课间活动
学生alex课间活动
学生wxx课间活动
学生yxx课间活动
"""

# 改写：有的学生线程，需要在老师发出结束信号前就去做其他工作
from threading import Thread, Event
import time

event = Event()

def student(name):
    print("学生%s正在听课" % name)
    event.wait(2)
    print("学生%s课间活动" % name)


def teacher(name):
    print("老师%s 正在授课" % name)
    time.sleep(7)
    event.set()


if __name__ == '__main__':
    stu1 = Thread(target=student, args=('alex',))
    stu2 = Thread(target=student, args=('wxx',))
    stu3 = Thread(target=student, args=('yxx',))
    t1 = Thread(target=teacher, args=('egon',))

    stu1.start()
    stu2.start()
    stu3.start()
    t1.start()
"""
学生alex正在听课
学生wxx正在听课
学生yxx正在听课
老师egon 正在授课   -------》等两秒后，学生就去做课间活动了，等满七秒，程序才结束
学生alex课间活动
学生yxx课间活动
学生wxx课间活动
"""

# 其他应用——检测多次不通过，设置超时
from threading import Thread, Event, currentThread
import time

event = Event()

def conn():
    n=0
    while not event.is_set():   # 还没有set()过，值为False
        if n == 3:
            print("%s try too many times!" % currentThread().getName())
            return   # 结束整个函数，如果break，则链接成功了
        print("%s try %s" % (currentThread().getName(), n))
        event.wait(0.5)   # 原地等待，并设置了超时时间
        n += 1

    print("%s is connected" % currentThread().getName())


def check():
    print("%s is checking" % currentThread().getName())
    time.sleep(5)   # 模拟检测
    event.set()     # 检测OK

if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=conn)
        t.start()
    t = Thread(target=check)   # 检测线程
    t.start()
"""
Thread-1 try 0
Thread-2 try 0
Thread-3 try 0
Thread-4 is checking
Thread-1 try 1
Thread-2 try 1
Thread-3 try 1
Thread-1 try 2
Thread-3 try 2
Thread-2 try 2
Thread-1 try too many times!
Thread-2 try too many times!
Thread-3 try too many times!
"""