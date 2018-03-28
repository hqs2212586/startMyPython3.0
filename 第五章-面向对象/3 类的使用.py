# 先定义类
class LuffyStudent:
    school = 'luffycity'

    def learn(self):
        print('is learning')

    def eat(self):
        print('is sleeping')


# def func():
#     x = 1
#     print('==>')
#
#
# func()

# 查看类的名称空间
# print(LuffyStudent.__dict__)
# print(LuffyStudent.__dict__['school'])
# print(LuffyStudent.__dict__['learn'])
"""
{'__module__': '__main__', 'school': 'luffycity', 'learn': <function LuffyStudent.learn at 0x101eb3620>, 'eat': <function LuffyStudent.eat at 0x101f211e0>, '__dict__': <attribute '__dict__' of 'LuffyStudent' objects>, '__weakref__': <attribute '__weakref__' of 'LuffyStudent' objects>, '__doc__': None}
luffycity
<function LuffyStudent.learn at 0x101eb3620>
"""

# 查看
# print(LuffyStudent.school)  # luffystudent.__dict__['school']
# print(LuffyStudent.learn)  # Luffystudent.__dicg_ （'learn'）
"""
luffycity
<function LuffyStudent.learn at 0x101cb3620>
"""

# 增
LuffyStudent.country = 'China'
print(LuffyStudent.__dict__)
print(LuffyStudent.country)
"""
{'__module__': '__main__', 'school': 'luffycity', 'learn': <function LuffyStudent.learn at 0x101eb3620>, 'eat': <function LuffyStudent.eat at 0x1040211e0>, '__dict__': <attribute '__dict__' of 'LuffyStudent' objects>, '__weakref__': <attribute '__weakref__' of 'LuffyStudent' objects>, '__doc__': None, 'country': 'China'}
China
"""

# 删
del LuffyStudent.country

# 改
LuffyStudent.school = 'whu'
print(LuffyStudent.school)
"""
whu
"""