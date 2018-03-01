"""
    在函数里面又套了一层子函数，在外层函数被执行时，子函数被返回，返回的内存地址
    函数外部执行子函数时却又引用了外层函数的变量，
    相当于子函数跟外层函数关系纠结不清，这种关系就是闭包。类似如下代码：
"""


def func():
    n = 10

    def func2():
        print("func2:",n)
    return func2

f = func()
print(f)  # func2内存地址
f()   # 输出func2: 10
