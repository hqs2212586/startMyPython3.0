# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import re

# 电话号码检查
# class IsCellphone():
#     def __init__(self):
#         self.p = re.compile('^1[348]\\d{9}')  # 公式编译好了，直接拿去匹配提升效率
#
#     def iscellphone(self, number):
#         res = self.p.match(number)
#         if res:
#             return True
#         else:
#             return False
#
#
# p = IsCellphone()
# f = open("嫩模联系方式", "r")
# data = f.read()
# contacts = re.findall("[0-9]{11}", data)
# for i in contacts:
#     if p.iscellphone(i):
#         print("%s 是正常号码" % i)
#     else:
#         print("请检查手机号码%s" % i)


# 邮箱检查
# class IsMail():
#     def __init__(self):
#         self.p = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
#
#     def ismail(self, str):
#         res = self.p.match(str)
#         if res:
#             return True
#         else:
#             return False
#
#
# p = IsMail()
# f = open("嫩模联系方式", "r")
# for k,v in enumerate(f):
#     if k == 0:
#         pass
#     else:
#         data = v.split(" "*5)
#         mail_addr = data[5]
#         if p.ismail(mail_addr):
#             print("正常得邮箱地址%s" % mail_addr)
#         else:
#             print("请检查邮箱地址%s" % mail_addr)
"""
正常得邮箱地址133123@qq.com

正常得邮箱地址wdasd@13.ad.asdw

请检查邮箱地址sadw@*sad2.asdw

正常得邮箱地址wddada@sina.com

正常得邮箱地址asddwa@adwd.adww

正常得邮箱地址adwwd2@12313.sadw

请检查邮箱地址asdwd2133@dedewd3

正常得邮箱地址asdwd2@dadwdw.dww

请检查邮箱地址adwdadw@dwdw..wda

请检查邮箱地址asdwd2@de13.d23*
"""


s = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"

print(re.search(r'\([^()]+\)',s).group())  # 可拿到最里层的括号中的值'(-40/5)'
