"""
练习1：编写一个学生类，产生一堆学生对象
要求：
有一个计算器（属性），统计总共实力了多少个对象
"""


class Student:   # 类名头字母大写
    school = 'whu'
    count = 0

    def __init__(self, name, age, sex):  # 为对象定制对象自己独有的特征
        self.name = name
        self.age = age
        self.sex = sex
        # self.count += 1  # 每个对象都是1，无法实现累加，student类的count一直都是0
        Student.count += 1

    def learn(self):
        print('%s is learning' % self.name)

    def eat(self):
        print('%s is eating very happy!' % self.name)


stu1 = Student('alex', 'male', 38)   # 实例化一次就触发一次__init__
stu2 = Student('jinxing', 'female', 48)
stu3 = Student('egon', 'male', 18)


print(Student.count)
print(stu1.count)
print(stu2.count)
print(stu3.count)
print(stu1.__dict__)
print(stu3.__dict__)
"""
3
3
3
3
{'name': 'alex', 'age': 'male', 'sex': 38}
{'name': 'egon', 'age': 'male', 'sex': 18}
"""