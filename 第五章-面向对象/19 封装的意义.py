# 一、封装数据属性：明确地区分内外，控制外部对隐藏属性的操作行为
# class People:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def tell_info(self):
#         print('Name:<%s> Age:<%s>' % (self.__name, self.__age))
#
#     def set_info(self, name, age):
#         if not isinstance(name, str):
#             print('名字必须是字符串类型')
#             return
#         if not isinstance(age, int):
#             print('年龄必须是数字类型')
#             return
#         self.__name = name
#         self.__age = age
#
#
# p = People('egon', 18)
#
# # p.tell_info()
# """
# Name:<egon> Age:<18>  # 封装数据，开放接口给外部访问
# """
#
# # p.set_info('Egon', 38) # 修改数据只能通过接口来完成，可以通过接口完成各种限制
# # p.tell_info()
# """
# Name:<Egon> Age:<38>
# """
#
# # p.set_info(123, 38)
# """
# 名字必须是字符串类型
# """
# p.set_info('egon', '38')
# """
# 年龄必须是数字类型
# """
# p.tell_info()


# 二、封装方法的目的：隔离复杂度
class ATM:
    def __card(self):
        print('插卡')
    def __auth(self):
        print('输入取款金额')
    def __input(self):
        print('输入取款金额')
    def __print_bill(self):
        print('打印账单')
    def __take_money(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()


a = ATM()
a.withdraw()