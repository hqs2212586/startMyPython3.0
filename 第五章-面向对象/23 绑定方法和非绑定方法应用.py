import settings
import hashlib
import time

class People:
    def __init__(self, name, age, sex):
        self.id = self.create_id()
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        print('Name %s Age %s Sex %s' % (self.name, self.age, self.sex))

    @classmethod
    def from_conf(cls):
        obj= cls(
            settings.name,
            settings.age,
            settings.sex
        )
        return obj

    @staticmethod
    def create_id():  # 不依赖类和对象的方法，因此创建普通函数
        m = hashlib.md5(str(time.time()).encode('utf-8'))
        return m.hexdigest()


p = People('egon',18,'male')
# 绑定给对象，就应该由对象来调用，自动将对象本身当做第一个参数传入
p.tell_info()   # tell_info(p)
"""
Name egon Age 18 Sex male
"""

# 绑定给类，就应该由类来调用，自动将类本身当做第一个参数传入
p=People.from_conf()  # from_conf(People)
p.tell_info()
"""
Name alex Age 18 Sex female
"""


# 非绑定方法，不与类或对象绑定，谁都可以调用，没有自动传值一说
p1 = People('egon1', 18, 'male')
p2 = People('egon2', 28, 'male')
p3 = People('egon3', 38, 'male')
print(p1.id)
print(p2.id)
print(p3.id)
"""
a653d2ce4826a31051d7ddd13a9d82cf
4c0f5168f3a2fdb96a37430380d336e4
b214300c918bc319b840077dfdbb8425
"""