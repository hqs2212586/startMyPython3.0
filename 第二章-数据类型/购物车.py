# -*- coding:utf-8 -*-
import os
import sys
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998}
]
'''
功能要求：
基础要求：
1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
2、允许用户根据商品编号购买商品
3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
4、可随时退出，退出时，打印已购买商品和余额
5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示

扩展需求：
1、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
2、允许查询之前的消费记录
'''

welcome_head = "欢迎登录购物平台"
print(welcome_head.center(50,'-'))

# 判断用户历史文件是否存在，若不存在创建用户历史文件,存在则打开文件
file = os.path.exists('/Users/huangqiushi/Desktop/python/user_info.txt')
if file == True:
    pass
else:
    file = open(file='/Users/huangqiushi/Desktop/python/user_info.txt', mode='w', encoding='utf-8')

# 购物车用户信息文件保存用户名、密码、工资
user_info = []
with open(file='/Users/huangqiushi/Desktop/python/user_info.txt', mode='r+', encoding='utf-8') as f:
    for line in f.readlines(): # readlines读取所有行，并返回字符串
        dic_f = eval(line.strip())  # 将字符串转化为字典
        user_info.append(dic_f)    # 将字典添加进数组中
    f.close()


# 用户登录输入用户名密码和工资注册购物平台
# 文本中每一行记录一条字典，包含用户名、密码、工资三条信息
new_user={} # 集合
flag = True
while flag:
    user = input("请输入用户名：")
    password = input("请输入密码：")
    i = 0
    while i < len(user_info):
        if user == user_info[i]['name']:
            if password == user_info[i]['password']:
                salary = user_info[i]['salary']
                new_user["name"] = user
                new_user["password"] = password
                new_user["salary"] = salary
                welcome_msg = "\033[32;1m欢迎登录，目前工资剩余%s \033[0m"%salary
                print(welcome_msg.center(50,'-'))
                flag = False
                break
            else:
                # 密码不正确更新密码登录
                password = input("用户密码不正确，请重新输入：")
                continue
        else:   # 用户在字典中无记录
            salary = input("首次登录请填写工资：")  # 与前面已创建的用户统一
            if salary.isdigit:   # 判断工资是否是数字
                salary = int(salary)
                # new_user["name"] = user
                # new_user["password"] = password
                # new_user["salary"] = salary
                # user_info.append(new_user)
                break
            else:
                exit("您输入的工资不是数字！！")


# 购物车开始
shop_car = []
while flag is not True:
    # 打印商品列表:编号＋商品＋价格
    print('商品列表'.center(50,'-'))
    lebal = 0
    for item in goods:
        print(lebal,item['name'],item['price'])
        lebal += 1
    print('结束'.center(50,'-'))


    # 选择商品
    user_choice = input('q=quit,c=check]  输入想购买商品的编号:')
    # 判断是否是数字
    if user_choice .isdigit():
        user_choice = int(user_choice)  # 转换为整数
        # 序号是否在产品范围内
        if user_choice < len(goods): # len(goods)=4,取值范围0-3
            dic_g = goods[user_choice] # 选择商品,返回值为字典
            # 商品价格是否小于工资
            if dic_g['price'] <= salary:
                shop_car.append(dic_g) # 加入购物车,同样是字典存入列表
                salary = salary - dic_g['price']  # 减钱
                print('购买的商品是：'.center(35,'-'))
                for item in shop_car:
                    print(item)
                print('剩余资金：［%s］' % salary)
            else:
                print('剩余资金：［%s］,买不起这个产品！' %salary)
        else:
            print('没有这个商品，请重新输入！')
    elif user_choice == 'q' or user_choice == 'quit':
        print('买入的商品：'.center(40,'-'))
        for item in shop_car:
            print(item)
        print('END' .center(40,'-'))
        print('你的资金是 ［%s］' %salary)
        # 将工资变动写入文件中
        new_user["salary"] = salary
        user_info[i] = new_user
        with open(file='/Users/huangqiushi/Desktop/python/user_info.txt', mode='w+', encoding='utf-8') as f:
            for j in user_info:
                f.write(str(j)+ '\n')

        flag = True
    elif user_choice == 'c' or user_choice == 'check':
        print('买入的商品：'.center(40,'-'))
        for item in shop_car:
            print(item)
        print('你的资金是 %d' %salary)
        print('Check '.center(40,'-'))
    else:
        print('错误的输入，请检查!!')
