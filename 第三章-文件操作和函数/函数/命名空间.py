'''
    命名空间（name space），若变量x=1,1存放在内存中，命名空间是存放名字x、x与1绑定关系的地方。
    命名空间分三种：
        locals：函数内的名称空间，包括局部变量和形参
        globals：全局变量，函数定义所在模块的名字空间
        builtins：内置模块的名字空间   dir(__builtins__)查看所有内置方法

    不同变量的作用域不同就是由这个变量所在的命名空间决定的
    作用域即范围：
        全局范围：全局存活，全局有效
        局部范围：临时存活，局部有效


'''


'''
    作用域的查找顺序：
    LEGB：locals  enclosing(相邻的上一级)  globals   __builtins__
'''
n = 10
def fun1():
    n = 20
    print('func1',n)

    def fun2():
        n = 30
        print('func2',n)

        def func3():
            print("func3",n)    # locals没有，先找相邻上一级作用域
        func3()  # 20
    fun2()  # 30
fun1()  # 30