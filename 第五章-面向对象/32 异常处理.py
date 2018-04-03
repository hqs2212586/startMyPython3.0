# 1、什么是异常？
# 异常是错误发生的信号，一旦程序出错，并且程序没有处理这个错误，那就会抛出异常，并且程序的运行随之终止。


# 2、错误分为两种
# 语法错误:在程序执行前就要立刻改正过来
# print('xxxx'
# if 1 > 2

# 逻辑错误：
# ValueError
# int('aaa')

# NameError

# IndexError
# l = [1,2,3]
# l[1000] # list index out of range

# KeyError
# d = {}
# d['name']

# AttributeError
# class Foo:
#     pass
# Foo.xxx

# ZeroDivisionError
# 1/0

# TypeError:int类型不可迭代
# for i in 3:
#     pass
