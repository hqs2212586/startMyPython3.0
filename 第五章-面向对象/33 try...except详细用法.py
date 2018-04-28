# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 1、异常类只能用来处理指定的异常情况，如果非指定异常则无法处理
# s1 = 'hello'
# try:
#     int(s1)
# except IndexError as e:  # 未捕获到异常，程序直接报错
#     print(e)
# """
# ValueError: invalid literal for int() with base 10: 'hello'
# """

# 2、多分支：被监测的代码抛出的异常有多种可能性，并且需要针对每一种异常类型都定制专门的处理逻辑
# try:
#     print('====>1')
#     #name
#     print('====>2')
#     l = [1, 2, 3]
#     #l[100]
#     print('====>3')
#     d = {}
#     d['name']
#     print('====>4')
#
# except NameError as e:  # as将异常类型的值赋值给e
#     print('-=---->NameError', e)
# except IndexError as e:
#     print('---->', e)
# except KeyError as e:
#     print('---->', e)
# print('====》after code')

# 3、万能异常：Exception涵盖各种各样的异常类型
# 使用场景：被监测的代码块抛出的异常有多种可能，并且针对所有异常类型都只用一种处理逻辑。
# try:
#     print('====>1')
#     # name
#     print('====>2')
#     l = [1, 2, 3]
#     l[100]
#     print('====>3')
#     d = {}
#     d['name']
#     print('====>4')
# except Exception as e:
#     print('异常发生', e)
# print('+++++>after code')
"""
====>1
====>2
异常发生 list index out of range
+++++>after code
"""

# 4、多分支和万能异常组合使用：
# try:
#     print('====>1')
#     #name
#     print('====>2')
#     l = [1, 2, 3]
#     #l[100]
#     print('====>3')
#     d = {}
#     d['name']
#     print('====>4')
#
# except NameError as e:  # as将异常类型的值赋值给e
#     print('-=---->NameError', e)
# except IndexError as e:
#     print('---->', e)
# except KeyError as e:
#     print('---->', e)
# except Exception as e:
#     print('统一处理方法')
#
# print('====》after code')

# 5、异常的其他结构else\finaly
try:
    print('====>1')
    #name
    print('====>2')
    l = [1, 2, 3]
    #l[100]
    print('====>3')
    d = {}
    #d['name']
    print('====>4')

except NameError as e:  # as将异常类型的值赋值给e
    print('-=---->NameError', e)
except IndexError as e:
    print('---->', e)
except KeyError as e:
    print('---->', e)
except Exception as e:
    print('统一处理方法')

else:
    print('在被监测的代码块没有发生异常时执行')
finally:                        # 通常是用于回收资源等方面
    print('不管被监测的代码有没有发生异常都会执行')

print('====》after code')
"""
====>1
====>2
====>3
====>4
在被监测的代码块没有发生异常时执行
====》after code
"""

# 6、主动触发异常：raise  异常类型（值）
class People:
    def __init__(self, name, age):
        if not isinstance(name, str):   # 不让实例化
            raise TypeError('名字必须传入str类型')
        if not isinstance(age, int):
            raise TypeError('年龄必须传入int类型')
        self.name = name
        self.age = age


p1 = People('egon', '18')
p2 = People(12, 18)
p3 = People('egon', 18)
"""
Traceback (most recent call last):
  File "/Users/.../33 try...except详细用法.py", line 126, in <module>
    p1 = People('egon', '18')
  File "/Users/.../33 try...except详细用法.py", line 121, in __init__
    raise TypeError('年龄必须传入int类型')
TypeError: 年龄必须传入int类型
"""

# 7、自定义异常类型
class MyException(BaseException):   # 继承异常类型
    def __init__(self, msg):
        super(MyException, self).__init__()
        self.msg = msg

    def __str__(self):
        return '<%s>' % self.msg   # 异常的值

# 主动触发异常，追踪信息和异常类型  # print(obj)
raise MyException('我自己的异常类型')
"""
Traceback (most recent call last):
  File "/Users/.../33 try...except详细用法.py", line 148, in <module>
    raise MyException('我自己的异常类型')
__main__.MyException
"""
"""
Traceback (most recent call last):
  File "/Users/.../33 try...except详细用法.py", line 148, in <module>
    raise MyException('我自己的异常类型')
__main__.MyException: <我自己的异常类型>
"""


# 8、assert断言  是声明其布尔值必须为真的判定，发生异常则为假。
# 语法格式：assert expression  等价于
# if not expresstion:
#     raise AssertionError

info = {}
info['name'] = 'egon'
info['age'] = 18

# if 'name' not in info:
#     raise KeyError('必须有name这个key')
#
# if 'age' not in info:
#     raise KeyError('必须有age这个key')
# 用assert取代上述代码：
assert ('name' in info) and ('age' in info)

if info['name'] == 'egon' and info['age'] > 10:
    print('welcome')
"""
welcome
"""

# 9、总结try...except使用
# （1）把错误处理和真正的工作分开来
# （2）代码更易组织，更清晰，复杂的工作任务更容易实现
# （3）更安全了，不至于因为一些小的疏忽而使程序意外崩溃了
