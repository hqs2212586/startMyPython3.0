# 知识储备__call__方法
# class Foo:
#     def __call__(self, *args, **kwargs):
#         print(self)
#         print(args)
#         print(kwargs)
#     pass
#
# obj=Foo()
# # obj()
# # 没有__call__方法前，obj() 报错：TypeError: 'Foo' object is not callable（不可调用）
# obj(1, 2, 3, a=1, b=2, c=3)
"""
<__main__.Foo object at 0x101eb6390>
(1, 2, 3)
{'a': 1, 'b': 2, 'c': 3}
"""
# 由此推出元类中也应有一个__call__方法，会在调用Foo时触发执行
# Foo(1,2,x=1)   # Foo.__call__(Foo,1,2,x=1)


class Mymeta(type):   # 自定义元类，大多数属性依然是继承的type
    def __init__(self, class_name, class_bases, class_dic):
        # print(class_name)  # 类名：Chinese
        # print(class_bases)  # 基类：(<class 'object'>,)
        # print(class_dic)  # 类的名称空间：{'__module__': '__main__', '__qualname__': 'Chinese', 'country': 'China', '__init__': <function Chinese.__init__ at 0x101f201e0>, 'talk': <function Chinese.talk at 0x101f20378>}

        # 自订制控制类的行为
        if not class_name.istitle():  # istitle()判断首字母大写
            raise TypeError('类名的首字母必须大写')# 主动报错的关键字是raise

        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError("必须有注释，且注释不能为空")

        super(Mymeta, self).__init__(class_name, class_bases, class_dic)  # 重用父类功能

    def __call__(self, *args, **kwargs):  # obj = Chinese('egon',age=18)
        print(self)  # self = Chinese
        print(args)   # args = ('egon',)
        print(kwargs)   # kwargs = {'age': 18}

        # 第一件事：实例化先造一个空对象obj
        obj = object.__new__(self)
        # 第二件事：初始化obj
        self.__init__(obj, *args, **kwargs)
        # 第三件事：返回obj
        return obj

class Chinese(object, metaclass=Mymeta):  # 元类为Mymeta的类的创建可受人控制
    """
    中国人的类
    """
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)

# obj = Chinese('egon', 18)  # Chinese.__call__(Chinese, 'egon', 18)

obj = Chinese('egon', age=18)   # 实例化的行为
"""
<class '__main__.Chinese'>
('egon',)
{'age': 18}
"""

# print(obj.__dict__)
"""
{'name': 'egon', 'age': 18}
"""