'''
    局部变量：函数内定义的变量，只能在局部生效
    全局变量：定义在函数外部一级代码的变量，整个程序可用（由上到下可用）
    在函数内部可以引用全局变量。
    如果全局和局部都有一个变量，函数查找变量的顺序是由内而外的。两个函数间互不可见
'''

name = "Black girl"       # 全局变量

def change_name():
    # global name         ＃ （不建议使用global）在函数内修改全局变量，不能放在函数内局部变量后面
    name = "黑色的姑娘"     # 局部变量
    print("在",name,"里面...",id(name))

change_name()
print(name,id(name))   # 与函数内的变量内容完全不同
'''
输出结果：
    在 黑色的姑娘 里面... 4302993904
    Black girl 4316351984
'''


# 函数内可以修改字典、列表、集合、对象、类、元组内的列表
names = ['Alex','Black Girl','Peiqi']
def change_name():
    names = ['Alex']
    del names[2]      # names整体的内存地址不能修改只能引用,但其内部的元素是可以修改的
    names[1] = "黑姑娘"
    print(names)

change_name()
print(names)
'''
输出结果：
    ['Alex', '黑姑娘']
    ['Alex', '黑姑娘']
'''