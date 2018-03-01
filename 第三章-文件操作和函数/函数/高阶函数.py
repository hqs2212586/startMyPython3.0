'''
    高阶函数：一个函数就可以接收另一个函数作为参数（变量可以指向函数，函数的参数能接收变量）
    满足以下任意条件可以判断是高阶函数：
        1、接受一个或多个函数作为输入
        2、return返回另外一个函数
'''
# 下述例子说明变量可以指向函数
'''
def calc(x):
    return x*x
f = calc
print(f(2))
'''

# 下述例子说明函数的参数能接收变量
def func(x,y):
    return x+y
def calc(x):
    return x

n = func
print(calc(n))
# 输出：<function func at 0x101a62ea0>

# 下述例子是函数返回函数
def func2(x,y):
    return abs,x,y    # abs()函数求绝对值；返回结果包含一个函数的函数就是高阶函数
res = func2(3,-10)
print(res[0](res[1]+res[2]))
# 输出结果：7