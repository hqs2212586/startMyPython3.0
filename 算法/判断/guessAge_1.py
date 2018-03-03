#! /usr/bin/python3
# -*- coding:utf-8 -*-

my_age = 28

count = 0
while count < 3:
    user_input = int(input("input your guess num:"))

    if user_input == my_age:
        print("Congratulations, you got it !")
        break
    elif user_input < my_age:
        print("Oops,think bigger!")
    else:
        print("think smaller!")
    count += 1 #每次loop  计算器＋1
else:
    print("三次机会均未猜中！")
