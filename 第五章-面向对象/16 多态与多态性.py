"""
多态:同一类事物的多种形态
多态性:指在不考虑实例类型的情况下使用实例，多态性分为静态多态性和动态多态性
"""
import abc    #利用abc模块实现抽象类
class Animal(metaclass=abc.ABCMeta):  # 类似接口，只定义规范，不实现具体的代码
    @abc.abstractclassmethod
    def talk(self):
        pass

class People(Animal):  # 动物形态之一：人
    def talk(self):
        print('people is talking')

class Pig(Animal):     # 动物形态之二：猪
    def talk(self):
        print('Pig is talking')

class Dog(Animal):     # 动物形态之三：狗
    def talk(self):
        print('Dog is talking')


peo1 = People()
pig1 = Pig()
dog1 = Dog()
# 调用方法不用考虑三者具体是什么类型直接使用，这种就是动态多态性

# peo1.talk()
# pig1.talk()
# dog1.talk()


#更进一步,我们可以定义一个统一的接口来使用
def func(animal):
    animal.talk()

func(peo1)
func(pig1)
func(dog1)

"""
多态性的好处：
    1、增加程序的灵活性
    以不变应万变，无论对象千变万化，使用者都是同一种形式去调用
    2、增加程序的扩展性
    通过继承animal类创建一个新类，使用者可以不改变自己的代码，依然用func(animal)调用    
"""

class Cat(Animal):
    def talk(self):
        print('say miaomiao')

cat1 = Cat()
func(cat1)

