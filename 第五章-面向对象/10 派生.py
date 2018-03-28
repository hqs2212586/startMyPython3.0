class Hero:
    def __init__(self, nickname, life_value, aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attack(self, enemy):
        enemy.life_value -= self.aggresivity


class Garen(Hero):
    camp = 'Demacia'

    def attack(self, enemy):  # 一旦重新定义了自己的属性且与父类重名，调用新增属性时，就以自己为准。
        print('from Garen Class')


class Riven(Hero):
    camp = 'Noxus'


g = Garen('草丛伦', 100, 30)
r = Riven('锐雯雯', 80, 50)

print(g.camp)
g.attack(r)
print(r.life_value)