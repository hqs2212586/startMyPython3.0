# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

class Str:
    def __init__(self,name):
        self.name=name
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->',instance,value)
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)


class People:
    name=Str('name')
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People('egon',18,3231.3)

#调用
print(p1.__dict__)
p1.name
"""
set---> <__main__.People object at 0x10402cba8> egon
{'name': 'egon', 'age': 18, 'salary': 3231.3}
get---> <__main__.People object at 0x10402cba8> <class '__main__.People'>
"""

#赋值
print(p1.__dict__)
p1.name='egonlin'
print(p1.__dict__)
"""
{'name': 'egon', 'age': 18, 'salary': 3231.3}
set---> <__main__.People object at 0x10402cc18> egonlin
{'name': 'egonlin', 'age': 18, 'salary': 3231.3}
"""

#删除
print(p1.__dict__)
del p1.name
print(p1.__dict__)
"""
{'name': 'egonlin', 'age': 18, 'salary': 3231.3}
delete---> <__main__.People object at 0x10402cba8>
{'age': 18, 'salary': 3231.3}
"""