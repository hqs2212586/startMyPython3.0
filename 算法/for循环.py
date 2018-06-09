# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

"""
作业：使用*打印直角三角形  6行
         *
         * *
         * * *
         * * * *
         * * * * *
         * * * * * *
"""
i = j = k = 1
for i in range(0, 6):
    for j in range(0, 6-i):
        print("*", end='')   # 特别需要注意加了end='' 才会不自动换行
        j += 1
    i += 1
    print('')  # print('\n') 默认就有换行

"""
作业：使用*打印等边三角形
     *
    ***
   *****
  *******
 *********
***********
"""
m = n = 1
for m in range(0, 7):
    for p in range(m, 6):
        print(" ", end='')
    for n in range(0, 2*m-1):
        print('*', end='')
    print('')
