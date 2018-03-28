"""
补充说明：
    1、站的角度不同，定义出的类截然不同
    2、现实中的类并不完全等于程序中的类，比如现实中的公司类，往往会在程序中拆分为部门类，业务类等；
    3、有时为了编程的需求，程序中也可能会定义现实中不存在的类，比如策略类（现实中不存在，但在程序中却非常常见的类）
"""


class student:
    school = 'whu'


# python当中一切皆对象，在python3中统一了类和类型的概念
print(list)
print(dict)

print(student)
"""
<class 'list'>
<class 'dict'>
<class '__main__.student'>
"""

l1 = [1, 2, 3]
l2 = list([1, 2])

l1.append(4)   # 对象调用绑定方法append
list.append(l2, 4)   # list类的方法append来对对象添加元素
print(l1, l2)
"""
[1, 2, 3, 4] [1, 2, 4]
"""