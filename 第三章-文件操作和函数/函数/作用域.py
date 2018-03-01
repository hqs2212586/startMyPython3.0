
'''
作用域：
    python中一个函数就是一个作用域，局部变量放置在其作用域中
    C# Java中作用域｛｝
    代码定义完成后，作用域已经完成，作用域链向上查找
'''
age = 18
def func1():
    age = 73
    def func2():
        age = 84
        print(age)

    return 666

val = func1()
print(val)
'''
输出：666
'''
# 函数名可以当作返回值
age = 18
def func1():
    age = 73
    def func2():...
    return func2   # 返回一个函数名# val = func1()
print(val)
'''
输出：<function func1.<locals>.func2 at 0x101462598>
'''

# 代码写完之后作用域已经生成，不管函数名传到哪里，只要执行都回回定义的地方往上找
age = 18
def func1():
    age = 73
    def func2():
        print(age)
    return func2   # 返回一个函数名不带括号

val = func1()
val()
'''
输出结果：73
'''