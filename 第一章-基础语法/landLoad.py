user_dic = {"hqs":"123","jack":"345","even":"123456"}
n = 0
lock_list = [""]
while n < 3:
    user = input("输入用户名：")
    password = input("输入密码：")
    if user in user_dic.keys() and password in user_dic.values() and user not in lock_list:
        print("welcome,landload!")
        break
    else:
        print("input the user\password again!")
        n += 1
if n==3:
    lock_list.append(user)

# 342:
# bin(342)
# 1  0  1  0  1  0  1  1  0  342





