# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


# 求 50 - 100 之间的质数
import math
for i in range(50, 100 + 1):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
           break
    else:
        print(i)
"""
53
59
61
67
71
73
79
83
89
97
"""