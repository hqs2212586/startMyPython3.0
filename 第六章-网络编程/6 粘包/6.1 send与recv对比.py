# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
1、不管recv还是send都不是直接接收对方的数据，而是操作自己的操作系统内存--->不是一个send对应一个recv

2、recv：
    第一阶段：wait data 耗时非常长
    第二阶段：copy data 把数据从系统内存拷贝到程序内存，时间非常短
    
   send:
    一个阶段：copy data,由自己的应用程序内存拷贝到系统内存，时间非常短
    
3、
"""