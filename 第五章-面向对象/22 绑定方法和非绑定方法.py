"""
在类内部定义的函数，分为两大类：
    一、绑定方法：绑定给谁，就应该由谁来调用，##谁来调用就会把调用者当作第一个参数自动传入##
        绑定到对象的方法：在类内定义的没有被任何装饰器修饰的

        绑定到类的方法：在类内定义的被装饰器@classmethod修饰的方法

    二、非绑定方法：没有自动传值的说法，就是类中定义的一个普通工具，对象和类都可以使用
        非绑定方法：不与类或对象绑定
"""
class Foo:
    def __init__(self, name):
        self.name = name

    def tell(self):  # 绑定了对象的函数
        print('名字是%s' % self.name)

    @classmethod
    def func(cls):  # 绑定了类的方法，默认传入参数是类本身
        print(cls)

    @staticmethod
    def func1(x, y):   # 在类内部的普通函数
        print(x+y)

f = Foo('egon')
print(Foo.tell)
print(f.tell)
"""
<function Foo.tell at 0x104021378>
<bound method Foo.tell of <__main__.Foo object at 0x101fb6390>>
"""
print(Foo.func)
"""
<bound method Foo.func of <class '__main__.Foo'>>
"""
Foo.func()
"""
<class '__main__.Foo'>
"""

print(Foo.func1)
f.func1(1, 3)
Foo.func1(2, 4)
"""
<function Foo.func1 at 0x104021488>
4
6
"""