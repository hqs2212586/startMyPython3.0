
import random

random.randint(1, 100)  # 1-100之间取一个随机数
random.randrange(1, 100)  # 1-100之间取一个随机数
"""
randint&randrange的区别：
    randint不包含100，randrange包含100
"""

学习.模块.random()   # 返回一个随机浮点数
random.choice('huangisngiisha12131a@!!!')  # 返回一个给定数据集合中的随机字符
random.sample('adwas1231as!@#!as', 4)  # 从多个字符中选取特定数量的字符
"""
>>> random.random()
0.8102972151157363
>>> random.choice('huangisngiisha12131a@!!!')
'a'
>>> random.sample('adwas1231as!@#!as',4)
['@', '!', '1', 's']
"""


# 生成随机字符串

import string
"""
>>> string.digits
'0123456789'
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
"""

s = string.ascii_lowercase + string.digits
"""
>>> random.sample(s,5)
['x', 'k', '4', 'o', 'j']
>>> ''.join(random.sample(s,5))
'7abce'     # 随机验证码
"""

# 有序数打乱(抽奖)
"""
>>> li = list(range(100))
>>> random.shuffle(li)   # 打乱排序
>>> li
[9, 96, 74, 82, 54, 97, 49, 64, 31, 40, 58, 46, 30, 14, 38, 95, 48, 7, 12, 26, 56, 28, 16, 80, 77, 35, 57, 42, 60, 32, 70, 33, 67, 45, 43, 8, 76, 66, 89, 21, 69, 2, 87, 27, 61, 85, 36, 94, 65, 47, 13, 99, 73, 5, 18, 24, 52, 93, 78, 90, 15, 6, 68, 72, 63, 86, 81, 91, 20, 22, 84, 79, 59, 11, 75, 1, 83, 39, 10, 0, 51, 62, 50, 17, 34, 53, 29, 4, 19, 98, 92, 23, 88, 37, 44, 25, 3, 41, 71, 55]
"""