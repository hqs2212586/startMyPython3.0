'''
    函数外部的代码要想获取函数的执行结果,可以在函数里用return语句把结果返回
    注意：
    1、函数在执行过程中只要遇到return语句，就会停止执行并返回结果，so可以理解为return语句代表着函数的结束
    2、如果未在函数中指定return，那这个函数的返回值为None
'''
def stu_register(name,age,course='PY',country='CN'):
    print("注册学生信息".center(50,'-'))
    print("姓名：", name)
    print("age：", age)
    print("国籍", country)
    print("课程", course)
    if age > 22:
        return False
    else:
        return True

registration_status = stu_register('阿斯顿',22,course="全栈开发",country='JP')

if registration_status:
    print("注册成功".center(50,'-'))
else:
    print("too old to be a student.")

'''
    执行到return语句后，停止执行函数并返回结果
    
'''
def stu_register(name,age,course):
    print(name,age,course)
    #
    # if age > 22:
    #     return 'sdfsf'  # 返回值可以是任意值
    # else:
    #     return True
    #
    # return None      # 到return语句后，停止执行函数并返回结果
    # print('hahah')
    # return 1
    return [name,age]
status = stu_register('Peiqi',29,'安保')
print(status)