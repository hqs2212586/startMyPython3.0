# 1、什么是异常？
# 异常是错误发生的信号，一旦程序出错，并且程序没有处理这个错误，那就会抛出异常，并且程序的运行随之终止。
# （1）Traceback:异常定位
# （2）异常类型valueError
# （3）异常的值，说明具体是抛出了什么问题

# 2、错误分为两种
# （1）语法错误:在程序执行前就要立刻改正过来
# print('xxxx'
# if 1 > 2

# （2）逻辑错误：
# ValueError  对象使用不合适的值引起
# int('aaa')

# NameError   找不到名字变量引起

# IndexError  使用序列中不存在的索引时引发
# l = [1,2,3]
# l[1000] # list index out of range

# KeyError  在使用映射中不存在的键时引发
# d = {}
# d['name']

# AttributeError   特性引用或赋值失败引发
# class Foo:
#     pass
# Foo.xxx

# ZeroDivisionError   在除法或模除操作的第二参数为0时引发
# 1/0

# TypeError:   内建操作或函数应用于错误类型的对象时引发
# for i in 3:
#     pass


# 3、异常
# 强调一：对于错误发生的条件如果是可以预知的，此时应该用if判断去预防异常。
AGE = 10
age = input('>>:').strip()

if age.isdigit():   # 预防异常 'aaa'
    age = int(age)
    if age > AGE:
        print('大了')
"""
>>:123
大了
"""

# 强调二：错误发生的条件如果是不可预知的，此时应该用异常处理机制，try...except
try:  # try代表监测
    f = open('/Users/hqs/Desktop/conf_test.ini', 'r', encoding='utf-8')
    # 由于f对象具备__next__()、__iter__()说明f是一个迭代器对象
    print(next(f), end='')  # end=''去掉回车符号
    print(next(f), end='')
    print(next(f), end='')
    print(next(f), end='')
    print(next(f), end='')
    print(next(f), end='')
    print(next(f), end='')
    print(next(f), end='')
    print(next(f), end='')
    print(next(f), end='')
    print(next(f), end='')
    print(next(f), end='')
    f.close()
except StopIteration:
    print("出错了")

print('=====》1')
print('=====》2')
print('=====》3')
"""
[group1]
k1 = v1

[group2]
k1 = v1

出错了
=====》1
=====》2
=====》3
"""