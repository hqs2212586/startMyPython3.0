# 注意写'__'开头，不要加'__'结尾，这样写是python内置的功能。

# class A:
#     __x = 1  # _A__x = 1
#
#     def __init__(self, name):
#         self.__name = name  # self._A__name='egon'
#
#     def __foo(self):   # _A__foo
#         print('%s foo run' % self.__name)
#
#     def bar(self):
#         self.__foo()  # self._A__foo()
#         print('from bar')
#
# # 无法找到类的属性和函数：
# # print(A.__x)
# # print(A.__foo)
#
# print(A.__dict__)
# a = A('egon')
# #a._A__foo()  # 通过这种方式可以访问类隐藏函数
# a.bar()
"""
在前面加'__'，在类定义阶段就发生了变形，变形后在外部就无法通过.__func来调用。 
这种变形的特点：
    1、在类外部无法直接obj.__AttrName ————因为名字已经改变了，在了解变形规则的情况下可以调用隐藏属性和方法
    2、在类内部可以直接使用：obj.__AttrName
    3、子类无法覆盖父类__开头的属性
"""
# class Foo:
#     def __func(self):   # _Foo_func
#         print('from foo')
#
#
# class Bar(Foo):
#     def __func(self):   # _Bar__func
#         print('from bar')
#
# b = Bar()
# # b.func()   # AttributeError：没有这个属性
# b._Bar__func()  # 输出：from bar

"""
总结这种变形需要注意的问题：
    1、知道了类名和属性名就可以拼出名字：_类名__属性，然后就可以访问了
    2、变形的过程只在类的定义时发生一次，定义后的赋值操作，不会变形
    3、在继承中，父类如果不想让子类覆盖自己的方法，可以将方法定义为私有的
"""



# class B:
#     __x = 1
#
#     def __init__(self, name):
#         self.__name = name
#
# # 验证问题一：
# print(B._B__x)

# 验证问题二：
# B.__y = 2   # '__'开头只在类定义阶段才会发生变形，类定义之后不变
# print(B.__dict__)
# b = B('egon')
# print(b.__dict__)
#
# b.__age = 18
# print(b.__dict__)
# print(b.__age)

# 验证问题三：
class A:
    def __foo(self):  # _A__foo
        print('A foo')

    def bar(self):
        print('A.bar')
        self.__foo()  # self._A__foo()

class B(A):
    def __foo(self):  # _B__foo
        print('B.foo')

b = B()
b.bar()
"""
A.bar
A foo  # 只在自己类找方法不去其他类查找，子类不覆盖父类方法
"""

