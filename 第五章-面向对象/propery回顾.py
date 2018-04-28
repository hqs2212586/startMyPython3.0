# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

class Room:
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length

    @property
    def area(self):
        return self.width * self.length

r1=Room('alex',1,1)
print(r1.area)
"""
1
"""