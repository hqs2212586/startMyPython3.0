# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 方式一：通过multiprocessing模块开启紫禁城
# from multiprocessing import Process
# import time
#
# def task(name):
#     print("%s is running" % name)
#     time.sleep(3)
#     print("%s is done" % name)
#
# if __name__ == '__main__':
#     p = Process(target=task, args=('子进程1',))  # 得到对象
#     # Process(target=task, kwargs={'name': "子进程1"})
#
#     p.start()   # 给操作系统发送启动信号
#     print("主")
"""
主
子进程1 is running
子进程1 is done
"""
# 上述方法：是有父子关系，初始状态和父亲是一样的，但是运行状态完全无关。


# 方式二：不用默认的multiprocessing模块，继承并订制自己的类
from multiprocessing import Process
import time
class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):  # run()是固定形式，p.start本质是调用的绑定的run方法
        print('%s is running'%self.name)
        time.sleep(3)
        print("%s is done" % self.name)

if __name__ == '__main__':
    p = MyProcess('子进程')
    p.start()   # 给操作系统发送启动信号
    print('主')
"""
主
子进程 is running   # 间隔三秒
子进程 is done
"""