# 需要：列表[0,1,2,3,4,5,6,7,8,9],需要将列表每个值加1
# 方法一：
a = [0,1,2,3,4,5,6,7,8,9]
b = []
for i in a:b.append(i+1)
a = b
print(a)
'''
    此方法内存中会同时有两份列表，不适合处理大规模数据
'''

# 方法二：
a = [0,1,2,3,4,5,6,7,8,9]
for index,i in enumerate(a):
    a[index] += 1
print(a)

# 方法三:
a = [0,1,2,3,4,5,6,7,8,9]
a = map(lambda x:x+1, a)  # <map object at 0x1018da5f8>
print(a)

# 方式四：列表生成式
a = [i+1 for i in range(10)] # 一行代码完成列表操作

a = [i if i < 5 else i*i for i in a]
print(a)  # [1,2,3,4,25,36,49,64,81,100]


# 生成器保存的是公式，取一次创建一次，只能往前不能后退
'''
>>> a2 = (i for i in range(1000))
>>> a2
<generator object <genexpr> at 0x103761a98>
>>> next(a2)
0
>>> next(a2)
1
'''

#生成器走完时，会报错：StopIteration
'''
>>> a3 = (i for i in range(5))   # 限制5个
>>> a3
<generator object <genexpr> at 0x103761e08>
>>> next(a3)
0
>>> next(a3)
1
>>> next(a3)
2
>>> next(a3)
3
>>> next(a3)
4
>>> next(a3)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
StopIteration

'''

a3 = (i for i in range(5))
for i in a3:   # 使用for循环来迭代生成器，不会出现StopIteration报错，直接结束。
    print(i)
'''
0
1
2
3
4
'''
# a2 = (i for i in range(3))
# while True:    # while循环不适用
#     next(a2)   # 报StopIteration错误

# Python3中：
range(10)  # range(0,10)  生成这个公式没有正式创建
type(range(10))  # <class 'range'>
# Python2中：
# range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# xrange(10)  # xrange(10)  等同于Python3中的range()
'''
Python2
    range = list
    xrange = 生成器
Python3
    range = 生成器
    xrange 没有
    
生成器的创建方式
    1.列表  列表生成式
    2.函数  函数生成器 yield
    
yield  对比  return
    return返回并中止function
    yield返回函数，并冻结当前的执行过程
    next唤醒冻结的函数执行过程，继续执行，直到遇到下一个yield

函数有了yield之后
    1、函数名加()就变成了一个生成器
    2、return在生成器里，代表生成器的中止，直接报错
    
next:唤醒生成器并继续执行
send("stop"):
    1.唤醒并继续执行
    2.发送一个信息到生成器内部
'''