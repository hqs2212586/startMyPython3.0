# 改变对象的字符串显示__str__, __repr__
# 自定制格式化字符串__format__

# d = dict({'name' : 'egon'})
# print(isinstance(d, dict))  # True,d是dict类的实例
# print(d)
#
# class Foo:
#     pass
# obj = Foo()
# print(obj)
""" 同样是打印对象，显示形式完全不同，打印总是希望像前一种有提示功能。
{'name': 'egon'}
<__main__.Foo object at 0x10401ad68>
"""

# __str__方法定义后，会在打印对象的时候，触发这个对象下的__str__方法，把字符串的结果作为打印的结果
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):  # 必须return一个字符串
#         # print("触发__str__方法：")
#         return '<name:%s,age:%s>' %(self.name, self.age)
#
#
# obj = People('egon', 18)
# print(obj)
"""
<name:egon,age:18>
"""



# __del__

# f = open('settings.py') # 应用程序（变量）、操作系统(打开变量)
# # 关闭文件是为了收回内存空间，Python自己的垃圾回收机制，只能回收自己的变量，不能回收操作系统的资源
# f.read()
# f.close() # 给操作系统发信号关闭，回收操作系统的资源
#
# print(f)
"""
<_io.TextIOWrapper name='settings.py' mode='r' encoding='UTF-8'>
"""

class Open():
    def __init__(self, filename):
        print('open file .....')
        self.filename = filename

    def __del__(self):  # 回收操作系统资源
        print('回收系统资源')

f = Open('setting.py')
# del f   # f.__del__()
print('--------main--------')
"""
open file .....
--------main--------
del......   # 程序结束后，__del__回收操作系统资源
"""

