"""
BMI指数：（BMI是计算而来的，很明显它听起来像一个属性而非方法，如果我们将其作为一个属性，更便于理解）
成人的BMI数值：
过轻：低于18.5
正常：18.5-23.9
过重：24-27
肥胖：28-32
非常肥胖：高于32
体质指数（BMI）= 体重（KG）/ 身高^2（M）
EX：70KG / (1.75*1.75) = 22.86
"""
# 一、普通解决方法
# class People:
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
# p = People('jack', 48, 1.65)
# p.bmi = p.weight / (p.height ** 2)
#
# print(p.bmi)

# 二、添加函数改写
# class People:
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     def bmi(self):
#         print('===>')
#         return self.weight / (self.height ** 2)
#
# p = People('SH', 53, 1.70)
# print(p.bmi())  # bmi是一个名词，却使用bmi()，容易误解为一个动作


# 三、增加property装饰器
# class People:
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     @property    # 应用场景：有一个值是通过计算得来的，首选定义方法，运用property让使用者感知不到
#     def bmi(self):
#         print('===>')
#         return self.weight / (self.height ** 2)
#
# p = People('SH', 53, 1.70)
# print(p.bmi)   # 使用者像访问数据属性一样访问bmi，方法被伪装
#
# p.height = 1.82
# print(p.bmi)
#
# p.bmi = 333  # 报错，看起来像数据属性，其实还是一个方法，不能赋值


"""
property的另一种用法
"""
# class People:
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
# p = People('egon')
# print(p.get_name())



# class People:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
# p = People('egon')
# print(p.name)


class People:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        # print('getter')
        return self.__name

    @name.setter
    def name(self, val):
        # print('setter', val)
        if not isinstance(val, str):
            print('名字必须是字符串类型')
            return
        self.__name=val

    @name.deleter
    def name(self):
        # print('deleter')
        print('不允许删除')

p = People('egon')
print(p.name)
p.name = 'dragon'
print(p.name)   # name修改成功

p.name = 123   # 提示报错：名字必须是字符串类型
print(p.name)

del p.name  # 提示报错：不允许删除
