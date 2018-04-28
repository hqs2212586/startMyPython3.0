"""
继承指的是类与类之间的关系，继承的功能之一就是可以用来解决代码重用问题。
继承是一种创建新类的方式，在python中，新建的类可以继承一个或多个父类（其他语言只能继承一个父类），父类又可以称为基类或者超类
                                 新建的类称为派生类或子类。
"""


# class ParentClass1:
#     pass
#
#
# class ParentClass2:
#     pass
#
#
# class SubClass1(ParentClass1):  # 单继承，基类是ParentClass1，派生类是SubClass
#     pass
#
#
# class SubClass2(ParentClass1, ParentClass2):   # 多继承，用逗号分隔开多个继承的类
#     pass


"""
__base__只查看从左到右继承的第一个子类
__bases__查看所有继承的父类
"""
# print(ParentClass1.__base__, type(ParentClass1.__base__))
# print(SubClass2.__base__, type(SubClass2.__base__))
"""
<class 'object'> <class 'type'>
<class '__main__.ParentClass1'> <class 'type'>
"""

# print(SubClass1.__bases__)
# print(SubClass2.__bases__)
"""数据结构为元组
(<class '__main__.ParentClass1'>,)
(<class '__main__.ParentClass1'>, <class '__main__.ParentClass2'>)
"""


# 继承与抽象（先抽象再继承）
"""
抽象即抽取类似或者说比较像的部分
抽象分为两个层次：
    1、将奥巴马和梅西者俩对象比较像的部分抽取成类；
    2、将人，猪，狗这三个类比较像的部分抽取成父类。
    
抽象最主要的作用是划分类别（可以隔离关注点，降低复杂度），

继承：是基于抽象的结果，通过编程语言去实现它，肯定是先经历抽象这个过程，才能通过继承的方式去表达出抽象的结构。

抽象只是分析和设计的过程中，一个动作或者说一种技巧，通过抽象可以得到类。
"""


# class Hero:
#     def __init__(self, nickname, life_value, aggresivity):
#         self.nickname = nickname
#         self.life_value = life_value
#         self.aggresivity = aggresivity
#
#     def attack(self, enemy):
#         enemy.life_value -= self.aggresivity
#
#
# class Garen(Hero):
#     pass
#
#
# class Riven(Hero):
#     pass
#
# g1 = Garen('刚哥', 29, 30)
# print(g1.__dict__)
"""
{'nickname': '刚哥', 'life_value': 29, 'aggresivity': 30}
"""

# 属性查找小练习
class Foo:
    def f1(self):
        print('from Foo.f1')

    def f2(self):
        print('from Foo.f2')
        self.f1()


class Bar(Foo):
    def f2(self):
        print('from Bar.f2')

b = Bar()
print(b.__dict__)  # 未定义__init__没有自己的属性  字典内为空
b.f1()   # 指向父类的函数
b.f2()   # 指向子类重用的函数
"""
{}
from Foo.f1
from Bar.f2   # 注意和父类中的区别
"""
