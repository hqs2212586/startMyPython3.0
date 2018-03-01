# 装饰器内要传入参数
'''
user_status = False
def login(auth_type,func):  # qq
    def inner(*args,**kwargs):   # 添加参数eg.3p
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
            # func(args,kwargs)  # 这样写是固定两个参数
            func(*args,**kwargs)   # henan()  适配任意多个参数
    return inner # 加括号执行，不加括号返回内存地址

def home():
    print("首页".center(40,'-'))
def america():
    print("欧美专区".center(40,'-'))
def japan():
    print("日韩专区".center(40,'-'))
def henan(style):
    print("河南专区".center(40,'-'),style)

henan = login('qq',henan)
henan('3p')
print(henan)
'''


# 装饰器带参数多包了一层函数，装饰器执行流程
user_status = False


def login(auth_type):  # qq

    def outer(func):
        def inner(*args,**kwargs):   # 添加参数eg.3p
            _username = "alex"
            _password = "abc!23"
            global user_status

            # if user_status == False:
            if user_status is False:
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
                # func(args,kwargs)  # 这样写是固定两个参数
                func(*args,*kwargs)   # henan()  适配任意多个参数
        return inner # 加括号执行，不加括号返回内存地址
    return outer


def home():
    print("首页".center(40,'-'))


def america():
    print("欧美专区".center(40,'-'))


def japan():
    print("日韩专区".center(40,'-'))
'''
def henan(style):
    print("河南专区".center(40,'-'),style)

xx = login('qq')   # outer地址
print(xx)

henan = xx(henan)
print(henan)

henan('3p')
'''

# 装饰器用@改写
# 不调用就会默认执行login


@login('qq')   # login('qq')——>outer(henan)——>inner('3p')返回新河南
def henan(style):
    print("河南专区".center(40,'-'),style)

henan('3p')