'''
嵌套函数
    1、函数内部可以再次定义函数
    2、执行需要被调用
    3、嵌套函数寻找变量的顺序（一层一层往上找）
'''
def func1():
    print('alex')

    def func2():
        print('eric')

func1()
'''
输出：
    alex
'''

def func1():
    print('alex')

    def func2():
        print('eric')

    func2()

func1()

'''
输出：
    alex
    eric
'''
age = 19

def func1():
    # age = 73
    print(age)   # 寻找变量，先找自己的函数内，没有就找全局变量（一层一层往上找）
    def func2():
        age = 84
        print(age)   # 寻找变量，优先自己函数、再找父级、爷爷级，最后找全局变量
    func2()
func1()
# 输出： 73  84
'''
    示例
'''
age1 = 19
def func1():
    age1 = 73
    def func2():
        print(age1)
    func2()


# 局部变量位置调整   第三章第20视频需要重新看
age = 19
def func1():
    def func2():
        print(age)
    func2()
    age = 73
func1()
'''
    执行报错，73在func2后面，func2不知道该取哪个参数
'''