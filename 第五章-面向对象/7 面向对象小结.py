
class Chinese:
    country = 'China'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print('%s is eating' % self.name)


p1 = Chinese('egon', 18, 'male')
p2 = Chinese('alex', 38, 'female')
p3 = Chinese('wpq', 48, 'female')

print(p1.country)
p1.eat()
"""
China
egon is eating
"""