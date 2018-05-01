# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


"""
join方法：优先运行子进程，主进程卡在原地，子进程结束后，运行主进程后面的代码。
"""
# from multiprocessing import Process
# import time, os
#
# def task():
#     print('%s is running, parent id is <%s>' % (os.getpid(), os.getppid()))   # 进程和父进程查看方式
#     time.sleep(3)
#     print("%s is done, parent id is <%s>" % (os.getpid(), os.getppid()))
#
# if __name__ == '__main__':
#     p = Process(target=task, )
#     p.start()
#
#     p.join()   # 优先运行子进程，主进程卡在原地
#     print('主进程', os.getpid(), 'pycharm ID', os.getppid())
#     print(p.pid)  # 子进程运行完，变为僵尸进程，主进程仍能够查到子进程的pid，当主进程结束后，所有僵尸子进程将被丢掉。
"""
828 is running, parent id is <827>
828 is done, parent id is <827>
主进程 827 pycharm ID 504
828
"""


# 并发执行
# from multiprocessing import Process
# import time, os
#
# def task(name ,n):
#     print('%s is running' % name)
#     time.sleep(n)
#
# if __name__ == '__main__':
#     start = time.time()
#     p1 = Process(target=task, args=("子进程1",5))
#     p2 = Process(target=task, args=("子进程2",3))
#     p3 = Process(target=task, args=("子进程3",2))
#     """
#     进程开启顺序由操作系统统筹控制，顺序是不一定的
#     主进程 1014 pycharm ID 504
#     子进程2 is running
#     子进程1 is running
#     子进程3 is running
#     """
#     p1.start()
#     p2.start()
#     p3.start()
#     # 再添加join函数前，主程序的执行输出次序是完全随机的，需要加join()保证主程序等到在子进程之后执行完成
#     p1.join()
#     p2.join()
#     p3.join()
#     # 以上并非串行执行，实际是并发执行，只是约束了主程序要等在子程序后结束
#     # print('主进程', os.getpid(), 'pycharm ID', os.getppid())
#     print("主进程", (time.time()-start))
"""
子进程1 is running
子进程2 is running
子进程3 is running
主进程 5.010260343551636   # 主程序只等了5秒，说明确实是并发执行
"""

# 并发简写
# from multiprocessing import Process
# import time, os
#
# def task(name ,n):
#     print('%s is running' % name)
#     time.sleep(n)
#
# if __name__ == '__main__':
#     start = time.time()
#     p1 = Process(target=task, args=("子进程1",5))
#     p2 = Process(target=task, args=("子进程2",3))
#     p3 = Process(target=task, args=("子进程3",2))
#     p_l = [p1, p2, p3]
#
#     for p in p_l:
#         p.start()
#
#     for p in p_l:
#         p.join()
#
#     print("主进程", (time.time()-start))
"""
子进程1 is running
子进程2 is running
子进程3 is running
主进程 5.007940769195557
"""


# 串行执行
# from multiprocessing import Process
# import time, os
#
# def task(name ,n):
#     print('%s is running' % name)
#     time.sleep(n)
#
# if __name__ == '__main__':
#     start = time.time()
#     p1 = Process(target=task, args=("子进程1",5))
#     p2 = Process(target=task, args=("子进程2",3))
#     p3 = Process(target=task, args=("子进程3",2))
#     # 串行执行
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     p3.start()
#     p3.join()
#
#     print("主进程", (time.time()-start))
"""
子进程1 is running
子进程2 is running
子进程3 is running
主进程 10.019965887069702
"""


"""
其他进程对象的属性和方法（了解）
1、p.pid  2、p.is_alive()   
"""
# from multiprocessing import Process
# import time, os
#
# def task():
#     print('%s is running, parent id is <%s>' % (os.getpid(), os.getppid()))   # 进程和父进程查看方式
#     time.sleep(3)
#     print("%s is done, parent id is <%s>" % (os.getpid(), os.getppid()))
#
# if __name__ == '__main__':
#     p = Process(target=task, )
#     p.start()
#     print(p.is_alive())
#     p.join()   # 优先运行子进程，主进程卡在原地
#     print('主进程', os.getpid(), 'pycharm ID', os.getppid())
#     print(p.pid)   # 查看进程
#     print(p.is_alive())   # 查看进程是否是活着的



"""
其他方法：p.terminate
         p.name   查看进程名
"""
from multiprocessing import Process
import time, os

def task():
    print('%s is running, parent id is <%s>' % (os.getpid(), os.getppid()))   # 进程和父进程查看方式
    time.sleep(3)
    print("%s is done, parent id is <%s>" % (os.getpid(), os.getppid()))

if __name__ == '__main__':
    p = Process(target=task, name='sub-Process')
    p.start()
    p.terminate()   # 告诉操作系统杀死进程
    time.sleep(3)
    print(p.is_alive())  # True:因为操作系统杀死进程也需要反映时间; 等三秒再查看，反馈为False
    print('主')
    print(p.name)  # 查看进程名
"""
False
主
sub-Process
"""