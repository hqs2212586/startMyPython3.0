# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 练习一：在元类中控制把自定义类的数据属性都变成大写
# class Mymetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         update_attrs={}
#         for k,v in attrs.items():
#             if not callable(v) and not k.startswith('__'):
#                 update_attrs[k.upper()] = v
#             else:
#                 update_attrs[k]=v
#         return type.__new__(cls, name, bases, update_attrs)
#
# class Chinese(metaclass=Mymetaclass):
#     country = 'China'            # 需要大写的数据属性
#     tag = 'Legend of the Dragon'
#     def walk(self):
#         print('%s is walking' %self.name)
#
# print(Chinese.__dict__)
"""
{'__module__': '__main__',
 'COUNTRY': 'China', 
 'TAG': 'Legend of the Dragon',
 'walk': <function Chinese.walk at 0x1040211e0>,
 '__dict__': <attribute '__dict__' of 'Chinese' objects>, 
 '__weakref__': <attribute '__weakref__' of 'Chinese' objects>, 
 '__doc__': None}
"""


class Mymetaclass(type):

    def __call__(self, *args, **kwargs):
        if args:
            raise TypeError('must use keyword argument for key function')
        obj = object.__new__(self)  # 创建对象，self为类Foo

        for k,v in kwargs.items():
            obj.__dict__[k.upper()] = v
        return obj


class Chinese(metaclass=Mymetaclass):
    country = 'China'            # 需要大写的数据属性
    tag = 'Legend of the Dragon'
    def walk(self):
        print('%s is walking' %self.name)

p=Chinese(name='Jack', age=18, sex='male')
print(Chinese.__dict__)
"""
{'__module__': '__main__', 
'country': 'China', 
'tag': 'Legend of the Dragon', 
'walk': <function Chinese.walk at 0x1040211e0>, 
'__dict__': <attribute '__dict__' of 'Chinese' objects>, 
'__weakref__': <attribute '__weakref__' of 'Chinese' objects>, 
'__doc__': None}
"""