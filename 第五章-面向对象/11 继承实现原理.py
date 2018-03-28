# Python对于定义的每一个类，都会计算出一个方法解析顺序(MRO)列表
# 这个MRO列表就是一个简单的所有基类的线性顺序列表
"""
Python会在MRO列表上从左到右开始查找基类，直到找到第一个匹配这个属性的类为止。
    这个MRO列表的构造是通过一个C3线性化算法来实现的
    这个算法就是合并所有父类的MRO列表并遵循如下三个准则：
    1、子类会先于父类被检查
    2、多个父类会根据它们在列表中的顺序被检查
    3、如果对下一个类存在两个合法的选择，选择第一个父类
"""

# Python2中分新式类和经典类，Python3中统一都为新式类

# Python2中经典类：没有继承object的类，以及它的子类

class Foo:
    pass

class Bar(Foo):
    pass

# python2中新式类：继承object的类，以及它的子类都称为新式类
class Foo(object):
    pass

class Bar(Foo):
    pass

"""
>>> class Foo:pass
...
>>> Foo.__bases__
()
>>> class Foo(object):pass
...
>>> Foo.__bases__
(<type 'object''>,)
"""


# python3中新式类：一个类没有继承object类，默认就继承object
class Foo():
    pass


print(Foo.__bases__)
