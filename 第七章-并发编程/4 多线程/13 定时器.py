# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


"""
定时器：隔多少时间之后去触发
"""
# from threading import Timer
#
#
# def task(name):
#     print("hello %s" % name)
#
# t = Timer(5, task, args=('egon',))   # 创建对象，Timer是Thread的子类，其实就是一个线程
# t.start()
# # hello egon ---->在等五秒后打印


# 定时器在验证码的应用
# import random
#
# def make_code(n=4):  # 设置默认值为4
#     res = ''
#     for i in range(n):
#         s1 = str(random.randint(0,9))   # 随机数字字符
#         s2 = chr(random.randint(65, 90))   # 随机字母 ，注意了解chr()内置函数
#         res += random.choice([s1, s2])
#     return res
#
# print(make_code())
"""
6HS8  \  6S38  ————》结果随机产生
"""

# 将定时器改写为类
from threading import Timer
import random

class Code:
    def __init__(self):
        self.make_cache()

    def make_cache(self, interval=8):
        self.cache = self.make_code()   # 缓存验证码
        print(self.cache)
        self.t = Timer(interval, self.make_cache)   # 创建定时器，到时间刷新一次
        self.t.start()

    def make_code(self, n=4):  # 设置默认值为4
        res = ''
        for i in range(n):
            s1 = str(random.randint(0,9))   # 随机数字字符
            s2 = chr(random.randint(65, 90))   # 随机字母 ，注意了解chr()内置函数
            res += random.choice([s1, s2])
        return res

    def check(self):
        while True:
            code = input("请输入你的验证码>>：").strip()
            if code.upper() == self.cache:
                print("验证码输入正确")
                self.t.cancel()
                break


obj = Code()
obj.check()
"""
E8I2
请输入你的验证码>>：E8I2
验证码输入正确
"""