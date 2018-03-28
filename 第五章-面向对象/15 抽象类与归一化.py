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

# animal = Animal()
#TypeError: Can't instantiate abstract class Animal with abstract methods eat, run
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
"""
TypeError: Can't instantiate abstract class People with abstract methods run
"""