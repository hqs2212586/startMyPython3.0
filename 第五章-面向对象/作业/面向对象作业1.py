# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 1.面向对象三大特性，各有什么用处，说说你的理解。
"""
继承：解决代码重用问题
多态：为了类在继承和派生的时候，保证使用家谱中任一类的实例的某一属性时可以正确调用。
封装：明确区分内外，控制外部对隐藏属性的操作行为，隔离复杂度
"""
# 2.类的属性和对象的属性有什么区别?
"""
类的属性分为数据属性和函数属性。
类的数据属性时所有对象共享的，类的函数属性是绑定给对象用的，称为绑定到对象的方法。

对象的属性可能来自类定义，即类属性。（类定义自身、类定义继承两种途径）
对象的属性还可能是该对象实例定义的，即对象属性
"""

# 3.面向过程编程与面向对象编程的区别与应用场景?
"""
面向过程的程序设计的核心是过程（流水线式思维），过程即解决问题的步骤，面向过程的设计就
好比精心设计好一条流水线，考虑周全什么时候处理什么问题。
优点：复杂问题流程化，进而简单化。缺点：可扩展性和可维护性差
适用：一般用于那些功能一旦实现之后就很少需要改变的场景， 如果你只是写一些简单的脚本，去做一些一次性任务。

面向对象编程是利用“类”和“对象”来创建各种模型来实现对真实世界的描述。
与面向过程机械式的思维方式形成鲜明对比，面向对象更加注重对现实世界而非流程的模拟，是一种“上帝式”的思维方式。
优点：更容易扩展和修改，更容易理解  缺点：编程复杂度高、可控性差
适用：应用于需求经常变化的软件中，一般需求的变化都集中在用户层，互联网应用，企业内部软件，游戏等都是面向对象的程序设计大显身手的好地方。
"""

# 4.类和对象在内存中是如何保存的。
"""
以字典的方式保存，代码在类定义阶段便会执行，因而会产生新的名称空间，
用来存放类的变量名和函数名，可以通过__dict__查看。
__dict__查出字典，key为属性名，value为属性值
"""

# 5.什么是绑定到对象的方法、绑定到类的方法、解除绑定的函数、如何定义，如何调用，给谁用？有什么特性
"""
绑定到对象的方法：在类中定义没有加装饰器修饰的方法。
    对象.bound_method()  自动将对象当做第一个参数传入

绑定到类的方法：在类中定义的装饰器@classmethod修饰的方法。
    类.bound_method()   自动将类当第一个参数传入

非绑定方法：在类中用@staticmethod装饰器装饰的方法。
    没有自动传值，不绑定类和对象，类和对象均可调用。
"""

# 6.使用实例进行 获取、设置、删除 数据, 分别会触发类的什么私有方法
# item系列就是为了把对象模拟成像字典一样，就可以像字典一样访问
# class A(object):
#     def __getitem__(self, item):
#         return self.__dict__.get(item)
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         del self.__dict__[key]
#
# a = A()
#
# a['key'] = "val"
# print(a.__dict__)   # {'key': 'val'}
# b = a["key"]
# print(b)           # val
# del a["key"]
# print(a.__dict__)   # {}

# 7.python中经典类和新式类的区别
"""
在Python2中，没有显式继承object类的类，以及该类的子类都是经典类。 深度优先
python2中，显式地声明继承object类，以及该类的子类都是新式类。     广度优先
object是所有python类的基类，它提供了一些常见方法（如__str__）的实现。
在python3中，无论是否继承object，都默认继承object，即python3中所有类均为新式类
"""

# 8.如下示例, 请用面向对象的形式优化以下代码
"""
在没有学习类这个概念时，数据与功能是分离的
def exc1(host,port,db,charset):
   conn=connect(host,port,db,charset)
   conn.execute(sql)
   return xxx
def exc2(host,port,db,charset,proc_name)
   conn=connect(host,port,db,charset)
   conn.call_proc(sql)
   return xxx
   # 每次调用都需要重复传入一堆参数
   exc1('127.0.0.1',3306,'db1','utf8','select * from tb1;')
   exc2('127.0.0.1',3306,'db1','utf8','存储过程的名字')
"""
class exec:
    host = '127.0.0.1'
    port = 3306
    charset = 'utf-8'
    db = 'db1'
    sql = "select * from tb1;"
    proc_name = "存储过程的名字"
    def __init__(self, *args):
        self.args = args

    def connect(self):
        pass

    def exc(self):
        if self.args == self.sql:
            conn = self.connect(self.host, self.port, self.db, self.charset)
            res = conn.execute(self.sql)
            return res
        elif self.args == self.proc_name:
            conn = self.connect(self.host, self.port, self.db, self.charset, self.proc_name)
            res = conn.call_proc(self.sql)
            return res

ex = exec('select * from tb1;')
print(ex.__dict__)  # {'args': ('select * from tb1;',)}

# 9.示例1，现有如下代码，会输出什么：
"""
class People(object):
    __name = "luffy"
    __age = 18

p1 = People()
print(p1.__name, p1.__age)

答：会报错，AttributeError: 'People' object has no attribute '__name'
"""

# 10.示例2, 现有如下代码， 会输出什么：
"""
class People(object):

   def __init__(self):
       print("__init__")

   def __new__(cls, *args, **kwargs):
       print("__new__")
       return object.__new__(cls, *args, **kwargs)

People()
# 输出：
__new__
__init__
"""
"""
new： 对象的创建，是一个静态方法，第一个参数是cls。(想想也是，不可能是self，对象还没创建，哪来的self)
init ： 对象的初始化， 是一个实例方法，第一个参数是self。
call ： 为了将一个类实例当做函数调用，我们需要在类中实现__call__()方法,可以用来改变实例的内部成员的值.
先有创建，才有初始化。即先new，而后init。
"""

# 11.请简单解释Python中 staticmethod（静态方法）和 classmethod（类方法）, 并分别补充代码执行下列方法。
"""
staticmethod（静态方法）：又称为非绑定方法，不与类和对象绑定，就是一个普通方法，不会自动传值。
classmethod(类方法)：是绑定到类的方法，自动将类作为第一个参数传入
"""
class A(object):
    def __init__(self, name):
        self.name = name

    def foo(self, x):
       print("executing foo(%s, %s)" % (self,x))

    @classmethod
    def class_foo(cls, x):
       print("executing class_foo(%s, %s)" % (cls,x))

    @staticmethod
    def static_foo(x):
       print("executing static_foo(%s)" % (x))

a = A('hqs')
a.foo('alex')
A.class_foo('alex')
a.static_foo('alex')
# A.static_foo('alex')
"""
executing foo(<__main__.A object at 0x10402cc50>, alex)
executing class_foo(<class '__main__.A'>, alex)
executing static_foo(alex)
executing static_foo(alex)
"""

# 12.请执行一下代码，解释错误原因，并修正错误。
# class Dog(object):
#
#    def __init__(self,name):
#        self.name = name
#
#    @property
#    def eat(self):
#        print(" %s is eating" %self.name)
#
# d = Dog("ChenRonghua")
# d.eat()
"""
TypeError: 'NoneType' object is not callable
因为eat方法添加了@property装饰器，将函数属性伪装得像数据属性一样被用户访问。
修改方法：去掉d.eat后面的括号即可。
"""
# d.eat
# 输出： ChenRonghua is eating


# 13.下面这段代码的输出结果将是什么？请解释。
# class Parent(object):
#    x = 1
#
# class Child1(Parent):
#    pass
#
# class Child2(Parent):
#    pass
#
# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)

# 1 1 1 继承自父类的类属性x，所以都一样，指向同一块内存地址
# 1 2 1 更改Child1，Child1的x指向了新的内存地址
# 3 2 3 更改Parent，Parent的x指向了新的内存地址


# 14.多重继承的执行顺序，请解答以下输出结果是什么？并解释。
# class A(object):
#     def __init__(self):
#         print('A')
#         super(A, self).__init__()
#
# class B(object):
#     def __init__(self):
#         print('B')
#         super(B, self).__init__()
#
# class C(A):
#     def __init__(self):
#         print('C')
#         super(C, self).__init__()
#
# class D(A):
#     def __init__(self):
#         print('D')
#         super(D, self).__init__()
#
# class E(B, C):
#     def __init__(self):
#         print('E')
#         super(E, self).__init__()
#
# class F(C, B, D):
#     def __init__(self):
#         print('F')
#         super(F, self).__init__()
#
# class G(D, B):
#     def __init__(self):
#         print('G')
#         super(G, self).__init__()
#
# if __name__ == '__main__':
#     #g = G()
#     #f = F()
#     print(G.mro())
#     print(F.mro())
"""新式类广度优先，super不管当前类的继承关系，会按照实例化的类的MRO列表，一直往后找。
G D A B
F C B D A
[<class '__main__.G'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
[<class '__main__.F'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.A'>, <class 'object'>]
"""

# 15.请编写一段符合多态特性的代码.
"""
多态性指在不考虑实例类型的情况下使用实例，多态性分为静态多态性和动态多态性。
静态多态性：就是在系统编译期间就可以确定程序执行到这里将要执行哪个函数

动态多态性：则是利用虚函数实现了运行时的多态，也就是说在系统编译的时候并不知道程序将要调用哪一个函数，
            只有在运行到这里的时候才能确定接下来会跳转到哪一个函数的栈帧。
"""
# import abc
# class Animal(metaclass=abc.ABCMeta):   # metaclass元类
#     def __init__(self, name):
#         self.name = name
#
#     @abc.abstractclassmethod    # 定义抽象方法，无需实现功能
#     def talk(self):
#         pass
#
# class People(Animal):
#     def talk(self):
#         print('people %s is talking loudly' % self.name)
#
# class Pig(Animal):
#     def talk(self):
#         print('pig %s is talking' % self.name)
#
# class Dog(Animal):
#     def talk(self):
#         print('Dog %s is talking' % self.name)
#
# def func(animal):
#     animal.talk()
#
# s = Dog('was')
# func(s)


# 16.很多同学都是学会了面向对象的语法，却依然写不出面向对象的程序，原因是什么呢？
# 原因就是因为你还没掌握一门面向对象设计利器，即领域建模，请解释下什么是领域建模，
# 以及如何通过其设计面向对象的程序？http://www.cnblogs.com/alex3714/articles/5188179.html 此blog最后面有详解
"""
    领域模型,顾名思义,就是需求所涉及的领域的一个建模,更通俗的讲法是业务模型。
    定义：
        需求到面向对象的桥梁
    作用：
        1.发掘重要的业务领域概念
        2.建立业务领域概念之间的关系 
    方法：
        从用例中找名词
    领域建模的三字经方法:找名词、加属性、连关系。
        参考：http://www.cnblogs.com/linhaifeng/articles/6182264.html#_label15 
             http://www.cnblogs.com/linhaifeng/articles/7341318.html
"""

# 17.请写一个小游戏，人狗大站，2个角色，人和狗，游戏开始后，生成2个人，3条狗，互相混战，
# 人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。
# 注意，请按题14领域建模的方式来设计类。
# class Role:
#     def __init__(self, name, life_value, attack_force):
#         self.name = name
#         self.life_value = life_value
#         self.attack_force = attack_force
#
#     def attack(self, obj):
#         obj.life_value -= self.attack_force
#
# class Person(Role):
#     def attack(self, obj):
#         super().attack(obj)
#         print('%s attack %s' % (self.name, obj.name))
#
# class Dog(Role):
#     def attack(self, obj):
#         super().attack(obj)
#         print('%s attack %s' % (self.name, obj.name))
#
#
# p1 = Person('alex', 100, 32)
# d1 = Dog('bela', 40, 40)
#
# p1.attack(d1)
# print(d1.life_value)
# d1.attack(p1)
# print(p1.life_value)
"""
alex attack bela
8
bela attack alex
60
"""

# 18.编写程序, 在元类中控制把自定义类的数据属性都变成大写.
"""
new： 对象的创建，是一个静态方法，第一个参数是cls。(想想也是，不可能是self，对象还没创建，哪来的self)
init ： 对象的初始化， 是一个实例方法，第一个参数是self。
call ： 为了将一个类实例当做函数调用，我们需要在类中实现__call__()方法,可以用来改变实例的内部成员的值.
先有创建，才有初始化。即先new，而后init。
"""
# class Mymeta(type):
#     """修改类属性为大写"""
#     def __new__(cls, *args, **kwargs):
#         for k,v in args[2].items():
#             if not callable(v) and not k.startswith('__'):
#                 args[2][k] = v.upper()
#             else:
#                 args[2][k] = v
#         return type.__new__(cls, *args, **kwargs)
#
#     """通过call改写了对象属性为大写"""
#     def __call__(self, *args, **kwargs):
#         # print(self, args, kwargs)  # <class '__main__.Chinese'> ('hqs', 12) {}
#         new_args = []
#         for index, i in enumerate(args):
#             if isinstance(i, str):
#                 new_args.append(i.upper())
#             else:
#                 new_args.append(i)
#         args = tuple(new_args)
#         print(args)
#         obj = object.__new__(self)
#         self.__init__(obj, *args, **kwargs)
#         return obj
#
# class Chinese(object, metaclass=Mymeta):
#     country = 'CHINA'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def talk(self):
#         print("%s is talking" % self.name)
#
#
# people1 = Chinese('hqs', 12)
# print(people1.name, people1.country, people1.age)
"""
('HQS', 12)
HQS CHINA 12
"""


# 19.编写程序, 在元类中控制自定义的类无需init方法.
# 同上18题答案


# 20.编写程序, 编写一个学生类, 要求有一个计数器的属性, 统计总共实例化了多少个学生.
# class Student:
#     __count = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.__count += 1
#
#     @staticmethod
#     def get_count():
#         print("总共实例化 %s 人" % Student.__count)
#
# stu1 = Student('hqs', 20)
# stu2 = Student('egon', 19)
# stu1.get_count()
# Student.get_count()

# 21.编写程序, A 继承了 B, 俩个类都实现了 handle 方法, 在 A 中的 handle 方法中调用 B 的 handle 方法
# class B:
#     def handle(self):
#         print('from B handle')
#
# class A(B):
#     def handle(self):
#         print("class A's instance")
#         super().handle()
#
# a = A()
# a.handle()
"""
class A's instance
from B handle
"""

# 22.编写程序, 如下有三点要求：
# 1、自定义用户信息数据结构， 写入文件, 然后读取出内容, 利用json模块进行数据的序列化和反序列化
# e.g
# {
#     "egon":{"password":"123",'status':False,'timeout':0},
#     "alex":{"password":"456",'status':False,'timeout':0},
# }
# 2、定义用户类，定义方法db，例如 执行obj.db可以拿到用户数据结构
# 3、在该类中实现登录、退出方法, 登录成功将状态(status)修改为True, 退出将状态修改为False(退出要判断是否处于登录状态).
#    密码输入错误三次将设置锁定时间(下次登录如果和当前时间比较大于10秒即不允许登录)
# import json
# import time
# class User:
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password
#         self.status = False
#         self.timeout = 0
#
#     @property
#     def db(self):
#         with open(self.name+".txt", 'r', encoding="utf-8") as f:
#             data = json.load(f)
#         return data
#
#     def save(self):
#         obj={}
#         obj[self.name] = {"password": self.password, "status": self.status, "timeout": self.timeout}
#         with open(self.name+'.txt', 'w', encoding='utf-8') as f:
#             json.dump(obj, f)
#
#     def login(self):
#         with open(self.name+'.txt', 'r+', encoding='utf-8') as f:
#             data = json.load(f)
#             count = 0
#             while count < 3:
#                 password = input("password>>:").strip()
#                 if password != data[self.name]['password']:
#                     count += 1
#                     continue
#                 else:
#                     if data[self.name]['timeout'] != 0:
#                         if time.time() - data[self.name]['timeout'] > 10:
#                             print('不允许登录，时间超时！')
#                             break
#                         else:
#                             data[self.name]['status'] = True
#                             f.seek(0)
#                             f.truncate()
#                             json.dump(data, f)
#                             print("--------welcome--------")
#                             break
#                     else:
#                         data[self.name]['status'] = True
#                         f.seek(0)
#                         f.truncate()
#                         json.dump(data, f)
#                         print("----------welcome----------")
#                         break
#             else:
#                 data[self.name]['timeout'] = time.time()
#                 f.seek(0)
#                 f.truncate()
#                 json.dump(data, f)
#
#     def exit(self):
#         with open(self.name+'.txt', 'r+', encoding="utf-8") as f:
#             data = json.load(f)
#             if data[self.name]["status"] == True:
#                 data[self.name]["status"] = False
#                 f.seek(0)
#                 f.truncate()
#                 json.dump(data, f)
#             else:
#                 print("您现在处于退出状态")
#
# user1 = User('alex', '123')
# user1.save()
# user1.login()



