# -*- coding:utf-8 -*-
import os
import sys
# 判断文件是否存在，若不存在创建lock.txt
file = os.path.exists('/Users/huangqiushi/Desktop/python/lock.txt')
if file == True:
    pass
else:
    f = open(file='/Users/huangqiushi/Desktop/python/lock.txt', mode='w', encoding='utf-8')
# 用户组和密码
user = ["hqs","alex","joker"]
password = 123
# 欢迎页面！！
print("欢迎进入登录页面!!!")

count = 0
tag = True
while tag:
    # 判断是否在黑名单
    usr = input("输入账号：")
    pwd = int(input("输入密码："))
    with open(file='/Users/huangqiushi/Desktop/python/lock.txt', mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            a = line.split('|')
            if usr == a[0]:
                sys.exit('%s 在黑名单中！！' %(usr))
                tag = False
    if usr in user and pwd == password:
        print("登录成功！！！！")
        tag=False
        break
    else:
        print("错误的用户名或密码！！！")
    count += 1
    # 添加黑名单
    if count == 3:
        with open(file='/Users/huangqiushi/Desktop/python/lock.txt', mode='w+', encoding='utf-8') as f:
            lock = print(f.read())
            f.write('%s' % usr)
            print("账户已经锁定！！！")
        tag = False
        break

