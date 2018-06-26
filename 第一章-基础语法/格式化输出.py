# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


# 练习：用户输入姓名、年龄、工作、爱好 ，然后打印成以下格式
def func():
    name = input('用户姓名：')
    age = input('用户年龄：')
    job = input('用户工作：')
    sex = input('用户性别：')

    print('info of Egon'.center(30, '-'))
    print('Name  : %s' % name)
    print('Age   : %s' % age)
    print('Sex   : %s' % sex)
    print('Job   : %s' % job)
    print('end'.center(30,'-'))


func()

"""
用户姓名：hqs
用户年龄：22
用户工作：Teacher
用户性别：male
---------info of Egon---------
Name  : hqs
Age   : 22
Sex   : male
Job   : Teacher
-------------end--------------
"""