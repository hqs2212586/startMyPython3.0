# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 提交任务的两种方式
"""
1、同步调用：提交完任务后，就在原地等待任务执行完毕，拿到执行结果，再执行下一行。
           导致程序是串行执行
"""
# from concurrent.futures import ThreadPoolExecutor
# import time
# import random
#
# def la(name):
#     print("%s is laing" % name)
#     time.sleep(random.randint(3,5))
#     res = random.randint(7, 13)*'#'
#     return {'name':name, 'res':res}
#
# def weigh(shit):
#     name = shit['name']
#     size = len(shit['res'])
#     print('%s 拉了 《%s》kg' % (name, size))
#
# if __name__ == '__main__':
#     pool = ThreadPoolExecutor(13)
#
#     shit1 = pool.submit(la, 'alex').result()
#     weigh(shit1)
#     shit2 = pool.submit(la, 'wupeiqi').result()
#     weigh(shit2)
#     shit3 = pool.submit(la, "yuanhao").result()
#     weigh(shit3)
"""
alex is laing
alex 拉了 《7》kg
wupeiqi is laing
wupeiqi 拉了 《9》kg
yuanhao is laing
yuanhao 拉了 《11》kg
"""

# 2、异步调用：提交完任务后，不在原地等待任务执行完毕
# 回调函数实现程序解耦合
from concurrent.futures import ThreadPoolExecutor
import time
import random

def la(name):
    print("%s is laing" % name)
    time.sleep(random.randint(3,5))
    res = random.randint(7, 13)*'#'
    # return {'name':name, 'res':res}

    weigh({'name':name, 'res':res})   # 直接把字典传给称重weigh()，但造成了程序耦合

def weigh(shit):
    name = shit['name']
    size = len(shit['res'])
    print('%s 拉了 《%s》kg' % (name, size))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)
    pool.submit(la, 'alex')
    pool.submit(la, 'wupeiqi')
    pool.submit(la, "yuanhao")
"""并发执行拉的任务，谁执行完，谁把结果传给称重功能。
alex is laing
wupeiqi is laing
yuanhao is laing
alex 拉了 《10》kg
wupeiqi 拉了 《7》kg
yuanhao 拉了 《7》kg
"""


# 解决上述程序的问题：程序耦合。
# 回调函数实现程序解耦合
from concurrent.futures import ThreadPoolExecutor
import time
import random

def la(name):
    print("%s is laing" % name)
    time.sleep(random.randint(3,5))
    res = random.randint(7, 13)*'#'
    return {'name':name, 'res':res}

    # weigh({'name':name, 'res':res})   # 直接把字典传给称重weigh()，造成了程序耦合

def weigh(shit):
    shit = shit.result()    # 对象.result()拿到结果并赋值给shit
    name = shit['name']
    size = len(shit['res'])
    print('%s 拉了 《%s》kg' % (name, size))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)
    # 回调函数，前面任务执行完，return返回值就会自动触发weith功能执行，把pool.submit(la, 'alex')对象当做参数传给weigh()
    pool.submit(la, 'alex').add_done_callback(weigh)
    pool.submit(la, 'wupeiqi').add_done_callback(weigh)
    pool.submit(la, "yuanhao").add_done_callback(weigh)
"""
alex is laing
wupeiqi is laing
yuanhao is laing
alex 拉了 《10》kg
wupeiqi 拉了 《7》kg
yuanhao 拉了 《7》kg
"""


# 阻塞和非阻塞
# 阻塞是进程运行的一种状态，遇到I/O就会进入阻塞状态，会被剥夺走CPU的执行权限。（非阻塞即对立面）

# 阻塞和同步的区别：同步调用时提交任务的方式，不考虑是否是计算型还是I/O型任务，都需要原地等待。