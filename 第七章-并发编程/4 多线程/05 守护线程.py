# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
一个进程内，如果不开线程，默认就是一个主线程。主线程代码运行完毕，进程被销毁。
一个进程内，开多个线程的情况下，主线程在代码运行完毕后，还要等其他线程工作完才死掉，进程销毁。

守护线程守护主线程，等到主线程死了才会被销毁。在有其他线程的情况下，主线程代码运行完后，等其他非守护线程结束，守护线程才会死掉。
"""
from threading import Thread
import time

def sayhi(name):
    time.sleep(2)
    print("%s say hello" % name)

if __name__ == '__main__':
    t = Thread(target=sayhi, args=('egon',))

    # 守护线程必须在t.start()前设置
    # 守护线程设置方式一：
    t.daemon=True
    # 守护线程设置方式二：
    # t.setDaemon(True)

    t.start()   # 立马创建子线程，但需要等待两秒，因此程序会先执行下面的代码

    print("主线程")
    print(t.is_alive())
# 这一行代码执行完后，主线程执行完毕，由于主线程之外，只有一个守护线程，主线程不需要等守护线程执行结束，因此主线程和守护进程终止，进程结束。
"""
主线程
True
"""


# 练习：思考下述代码的执行结果有可能是哪些情况？为什么？
from threading import Thread
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
    t1=Thread(target=foo)
    t2=Thread(target=bar)

    t1.daemon=True   # t1是守护线程
    t1.start()
    t2.start()
    print("main-------")   # 主线程结束后，会等待非守护线程结束
# 由于非守护线程需要等待的时间比守护线程长，因此线程都会得到执行
"""
123
456
main------
end123
end456
"""