"""
类就是一系列对象相似的特征和技能的结合体
强调：站在不同的角度，得到的分类是不一样的

在现实世界当中：一定先有对象，后有类
在程序当中：一定得先定义类，后调用类来产生对象
"""
# 先定义类
class LuffyStudent:
    school = 'luffycity'

    def learn(self):
        print('is learning')

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleeping')


# 后产生对象
stu1 = LuffyStudent()  # 不是执行类体，而是实例化
stu2 = LuffyStudent()
stu3 = LuffyStudent()
print(stu1)  # <__main__.LuffyStudent object at 0x10401ae80>
