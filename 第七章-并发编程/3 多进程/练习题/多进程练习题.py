# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
1、思考开启进程的方式一和方式二各开启了几个进程？
    两种方式都是开启了1个主进程4个子进程
"""
"""
2、进程之间的内存空间是共享的还是隔离的？下述代码的执行结果是什么？
    进程之间的内存空间是隔离的。执行输出："子进程内:  0"
"""
from multiprocessing import Process

n=100 #在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了

def work():
    global n
    n=0
    print('子进程内: ',n)


if __name__ == '__main__':
    p=Process(target=work)
    p.start()
"""输出：
子进程内:  0
"""

"""
3、基于多进程实现并发的套接字通信？
4、思考每来一个客户端，服务端就开启一个新的进程来服务它，这种实现方式有无问题？
    见多进程并发套接字通信文件夹。
"""

"""1、保证最先输出的是--------->4"""
# from multiprocessing import Process
# import time
# import random
#
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('-------->%s' %n)
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     print('-------->4')

"""2、保证最后输出的是--------->4"""
# from multiprocessing import Process
# import time
# import random
#
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('-------->%s' %n)
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#     p1.start()
#     p2.start()
#     p3.start()
#     p1.join()
#     p2.join()
#     p3.join()
#     print('-------->4')

"""3、保证按顺序输出"""
# from multiprocessing import Process
# import time
# import random
#
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('-------->%s' %n)
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     p3.start()
#     p3.join()
#     print('-------->4')

"""
4、判断上述三种效果，哪种属于并发，哪种属于串行？
    前两种都是并发，第三种属于串行
"""