"""
练习2：模仿lol定义两个英雄类
要求：
英雄需要有昵称、攻击力、生命值等属性；
实例化出两个英雄对象；
英雄之间可以互殴，被殴打一方掉血，血量小于0判定为死亡。
"""


class Garen:
    camp = 'Demacia'

    def __init__(self, nickname, life_value, aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attack(self, enemy):
        enemy.life_value -= self.aggresivity


class Riven:
    camp = 'Noxus'

    def __init__(self, nickname, life_value, aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attack(self, enemy):
        enemy.life_value -= self.aggresivity


g1 = Garen('草丛伦', 100, 30)

r1 = Riven('可爱的瑞雯', 80, 50)

print(r1.life_value)
g1.attack(r1)  # 攻击了一刀
r1.attack(g1)
print(r1.life_value)
print(g1.life_value)