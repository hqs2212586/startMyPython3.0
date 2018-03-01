'''
一个文件内的代码越多越长，就越不容易维护。
为了编写可维护的代码，将函数分组，分别放在不同的文件里。
用这种组织代码的方式，在Python中，一个.py文件就称之为一个模块(Module)
'''
"""
模块的好处：
    1、最大的好处是大大提升了代码的可维护性。
    2、编写代码不必从零开始，当一个模块编写完毕，就可以被其他地方引用（可重用）
    3、使用模块可以避免函数名和变量名冲突
        每个模块有独立的命名空间，相同名字函数、变量可分别存在不同模块
        编写模块时，不必考虑名字与其他模块冲突
        
模块分类：
    1、内置标准模块（标准库）执行help('modules')查看所有Python自带模块列表
    2、第三方开源模块，可通过pip install模块名  联网安装
    3、自定义模块
"""

# 模块导入方法
# 第一种：import module 把整个模块都导入
import os

# 第二种：from module import xx 是从什么导入什么
from os import rmdir,rename  # 可以一次导入多个子模块


# 第三种：from module xx.xx import xx as rename
# from django.core import handler  # 一层层进入
import multiprocessing as mul  # 对于名称很长的模块可以用as起一个别名

# import socket
# socket.AF_INET  # 想省去socket的填写

# from socket import AF_INET
# AF_INET


# 第四种：from socket import *  # 不要这么写，各种模块之前可能变量发生冲突
'''
    注意：模块一旦被调用，即相当于执行了另外一个py文件里的代码。
'''

import sys
# >>> sys.path  # 导入模块时，查找的目录，从左到右
'''
['',  # 第一个元素为空，代表当前目录，自己定义的模块在当前目录会优先导入
 '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', # Python自带安装包
 '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6',    # c语言相关库
  '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload',  # 
  '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages',  # 所有第三方和内置的库
]
'''
sys.path.append('第四章-模块')   # 添加新的查找目录
del sys.path[-1]         # 删除查找目录
"""
Python解释器会按照列表顺序去依次到每个目录下去匹配要导入的模块名，
只要在一个目录下匹配到了该模块名，就立刻导入，不再继续往后找。
"""
