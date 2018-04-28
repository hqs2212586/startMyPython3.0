# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


class Foo(object):
    staticField = "old boy"

    def __init__(self):
        self.name = 'wupeiqi'

    def func(self):
        return 'func'

    @staticmethod
    def bar():
        return 'bar'


print(getattr(Foo, 'staticField'))
print(getattr(Foo, 'func'))
print(getattr(Foo, 'bar'))
"""
old boy
<function Foo.func at 0x1040211e0>
<function Foo.bar at 0x104021378>
"""