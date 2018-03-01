def home():
    print("首页".center(40,'-'))
def america():
    #login()  # 改写删除该行
    print("欧美专区".center(40,'-'))
def japan():
    print("日韩专区".center(40,'-'))
def henan():
    #login()  # 改写删除该行
    print("河南专区".center(40,'-'))

'''
    需要实现henan模块和america模块会员充值收费观看。
'''
# user_status = False  # 用户登录就把这个改为True
#
# def login():
#     _username = 'alex'  # 假装这是DB里存的用户信息
#     _password = 'abc!23' # 假设这是DB里存的用户信息
#     global user_status
#
#     if user_status == False:  # 用户状态为True时可以访问视频
#         username = input("user:")
#         password = input("password:")
#
#         if username == _username and password == _password:
#             print("welcome login....")
#             user_status = True
#         else:
#             print("用户已经登录，验证通过！")
#
# henan()
# america()
'''
    软件开发中一个重要原则是"开放-封闭"原则。规定代码不允许呗修改，但可以被扩展
        封闭：已实现的功能代码块不应该被修改
        开放：对现有功能的扩展开放
    代码改写:
'''
user_status = False
def login(func):
    def inner():
        _username = "alex"
        _password = "abc!23"
        global user_status

        if user_status == False:
            username = input("user:")
            password = input("password:")
            if username == _username and password == _password:
                print("welcome login...")
                user_status = True
            else:
                print("wrong username or password!")
        else:
            print("wrong username or password!")
        if user_status:
            func()   # henan()——老的河南函数
    return inner # 加括号执行，不加括号返回内存地址

# login(henan)   # 需要验证就调用login,把需要验证的功能，当做一个参数传给login
# ogin(america)
''' 
    以上改写也不好，修改了调用方式，需要认真的模块都讲需要修改调用方式。
    需要不改变原功能代码，又不改变原有调用方式，还能加上认证的代码改写。
'''
# henan = login(henan)  # 返回内存地址，通过这个和login内的inner函数实现了扩展
# print(henan)
# henan()  # inner()执行
'''
    henan = login(henan)可以改写为如下代码：
'''
@login  # 等价于henan = login(henan)
def hubei():
    #login()  # 改写删除该行
    print("湖北专区".center(40,'-'))
