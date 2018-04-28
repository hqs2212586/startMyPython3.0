# 抽象类和类的区别：只能被继承，不能实例化。
# 好处是：可以降低使用者的使用复杂度，统一标准
import abc    #利用abc模块实现抽象类


class Animal(metaclass=abc.ABCMeta):  # 类似接口，只定义规范，不实现具体的代码
    @abc.abstractclassmethod
    def run(self):
        pass

    @abc.abstractclassmethod
    def eat(self):
        pass

# 尝试实例化抽象类：结果失败
# animal = Animal()
# TypeError: Can't instantiate abstract class Animal with abstract methods eat, run

class People(Animal):
    def run(self):  # 不符合规范，不允许实例化
        print('people is walking')

    def eat(self):
        print('people is eating')


class Pig(Animal):
    def run(self):
        print('Pig is running')

    def eat(self):
        print('Pig is eating')


class Dog(Animal):
    def run(self):
        print('Dog is zouing')

    def eat(self):
        print('Dog is eating')


peo1 = People()
pig1 = Pig()
Dog1 = Dog()

peo1.eat()
pig1.eat()
Dog1.run()
"""
people is eating
Pig is eating
Dog is zouing
"""
# # 正常实现调用
# class Applepay:
#     def pay(self,money):
#         print('apple pay 支付了%s' %money)
#
# class Alipay:
#     def pay(self,money):
#         print('支付宝  支付了%s' %money)
#
# def payment(pay_obj,money):  #实例化的另一种调用，这个方法让实例化的时候按照payment调用：就像下面的payment(apple1,200)
#         pay_obj.pay(money)
#
# apple1 = Applepay()
# # apple1.pay(200)
# payment(apple1,200)
# """
# apple pay 支付了200
# """

# 2.有时候写的时候会把方法写错，自己定义一个主动报错
# 接口初成：手动报异常：NotImplementedError来解决开发中遇到的问题
# class Payment:
#     def pay(self):
#         raise NotImplementedError  #主动让程序报错
#
# class Wechatpay(Payment): #微信支付
#     def pay(self,money):
#         print('微信支付了%s元',money)
#
# class QQchatpay(Payment): #QQ支付
#     def fuqian(self,money):
#         print('QQ支付了%s元',money)
#
# p = Wechatpay()
# p.pay(200)   #不报错  # 微信支付了%s元 200
# q = QQchatpay()
# q.pay()  #报错


# 3.借用abc模块来实现接口
#接口类（就是为了提供标准，约束后面的子类）
# from abc import ABCMeta,abstractmethod
# class Payment(metaclass=ABCMeta):
#     @abstractmethod
#     def pay(self,money):
#         pass
#
# class Wechatpay(Payment):
#     def fuqian(self,money):
#         '''实现了pay的功能，但是方法名字不一样'''
#         print('微信支付了%s元'%money)
#
# class Alipay:
#     def pay(self,money):
#         print('支付宝  支付了%s' %money)

# p = Wechatpay() #报错了（因为上面定义了一个接口类，接口类里面
# 定义了一个pay方法，而在下面的Wechatpay方法里没有pay方法，不能
# 调用，在接口类里面约束一下，接口类里的pay方法里面不能写其他，直接pass）
# a = Alipay()
# a.pay(200)
"""
支付宝  支付了200
"""
# p = Payment() #接口类不能被实例化