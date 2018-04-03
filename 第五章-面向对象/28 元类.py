# http://www.cnblogs.com/linhaifeng/articles/8029564.html
# 储备知识exec：有下面三个参数
# 参数一：字符串形式的命令
# 参数二：全局作用域（字典形式），如果不指定默认使用globals()
# 参数三：局部作用域(字典形式)，如果不指定默认就使用locals()

# 格式：exec(object, globals, locals)
# g = {
#     'x':1,
#     'y':2
# }
#
# l = {}
#
# exec("""
# global x,m
# x=10
# m=100
#
# z=3
# """, g, l)
#
# print(g)
#
# print(l)
"""
{'z': 3}
"""

# python一切皆对象，对象可以怎么用？
# 1、都可以被引用，x=obj
# 2、都可以当作函数的参数传入
# 3、都可以当作函数的返回值
# 4、都可以当作容器类的元素，l=[func, time, obj, 1]
# 换句话说，符合上述条件就是一个对象

# 类也是对象（对象是由一个类实例化出来的）

# 元类是类的类，是类的模板
# 元类是用来控制如何创建类的，正如类是创建对象的模板一样，而元类的主要目的是为了控制类的创建行为
# 元类的实例化的结果为我们用class定义的类，正如类的实例为对象(f1对象是Foo类的一个实例，Foo类是 type 类的一个实例)
# type是python的一个内建元类，用来直接控制生成类，python中任何class定义的类其实都是type类实例化的对象

# 产生类的类称之为元类，默认所有用class定义的类，他们的元类是type
class Bar:
    pass
print(type(Bar))
"""
<class 'type'>
"""

# 定义类的两种方式：
# 方式一：class
# class Chinese:  # 这个类其实是元类实例化的一个对象
#     country = 'China'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def talk(self):
#         print('%s is talking' % self.name)




# 方式二：type
# 定义类的三要素：类名、类的基类们、类的名称空间
class_name = ' Chinese'
class_bases = (object, )
class_body = """
country = 'China'

def __init__(self,name,age):
    self.name = name
    self.age = age
    
def talk(self):
    print('%s is talking' % self.name)
"""

class_dic = {}
exec(class_body, globals(), class_dic)
print(class_dic)
"""输出：
<class 'type'>
{'country': 'China', '__init__': <function __init__ at 0x101d62e18>, 'talk': <function talk at 0x101db3620>}
"""
Chinese = type(class_name, class_bases, class_dic)  # 元类实例化得到一个元类的对象，等同于class声明的类
print(Chinese)
"""
<class '__main__. Chinese'>
"""
obj = Chinese('egon', 18)
print(obj,obj.name, obj.age)
"""
<__main__. Chinese object at 0x10401af98> egon 18
"""

