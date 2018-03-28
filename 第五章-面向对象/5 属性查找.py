class LuffyStudent:
    school = 'luffycity'

    def __init__(self, name, sex, age):  # 实例化时自动调用
        self.Name = name
        self.Sex = sex
        self.Age = age

    def learn(self):
        print('%s is learning' % self.Name)

    def eat(self):
        print('%s is sleeping' % self.Name)


# 产生对象
stu1 = LuffyStudent('百合', '女', 12)
stu2 = LuffyStudent('李三炮', '男', 38)
stu3 = LuffyStudent('张铁蛋', '男', 48)
# print(stu1.__dict__)
# print(stu2.__dict__)
# print(stu3.__dict__)

# 对象：特征和技能的结合体
# 类：类是一系列对象相似的特征与相似技能的结合体


# 类中数据属性：是所有对象共有的（都是一样的）
print(LuffyStudent.school, id(LuffyStudent.school))

print(stu1.school, id(stu1.school))
print(stu2.school, id(stu2.school))
"""内存地址一样
luffycity 4325120112
luffycity 4325120112
luffycity 4325120112
"""

# 类中函数属性：是绑定给对象的，绑定到不同的对象是不同的绑定方法，对象调用绑定方法时，会把对象本身当做第一个参数传入，传给self
print(LuffyStudent.learn)
LuffyStudent.learn(stu1)
"""
<function LuffyStudent.learn at 0x1040211e0>
百合 is learning
"""


print(stu1.learn)
print(stu2.learn)
print(stu3.learn)
"""绑定方法，每个人的函数内存地址不同
<bound method LuffyStudent.learn of <__main__.LuffyStudent object at 0x10402cc18>>
<bound method LuffyStudent.learn of <__main__.LuffyStudent object at 0x10402cc50>>
<bound method LuffyStudent.learn of <__main__.LuffyStudent object at 0x10402cc88>>
"""

stu2.learn()
"""
李三炮 is learning
"""


# 属性查找，优先对象中查找，对象中没有在类中查找
# stu1.x = 'from stu1'
LuffyStudent.x = 'from Luffycity class'

print(stu1.__dict__)
print(stu1.x)
"""
{'Name': '百合', 'Sex': '女', 'Age': 12}
from Luffycity class
"""