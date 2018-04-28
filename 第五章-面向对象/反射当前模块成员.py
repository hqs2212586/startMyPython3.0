# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import sys


def s1():
    print('s1')


def s2():
    print('s2')


this_module = sys.modules[__name__]

print(hasattr(this_module, 's1'))
print(getattr(this_module, 's2'))
"""
True
<function s2 at 0x101fb3620>
"""