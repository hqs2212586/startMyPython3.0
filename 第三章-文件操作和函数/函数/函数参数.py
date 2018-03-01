'''
    参数可以让函数更灵活，不只能做死动作，还可以根据调用时传参的不同来决定函数内部的执行流程。

    形参变量：只有在被调用时才分配内存单元，在调用结束时，即刻释放所分配的内存单元。因此，形参只在函数内部有效。函数调用结束返回主调用函数后则不能再使用该形参变量

    实参：可以是常量、变量、表达式、函数等，无论实参是何种类型的量，在进行函数调用时，它们必须有确定的值，以便把这些值传送给形参。因此应预先用赋值，输入等办法使参数获得确定值
'''


def calc(x,y):   # 形参
    res = x**y
    return res
a,b = 3,5
c = calc(a,b)    # 实参
print(c)
d = calc(2,3)    # 实参


# 默认参数
def stu_register(name,age,country,course):
    print("注册学生信息".center(50,'-'))
    print("姓名：",name)
    print("age：" ,age)
    print("国籍",country)
    print("课程",course)

stu_register("山炮",22,"CN","python_devops")
stu_register("丰收",23,"CN","linux")

'''
    由于很多人国籍都是中国，可以将country设置为默认参数
    默认参数：
'''
def stu_register(name,age,course,country="CN"):  # 非默认参数不能跟在默认参数后面
    print("registration info".center(50,'-'))
    print(name,age,country,course)

stu_register("jack",22,'c++')     # 实参和形参按顺序一一对应
stu_register("rain",32,'dance','Korean')
stu_register("Alfa",21,'python')


# 关键字参数
'''
    正常情况下，给函数传参数要按顺序，不想按顺序可以用关键参数
    定义：指定了参数名的参数就叫关键参数
    关键参数必须放在位置参数（以位置顺序确定对应关系的参数）之后
'''
def stu_register(name,age,course,country='CN'):
    print("注册学生信息".center(50,'-'))
    print("姓名：",name)
    print("age：" ,age)
    print("国籍",country)
    print("课程",course)

stu_register("绮珊",course='Python',age=22,country='JP')  # 后三个均为为关键参数置于name位置参数之后
# stu_register("杉树",course='Python',22,country='JP')    # 22为位置参数不能放在关键参数course之后
# stu_register("曼玉",22,age=25,country='JP')    # age获得多个赋值