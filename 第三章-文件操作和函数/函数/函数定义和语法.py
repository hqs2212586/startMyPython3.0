"""
    函数一词来源于数学，编程中的"函数"与数学中的函数与欧很大的不同。
    （BASIC中叫subroutine，C中叫function，java中叫method）
    定义：函数是指将一组语句的集合通过一个名字（函数名）封装起来，想执行这个函数，只需调用其函数名即可。
    特性：1、减少重复代码
         2、使程序变得可扩展
         3、使得程序变得易维护
"""
# 无参函数
def sayhi(): # 函数名(小写即可)
    print("Hello,I'm nobody!")

sayhi()   # 调用函数，函数名指向上述代码指向的内存位置，加上括号才是执行代码
print(sayhi)   # 函数sayhi指向的内存地址

# 单个参数的函数
def sayhi(name):
    print("hello",name)
    print("my name is black girl....", name)
sayhi("tracy")

# 多个参数函数
def calc(x,y):   # 定义算数函数
    res = x**y
    return res   # 返回函数执行结果
a,b = 5,8
c = calc(a,b)    # 结果赋值给变量c
print(c)
calc(2,10)       # 直接写入参数