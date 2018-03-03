#! /usr/bin/python3
# -*- coding:utf-8 -*-

my_age = 28
for i in range(4):
    user_input = int(input("input your guess num:"))

    if user_input == my_age:
        print("Congratulations, you got it !")
        break
    elif user_input < my_age:
        print("Oops,think bigger!")
    else:
        print("think smaller!")
    i+=1

