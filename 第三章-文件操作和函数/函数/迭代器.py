"""
可以直接作用于for循环的数据类型有以下几种：
    集合数据类型：list、tuple、dict、set、str等
    生成器（generator），包括生成器和带yield的函数生成器

定义：可直接作用于for循环的对象统称为可迭代对象：Iterable
"""

from collections import Iterable  # 可迭代类型
# 使用isinstance()判断一个对象是否是可迭代对象
isinstance('abc', Iterable)
isinstance({}, Iterable)
isinstance((x for x in range(10)), Iterable)

isinstance(100, Iterable)  # 返回False

"""
定义：可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
    生成器是迭代器的一种：
    1、生成器都是迭代器对象，但list\dict\str虽然是可迭代对象，但不是迭代器。
    2、把list\dict\str等可迭代对象变成迭代器可以使用iter()函数
>>> from collections import Iterator
>>> isinstance('abc', Iterator)  
False
>>> a = iter('abc')
>>> a
<str_iterator object at 0x10c584b38>
>>> a.__next__()
'a'
"""