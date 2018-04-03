# 反射：通过字符串映射到对象的属性
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' %self.name)


obj=People('egon', 18)
print(obj.name)   # obj.__dict__('name')
obj.talk()

hasattr(obj, 'name')   # 判断obj内有没有name属性，obj.name  # obj.__dict__['name']
print(hasattr(obj, 'name'))  # 输出：True
print(hasattr(obj, 'talk'))  # obj.talk
"""
True
True
"""

getattr(obj, 'name', None)   # 拿到一个对象的属性
print(getattr(obj, 'name'))
print(getattr(obj, 'namesadwd', None))  # 设置default=None
print(getattr(obj, 'talk'))  # 拿到方法属性
"""
egon
None
<bound method People.talk of <__main__.People object at 0x10401af60>>
"""

setattr(obj, 'sex', 'male')   # 修改对象属性  obj.sex='male'
print(obj.sex)
"""
male
"""

delattr(obj, 'age')  # 删除对象属性  del obj.age
print(obj.__dict__)
"""
{'name': 'egon', 'sex': 'male'}
"""