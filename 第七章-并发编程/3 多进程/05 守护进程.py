# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
主进程创建子进程，然后将该进程设置成守护自己的进程
关于守护进程需要强调两点：
    其一：守护进程会在主进程代码执行结束后就终止
    其二：守护进程内不能再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children
"""
# 守护进程一定要在进程开启前设置
from multiprocessing import Process
import time

def task(name):
    print("%s is running" % name)
    time.sleep(2)


if __name__ == '__main__':
    p = Process(target=task, args=('子进程', ))
    p.daemon=True    # 守护进程一定要在进程开启前设置
    p.start()

    print("主进程")
"""
主进程    ————》子进程还没开始就已经结束了
"""

# 验证守护进程内部能再开子进程——》守护进程再开子进程会造成问题：会造成一堆孤儿
from multiprocessing import Process
import time

def task(name):
    print("%s is running" % name)
    time.sleep(2)
    p = Process(target=time.sleep, args=(3, ))
    p.start()

if __name__ == '__main__':
    p = Process(target=task, args=('子进程', ))
    p.daemon=True    # 守护进程一定要在进程开启前设置
    p.start()

    p.join()   # 让主进程等待子进程结束

    print("主进程")
"""
AssertionError: daemonic processes are not allowed to have children
"""

# 练习：思考下列代码的执行结果有可能有哪些情况？为什么？
from multiprocessing import Process

import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    p1=Process(target=foo)
    p2=Process(target=bar)

    p1.daemon=True   # 主进程代码执行完毕后，守护进程死
    p1.start()
    p2.start()
    print("main-------")
"""
main-------
456
end456
"""
# 另一种情况是机器性能特别强，在执行到main----之前，已经启动子进程p1了，会形成输出：
"""
123
main-------
456
end456
"""