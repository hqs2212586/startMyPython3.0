# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 1、简述计算机操作系统中的“中断”的作用？
"""
中断是指CPU对系统发生的某个事件做出的一种反应，CPU暂停正在执行的程序，保留现场后自动地转去执行相应的处理程序，处理完该事件后再返回断点继续执行被“打断”的程序。
中断是CPU处理突发事件的一个重要技术。
作用：它使计算机可以更好更快利用有限的系统资源解决系统响应速度和运行效率的一种控制技术.
         实时响应 + 系统调用
"""
# 2、简述计算机内存中的“内核态”和“用户态”；
"""
内核态:运行操作系统的程序,os的数据存放
用户态:运行用户程序,用户进程的数据存放
用户态的应用程序可以通过三种方式来访问内核态的资源：1）系统调用；2）库函数；3）Shell脚本。
用户态到内核态的切换:
    1.系统调用        用户程序主动发起的 软中断 os.fork() process
    2.异常            被动的   当CPU正在执行运行在用户态的程序时，突然发生某些预先不可知的异常事件，这个时候就会触发从当前用户态执行的进程
                              转向内核态执行相关的异常事件，典型的如缺页异常。
    3.外围设备的硬中断  被动的   外围设备完成用户的请求操作后，会像CPU发出中断信号，此时，CPU就会暂停执行下一条即将要执行的指令，
                              转而去执行中断信号对应的处理程序，如果先前执行的指令是在用户态下，则自然就发生从用户态到内核态的转换。
"""
# 3、进程间通信方式有哪些？
"""
进程彼此之间互相隔离，要实现进程间通信（IPC），multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的
"""
# 4、简述你对管道、队列的理解；
"""队列 = 管道 + 锁"""
# 5、请列举你知道的进程间通信方式；
"""队列,信号量,Event事件,定时器Timer,线程queue,进程池线程池,异步调用+回调机制"""
# 6、什么是同步I/O，什么是异步I/O？
"""
同步（synchronous）IO：就是在发出一个功能调用时，在没有得到结果之前，该调用就不会返回。按照这个定义，其实绝大多数函数都是同步调用。但是一般而言，我们在说同步、异步的时候，特指那些需要其他部件协作或者需要一定时间完成的任务。
异步（asynchronous）IO：异步的概念和同步相对。当一个异步功能调用发出后，调用者不能立刻得到结果。当该异步功能完成后，通过状态、通知或回调来通知调用者。
"""
# 7、请问multiprocessing模块中的Value、Array类的作用是什么？举例说明它们的使用场景
"""
Value，Array（用于进程通信，资源共享）

"""
# 8、请问multiprocessing模块中的Manager类的作用是什么？与Value和Array类相比，Manager的优缺点是什么？
"""
Manager（用于资源共享）
"""
# 9、写一个程序，包含十个线程，子线程必须等待主线程sleep 10秒钟之后才执行，并打印当前时间；
from threading import Thread
import time

def task(name):
    print(name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

if __name__ == '__main__':
    time.sleep(10)
    for i in range(10):
        t = Thread(target=task, args=("线程 %s" % i,))
        t.start()

# 10、写一个程序，包含十个线程，同时只能有五个子线程并行执行；
from concurrent.futures import ThreadPoolExecutor
import os,time,random
def task(n):
    print("%s is running" % os.getpid())
    time.sleep(random.randint(1,3))
    return n**2

if __name__ == '__main__':
    executor = ThreadPoolExecutor(5)
    futures=[]
    for i in range(10):
        future = executor.submit(task, i)
        futures.append(future)
    executor.shutdown(True)
    print('++>')
    for future in futures:
        print(future.result())

# 11、写一个程序，要求用户输入用户名和密码，要求密码长度不少于6个字符，且必须以字母开头，如果密码合法，则将该密码使用md5算法加密后的十六进制概要值存入名为password.txt的文件，超过三次不合法则退出程序；
import hashlib
import json
import re

def func():
    count = 0
    while count < 3:
        username = input("username>>>:").strip()
        password = input("password>>>:").strip()
        if len(password) < 6 or not re.search('\A([a-z]|[A-Z])', password):
            count += 1
            print("must match password rule")
        else:
            obj = {
                'username':username,
                'password':hashlib.md5(password.encode('utf-8')).hexdigest()
            }
            json.dump(obj, open('password.txt', 'a', encoding='utf-8'))
            break

if __name__ == '__main__':
    func()


# 12、写一个程序，使用socketserver模块，实现一个支持同时处理多个客户端请求的服务器，要求每次启动一个新线程处理客户端请求；
###################server#####################
import socketserver

class Handler(socketserver.BaseRequestHandler):    # 必须继承BaseRequestHandler
    def handle(self):
        print('new connection:', self.client_address)
        while True:
            try:
                data = self.request.recv(1024)
                if not data:break
                print('client data:', data.decode())
                self.request.send(data.upper())
            except Exception as e:
                print(e)
                break

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), Handler)  # 实例化对象，实现多线程的socket
    server.serve_forever()   # 事件监听，并调用handler方法

###################client######################
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
while True:
    msg = input(">>>:").strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))
