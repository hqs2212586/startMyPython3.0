"""
在子类派生的新的方法中重用父类的方法，有两种实现方式
"""
# 方式一、指名道姓（不依赖继承）
# class Hero:
#     def __init__(self, nickname, life_value, aggresivity):
#         self.nickname = nickname
#         self.life_value = life_value
#         self.aggresivity = aggresivity
#
#     def attack(self, enemy):
#         enemy.life_value -= self.aggresivity
#
#
# class Garen(Hero):
#     camp = 'Demacia'
#
#     def attack(self, enemy):  # 一旦重新定义了自己的属性且与父类重名，调用新增属性时，就以自己为准。
#         Hero.attack(self, enemy)  # 指名道姓，不依赖于继承(一种重用方式)
#         print('from Garen Class')
#
#
# class Riven(Hero):
#     camp = 'Noxus'
#
#
# g = Garen('草丛伦', 100, 30)
# r = Riven('锐雯雯', 80, 50)
#
# print(r.life_value)
# g.attack(r)
# print(r.life_value)

# 指名道姓，实例化子类添加自己独有特征
# class Hero:
#     def __init__(self, nickname, life_value, aggresivity):
#         self.nickname = nickname
#         self.life_value = life_value
#         self.aggresivity = aggresivity
#
#     def attack(self, enemy):
#         enemy.life_value -= self.aggresivity
#
#
# class Garen(Hero):
#     camp = 'Demacia'
#
#     def __init__(self, nickname, life_value, aggresivity, weapon):  # 代码复用
#         Hero.__init__(self, nickname, life_value, aggresivity)
#
#         self.weapon = weapon
#
#     def attack(self, enemy):
#         Hero.attack(self, enemy)  # 指名道姓
#         print('from Garen Class')
#
# g = Garen('草丛伦', 100, 30, '金箍棒')
# print(g.__dict__)


# 方式二：super()  （依赖继承）
# class Hero:
#     def __init__(self, nickname, life_value, aggresivity):
#         self.nickname = nickname
#         self.life_value = life_value
#         self.aggresivity = aggresivity
#
#     def attack(self, enemy):
#         enemy.life_value -= self.aggresivity
#
#
# class Garen(Hero):
#     camp = 'Demacia'
#
#     def attack(self, enemy):
#         super(Garen, self).attack(enemy)  # 依赖继承
#         print('from Garen Class')
#
#
# class Riven(Hero):
#     camp = 'Noxus'
#
#
# g = Garen('草丛伦', 100, 30)
# r = Riven('锐雯雯', 80, 50)
#
# g.attack(r)
# print(r.life_value)
"""
from Garen Class
50
"""

# 运用super()实例化子类添加独有特征
# class Hero:
#     def __init__(self, nickname, life_value, aggresivity):
#         self.nickname = nickname
#         self.life_value = life_value
#         self.aggresivity = aggresivity
#
#     def attack(self, enemy):
#         enemy.life_value -= self.aggresivity
#
#
# class Garen(Hero):
#     camp = 'Demacia'
#
#     def __init__(self, nickname, life_value, aggresivity, weapon):  # 代码复用
#
#         # Hero.__init__(self, nickname, life_value, aggresivity)
#         # super(Garen, self).__init__(nickname, life_value, aggresivity)  # python2必须这么写
#         super().__init__(nickname, life_value, aggresivity)  # python3可以这么简写
#
#         self.weapon = weapon
#
#     def attack(self, enemy):
#         Hero.attack(self, enemy)  # 指名道姓
#         print('from Garen Class')
#
#
# g = Garen('草丛伦', 100, 30, '金箍棒')
# print(g.__dict__)
"""
{'nickname': '草丛伦', 'life_value': 100, 'aggresivity': 30, 'weapon': '金箍棒'}
"""

# super与mro列表的关系
class A:
    def f1(self):
        print('from A')
        super().f1()   # super不管A的继承关系，按照C的MRO列表，继续往后找：B

class B:
    def f1(self):
        print('from B')

class C(A,B):
    pass

print(C.mro())
"""
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
"""
c = C()
c.f1()
"""
from A
from B
"""