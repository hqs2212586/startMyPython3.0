# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
程序目录：
    module_test.py
    index.py

当前文件：
    index.py
"""

import module_test as obj

obj.test()

print(hasattr(obj,'test'))

getattr(obj,'test')()
"""
from the test
True
from the test
"""