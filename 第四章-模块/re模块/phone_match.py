
# 正则表达式
import re


f = open("嫩模联系方式", "r")

# 取文件中手机号码，字符匹配传统方法
# contacts = []
# for line in f:
#     name,region,height,weight,phone = line.split()
#     if phone.isdigit():
#         # print(phone)
#         contacts.append(phone)
# print(contacts)

data = f.read()
contacts = re.findall("[0-9]{11}", data)  # 将要匹配的字符规律，提炼为一个公式
print(contacts)