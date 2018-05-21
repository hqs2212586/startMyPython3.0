# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
进程池和线程池的接口一模一样，用法完全一样。
    使用场景其实就是进程、线程一致。

池：要对数目加以限制，保证机器一个可承受的范围，以一个健康的状态保证它的运行。
"""
# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# import os, time, random
#
# def task(name):
#     print("name: %s pid: %s run" % (name, os.getpid()))
#     time.sleep(random.randint(1,3))
#
#
# if __name__ == '__main__':
#     pool = ProcessPoolExecutor(4)    # 指定进程池大小，最大进程数，如果不指定默认是CPU核数
#
#     for i in range(10):
#         """从始至终四个进程解决这10个任务，谁没事了接新任务"""
#         pool.submit(task, 'egon%s' %i)   # 提交任务的方式————异步调用：提交完任务，不用在原地等任务执行拿到结果。

#     print("主进程")
"""
name: egon0 pid: 12445 run
name: egon1 pid: 12444 run
name: egon2 pid: 12446 run
name: egon3 pid: 12447 run
主进程
name: egon4 pid: 12445 run
name: egon5 pid: 12444 run
name: egon6 pid: 12446 run

name: egon7 pid: 12445 run
name: egon8 pid: 12446 run
name: egon9 pid: 12447 run
"""

# shutdown()
# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# import os, time, random
#
# def task(name):
#     print("name: %s pid: %s run" % (name, os.getpid()))
#     time.sleep(random.randint(1,3))
#
#
# if __name__ == '__main__':
#     pool = ProcessPoolExecutor(4)    # 指定进程池大小，最大进程数，如果不指定默认是CPU核数
#
#     for i in range(10):
#         """从始至终四个进程解决这10个任务，谁没事了接新任务"""
#         pool.submit(task, 'egon%s' %i)   # 提交任务的方式————异步调用：提交完任务，不用在原地等任务执行拿到结果。
#
#     pool.shutdown()   # 把提交任务入口关闭，默认参数wait=True；同时还进行了pool.join()操作，等任务提交结束，再结束主进程
#
#     print("主进程")
"""
name: egon0 pid: 12502 run
name: egon1 pid: 12503 run
name: egon2 pid: 12504 run
name: egon3 pid: 12505 run
name: egon4 pid: 12502 run
name: egon5 pid: 12503 run
name: egon6 pid: 12505 run
name: egon7 pid: 12504 run
name: egon8 pid: 12503 run
name: egon9 pid: 12505 run
主进程
"""


# 针对线程情况
# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# import os, time, random
#
# def task(name):
#     print("name: %s pid: %s run" % (name, os.getpid()))
#     time.sleep(random.randint(1,3))
#
#
# if __name__ == '__main__':
#     pool = ThreadPoolExecutor(4)    # 指定进程池大小，最大进程数，如果不指定默认是CPU核数
#
#     for i in range(10):
#         """从始至终四个进程解决这10个任务，谁没事了接新任务"""
#         pool.submit(task, 'egon%s' %i)   # 提交任务的方式————异步调用：提交完任务，不用在原地等任务执行拿到结果。
#
#     pool.shutdown(wait=True)   # 把提交任务入口关闭，默认参数wait=True；同时还进行了pool.join()操作，等任务提交结束，再结束主进程
#
#     print("主进程")
"""
name: egon0 pid: 12528 run
name: egon1 pid: 12528 run
name: egon2 pid: 12528 run
name: egon3 pid: 12528 run
name: egon4 pid: 12528 run
name: egon5 pid: 12528 run
name: egon6 pid: 12528 run
name: egon7 pid: 12528 run
name: egon8 pid: 12528 run
name: egon9 pid: 12528 run
主进程
"""

from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from threading import currentThread  # 查看线程名
import os, time, random

def task():
    print("name: %s pid: %s run" % (currentThread().getName(), os.getpid()))
    time.sleep(random.randint(1,3))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(4)    # 指定进程池大小，最大进程数，如果不指定默认是CPU核数

    for i in range(10):
        """从始至终四个进程解决这10个任务，谁没事了接新任务"""
        pool.submit(task,)   # 提交任务的方式————异步调用：提交完任务，不用在原地等任务执行拿到结果。

    pool.shutdown(wait=True)   # 把提交任务入口关闭，默认参数wait=True；同时还进行了pool.join()操作，等任务提交结束，再结束主进程

    print("主进程")
"""
name: <concurrent.futures.thread.ThreadPoolExecutor object at 0x10401af28>_0 pid: 12554 run
name: <concurrent.futures.thread.ThreadPoolExecutor object at 0x10401af28>_1 pid: 12554 run
name: <concurrent.futures.thread.ThreadPoolExecutor object at 0x10401af28>_2 pid: 12554 run
name: <concurrent.futures.thread.ThreadPoolExecutor object at 0x10401af28>_3 pid: 12554 run
name: <concurrent.futures.thread.ThreadPoolExecutor object at 0x10401af28>_2 pid: 12554 run
name: <concurrent.futures.thread.ThreadPoolExecutor object at 0x10401af28>_0 pid: 12554 run
name: <concurrent.futures.thread.ThreadPoolExecutor object at 0x10401af28>_3 pid: 12554 run
name: <concurrent.futures.thread.ThreadPoolExecutor object at 0x10401af28>_2 pid: 12554 run
name: <concurrent.futures.thread.ThreadPoolExecutor object at 0x10401af28>_1 pid: 12554 run
name: <concurrent.futures.thread.ThreadPoolExecutor object at 0x10401af28>_0 pid: 12554 run
主进程
"""