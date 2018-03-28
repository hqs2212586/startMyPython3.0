"""
    __init__方法用来为对象定制对象自己独有的特征
"""
class LuffyStudent:
    school = 'luffycity'

    def __init__(self, name, sex, age):  # 实例化时自动调用
        self.Name = name
        self.Sex = sex
        self.Age = age

    def learn(self):
        print('is learning')

    def eat(self):
        print('is sleeping')


# 产生对象
stu1 = LuffyStudent('百合', '女', 12)
print(stu1.Name)

"""
加上__init__方法后，实例化的步骤
    1、先产生一个空对象
    2、LuffyStudent.__init__(stu1, '百合', '女', 12)
"""

# 查
print(stu1.__dict__)
print(stu1.Name)
print(stu1.Sex)
print(stu1.Age)
"""
{'Name': '百合', 'Sex': '女', 'Age': 12}
百合
女
12
"""

# 改
stu1.Name = '李二丫'
print(stu1.__dict__)
print(stu1.Name)
"""
{'Name': '李二丫', 'Sex': '女', 'Age': 12}
李二丫
"""

# 删除
del stu1.Name
print(stu1.__dict__)
"""
{'Sex': '女', 'Age': 12}
"""

# 增
stu1.class_name = 'python开发'
print(stu1.__dict__)
"""
{'Sex': '女', 'Age': 12, 'class_name': 'python开发'}
"""

stu2 = LuffyStudent('李三炮', '男', 22)
print(stu2.__dict__)
"""
{'Name': '李三炮', 'Sex': '男', 'Age': 22}
"""